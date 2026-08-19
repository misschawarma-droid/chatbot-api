# app/routers/reservations.py — Miss Chawarma
#
# Horaires réels : ouvert 7j/7, 11h30 →
#   lundi–mercredi : minuit
#   jeudi–dimanche : 2h du matin
#
# Deux idées structurent ce fichier :
#
# 1. JOUR DE SERVICE. Un dîner du vendredi à 00h30 appartient au service du
#    VENDREDI, pas au samedi. On stocke donc `jour` = date de service, et
#    `minute` = minutes depuis minuit de ce jour — qui peut dépasser 1440
#    (00h30 le lendemain = 1470). Aucune ambiguïté possible.
#
# 2. UNE LIGNE PAR CRÉNEAU OCCUPÉ. Une table réservée à 20h00 pour 1h30
#    bloque 20h00, 20h30 et 21h00 : trois lignes. La contrainte UNIQUE
#    empêche alors atomiquement toute double réservation, y compris
#    chevauchante, sans verrou applicatif.

from datetime import date as Date, datetime, timedelta
from typing import List, Optional
import os, secrets

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import (Column, Date as SADate, DateTime, Integer, String,
                        UniqueConstraint, create_engine, select, delete)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL
# ---------------------------------------------------------------- horaires --
OUVERTURE_MIN = 11 * 60 + 30           # 11h30
FERMETURE_MIN = {                       # 0 = lundi … 6 = dimanche
    0: 24 * 60,                         # lundi     → 00h00
    1: 24 * 60,                         # mardi     → 00h00
    2: 24 * 60,                         # mercredi  → 00h00
    3: 26 * 60,                         # jeudi     → 02h00
    4: 26 * 60,                         # vendredi  → 02h00
    5: 26 * 60,                         # samedi    → 02h00
    6: 26 * 60,                         # dimanche  → 02h00
}
PAS_MIN = 30                            # granularité des créneaux
DUREE_SERVICE_MIN = 90                  # durée d'occupation d'une table
DERNIERE_ARRIVEE_AVANT_FERMETURE = 60


def minutes_depuis(creneau: str, jour: Date) -> int:
    """'20:00' -> 1200 ; '00:30' -> 1470 (appartient au service de `jour`)."""
    h, m = (int(x) for x in creneau.split(":"))
    minute = h * 60 + m
    if minute < OUVERTURE_MIN:          # avant l'ouverture => après minuit
        minute += 24 * 60
    return minute


def creneau_valide(jour: Date, minute: int) -> bool:
    fermeture = FERMETURE_MIN[jour.weekday()]
    return (
        OUVERTURE_MIN <= minute <= fermeture - DERNIERE_ARRIVEE_AVANT_FERMETURE
        and minute % PAS_MIN == 0
    )


def creneaux_occupes(jour: Date, debut: int) -> List[int]:
    """Créneaux bloqués par une arrivée à `debut`, sans dépasser la fermeture."""
    fermeture = FERMETURE_MIN[jour.weekday()]
    fin = min(debut + DUREE_SERVICE_MIN, fermeture)
    return list(range(debut, fin, PAS_MIN))


# ------------------------------------------------------------------- base ---
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./misschawarma.db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


class Occupation(Base):
    """Une ligne = une table occupée sur un créneau de 30 min."""
    __tablename__ = "occupations"
    __table_args__ = (
        UniqueConstraint("jour", "minute", "table_id", name="uniq_table_creneau"),
    )

    id = Column(Integer, primary_key=True)
    jour = Column(SADate, nullable=False, index=True)
    minute = Column(Integer, nullable=False, index=True)
    table_id = Column(String(8), nullable=False)

    reference = Column(String(12), nullable=False, index=True)
    statut = Column(String(10), nullable=False, default="confirmee")  # hold | confirmee
    expire_le = Column(DateTime, nullable=True)

    convives = Column(Integer, nullable=False)
    nom = Column(String(120), nullable=False)
    tel = Column(String(40), nullable=False)
    email = Column(String(160))
    note = Column(String(400))
    lang = Column(String(5), default="fr")
    cree_le = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def purger_holds(db: Session):
    db.execute(delete(Occupation).where(
        Occupation.statut == "hold",
        Occupation.expire_le < datetime.utcnow(),
    ))
    db.commit()


# ---------------------------------------------------------------- schémas ---
class DemandeReservation(BaseModel):
    date: Date
    creneau: str = Field(pattern=r"^\d{2}:\d{2}$")
    tables: List[str] = Field(min_length=1, max_length=6)
    convives: int = Field(ge=1, le=12)
    nom: str = Field(min_length=2, max_length=120)
    tel: str = Field(min_length=6, max_length=40)
    email: Optional[str] = None
    note: Optional[str] = None
    lang: str = "fr"


router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/horaires")
def horaires():
    """Le front peut lire les horaires ici plutôt que de les dupliquer."""
    return {
        "ouverture": "11:30",
        "fermeture": {j: f"{(m // 60) % 24:02d}:{m % 60:02d}" for j, m in FERMETURE_MIN.items()},
        "pas": PAS_MIN,
        "duree_service": DUREE_SERVICE_MIN,
        "ouvert_7j7": True,
    }


