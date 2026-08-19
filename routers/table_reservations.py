# routers/table_reservations.py — NOUVEAU FICHIER à ajouter à ton projet.
#
# S'appuie sur tes vrais models.py / schemas.py (TableReservation, TableSlot,
# TableReservationIn). Remplace l'ancien routeur s'il en existait un pour
# les réservations de table — celui-ci fait tout : disponibilité + création
# + vérification du chevauchement horaire.
#
# ⚠️ Vérifie le chemin d'import de `get_db` et `SessionLocal` : j'ai supposé
# qu'ils viennent de `database.py`, comme `Base` dans models.py. Adapte si
# ton projet les nomme autrement.

import json
from datetime import datetime as DT, date as Date

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db          # ⟵ à adapter si le nom diffère
from models import TableReservation, TableSlot
from schemas import TableReservationIn, TableReservationOut, TableAvailabilityOut
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/table-reservations", tags=["table-reservations"])

# ---------------------------------------------------------------- horaires --
OUVERTURE_MIN = 11 * 60 + 30
FERMETURE_MIN = {  # 0 = lundi … 6 = dimanche
    0: 24 * 60, 1: 24 * 60, 2: 24 * 60,        # lun-mer -> minuit
    3: 26 * 60, 4: 26 * 60, 5: 26 * 60, 6: 26 * 60,  # jeu-dim -> 2h
}
PAS_MIN = 30
DUREE_SERVICE_MIN = 90
DERNIERE_ARRIVEE_AVANT_FERMETURE = 60


def jour_semaine(date_str: str) -> int:
    return DT.strptime(date_str, "%Y-%m-%d").weekday()


def minutes_depuis(time_str: str) -> int:
    h, m = (int(x) for x in time_str.split(":"))
    minute = h * 60 + m
    if minute < OUVERTURE_MIN:
        minute += 24 * 60
    return minute


def creneau_valide(date_str: str, minute: int) -> bool:
    fermeture = FERMETURE_MIN[jour_semaine(date_str)]
    return (
        OUVERTURE_MIN <= minute <= fermeture - DERNIERE_ARRIVEE_AVANT_FERMETURE
        and minute % PAS_MIN == 0
    )


def fenetre_occupee(date_str: str, debut: int) -> list[int]:
    fermeture = FERMETURE_MIN[jour_semaine(date_str)]
    fin = min(debut + DUREE_SERVICE_MIN, fermeture)
    return list(range(debut, fin, PAS_MIN))


def purger_expirees(db: Session):
    """Supprime les verrous 'hold' de plus de 5 minutes, s'il y en a."""
    # Pas de statut hold pour l'instant dans ce schéma simplifié — prévu
    # pour plus tard si un système de pré-réservation est ajouté.
    pass


@router.get("/availability", response_model=TableAvailabilityOut)
def disponibilites(date: str = Query(...), time: str = Query(...), db: Session = Depends(get_db)):
    minute = minutes_depuis(time)
    if not creneau_valide(date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    fenetre = fenetre_occupee(date, minute)
    occupees = db.execute(
        select(TableSlot.table_id).where(
            TableSlot.date == date,
            TableSlot.minute.in_(fenetre),
        ).distinct()
    ).scalars().all()

    return {"occupied_table_ids": occupees}


@router.post("", response_model=TableReservationOut, status_code=201)
def creer_reservation(
    d: TableReservationIn,
    background_tasks: BackgroundTasks,   # ⟵ AJOUT
    db: Session = Depends(get_db),
):
    ...
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        prises = db.execute(...).scalars().all()
        raise HTTPException(status_code=409, detail={"table_ids": prises})

    def _notify():
        sms_ali = (
            f"🔔 Nouvelle réservation table : {d.first_name} {d.last_name} le {d.date} "
            f"à {d.time} pour {d.guests} pers. Dashboard : {ADMIN_DASHBOARD_URL}"
        )
        if ALI_PHONE:
            send_sms(ALI_PHONE, sms_ali)

        email_body = (
            f"<p>Nouvelle réservation reçue :</p>"
            f"<p>👤 {d.first_name} {d.last_name}<br>"
            f"📞 {d.phone}<br>📧 {d.email}<br>"
            f"📅 {d.date} à {d.time}<br>👥 {d.guests} personne(s)</p>"
            f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
        )
        send_email(SMTP_EMAIL, "🔔 Nouvelle réservation de table : Miss Chawarma", email_body, html=True)

    background_tasks.add_task(_notify)

    db.refresh(reservation)
    return {"id": reservation.id, "table_ids": d.table_ids, "status": reservation.status}