@router.get("/availability")
def disponibilites(date: Date = Query(...), creneau: str = Query(...),
                   db: Session = Depends(get_db)):
    purger_holds(db)
    minute = minutes_depuis(creneau, date)

    if not creneau_valide(date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    # une table est prise si elle l'est sur N'IMPORTE lequel des créneaux
    # que cette nouvelle arrivée occuperait
    fenetre = creneaux_occupes(date, minute)
    occupees = db.execute(
        select(Occupation.table_id).where(
            Occupation.jour == date,
            Occupation.minute.in_(fenetre),
        ).distinct()
    ).scalars().all()

    return {
        "occupees": occupees,
        "creneau": creneau,
        "duree_service": DUREE_SERVICE_MIN,
        "serverTime": datetime.utcnow().isoformat(),
    }


@router.post("", status_code=201)
def creer(d: DemandeReservation, db: Session = Depends(get_db)):
    purger_holds(db)
    minute = minutes_depuis(d.creneau, d.date)

    if not creneau_valide(d.date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    reference = secrets.token_hex(3).upper()
    fenetre = creneaux_occupes(d.date, minute)

    for tid in d.tables:
        for m in fenetre:
            db.add(Occupation(
                jour=d.date, minute=m, table_id=str(tid),
                reference=reference, statut="confirmee",
                convives=d.convives, nom=d.nom, tel=d.tel,
                email=d.email, note=d.note, lang=d.lang,
            ))

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        prises = db.execute(
            select(Occupation.table_id).where(
                Occupation.jour == d.date,
                Occupation.minute.in_(fenetre),
                Occupation.table_id.in_([str(t) for t in d.tables]),
            ).distinct()
        ).scalars().all()
        raise HTTPException(status_code=409, detail={"tables": prises})

        # Notification interne à Ali : SMS + email
    sms_ali = (
        f"🔔 Nouvelle réservation table : {d.nom} le {d.date} à {d.creneau} "
        f"pour {d.convives} pers. Dashboard : {ADMIN_DASHBOARD_URL}"
    )
    if ALI_PHONE:
        send_sms(ALI_PHONE, sms_ali)

    email_body = (
        f"<p>Nouvelle réservation reçue :</p>"
        f"<p>👤 {d.nom}<br>"
        f"📞 {d.tel}<br>"
        f"📧 {d.email or ':'}<br>"
        f"📅 {d.date} à {d.creneau}<br>"
        f"👥 {d.convives} personne(s)<br>"
        f"🪑 Table(s) : {', '.join(str(t) for t in d.tables)}<br>"
        f"📝 {d.note or '—'}</p>"
        f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
    )
    send_email(SMTP_EMAIL, "🔔 Nouvelle réservation de table : Miss Chawarma", email_body, html=True)

    # TODO : e-mail de confirmation au CLIENT (reste à faire séparément, avec table_reservation_confirmed)
    return {"reference": reference, "tables": d.tables, "creneau": d.creneau}



@router.post("/hold", status_code=201)
def poser_hold(d: DemandeReservation, db: Session = Depends(get_db)):
    """Réserve 5 minutes le temps que le client remplisse ses coordonnées."""
    purger_holds(db)
    minute = minutes_depuis(d.creneau, d.date)
    if not creneau_valide(d.date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    reference = secrets.token_hex(3).upper()
    expire = datetime.utcnow() + timedelta(minutes=5)
    for tid in d.tables:
        for m in creneaux_occupes(d.date, minute):
            db.add(Occupation(
                jour=d.date, minute=m, table_id=str(tid),
                reference=reference, statut="hold", expire_le=expire,
                convives=d.convives, nom="—", tel="—", lang=d.lang,
            ))
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail={"tables": d.tables})
    return {"reference": reference, "expire_le": expire.isoformat()}


@router.get("/jour")
def vue_service(date: Date = Query(...), db: Session = Depends(get_db)):
    """Vue salle pour l'équipe : qui est là, à quelle table, à quelle heure."""
    purger_holds(db)
    lignes = db.execute(
        select(Occupation).where(Occupation.jour == date).order_by(Occupation.minute)
    ).scalars().all()

    par_ref = {}
    for o in lignes:
        r = par_ref.setdefault(o.reference, {
            "reference": o.reference, "nom": o.nom, "tel": o.tel,
            "convives": o.convives, "note": o.note, "statut": o.statut,
            "tables": set(), "arrivee": o.minute,
        })
        r["tables"].add(o.table_id)
        r["arrivee"] = min(r["arrivee"], o.minute)

    return [
        {**r, "tables": sorted(r["tables"]),
         "arrivee": f"{(r['arrivee'] // 60) % 24:02d}:{r['arrivee'] % 60:02d}"}
        for r in sorted(par_ref.values(), key=lambda x: x["arrivee"])
    ]
