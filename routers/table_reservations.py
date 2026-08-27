# routers/table_reservations.py — Réservations de table
#
# Disponibilité + création + modification + annulation, avec vérification
# du chevauchement horaire. Les notifications à Ali (SMS + email) partent
# en tâche de fond (BackgroundTasks) pour ne pas ralentir la réponse.
#
# Modification/annulation : le client s'identifie avec sa référence (id)
# + son email — pas de compte, pas de mot de passe, volontairement simple.

import json
from datetime import datetime as DT

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db
from models import TableReservation, TableSlot
from schemas import (
    TableReservationIn, TableReservationOut, TableAvailabilityOut,
    TableReservationLookupIn, TableReservationLookupOut,
    TableReservationModifyIn, TableReservationCancelIn,
)

from notifications import send_admin_sms, send_email, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/table-reservations", tags=["table-reservations"])

# ---------------------------------------------------------------- horaires --
OUVERTURE_MIN = 11 * 60 + 30
FERMETURE_MIN = {  # 0 = lundi … 6 = dimanche
    0: 24 * 60, 1: 24 * 60, 2: 24 * 60,
    3: 26 * 60, 4: 26 * 60, 5: 26 * 60, 6: 26 * 60,
}
PAS_MIN = 30
DUREE_SERVICE_MIN = 90
DERNIERE_ARRIVEE_AVANT_FERMETURE = 60
MAX_CONVIVES = 12


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


# --------------------------------------------- géométrie du plan (port JS) --
# Même géométrie que components/PlanDeSalle.tsx côté front — nécessaire ici
# pour ré-attribuer automatiquement des tables lors d'une MODIFICATION.
PLACES_PAR_TABLE = 2
TABLE_PLACES = {
    "21": 4, "20": 4, "19": 2, "18": 2,
    "17": 2, "16": 2, "15": 2, "14": 2,
    "13": 2, "12": 2, "11": 2, "10": 2, "8": 2, "9": 2,
    "7": 2, "6": 2, "5": 2, "4": 2, "3": 2, "2": 2, "1": 2,
    "T1": 2, "T2": 2, "T3": 2, "T4": 2, "T5": 2, "T6": 2,
}
PAIRES_FORCEES = [("13", "12"), ("11", "10"), ("8", "9")]
INSTA_A, INSTA_B, INSTA_COMBINE = "19", "18", 5

# Chaînes de tables voisines (même ordre que CHAINES côté front)
CHAINES = [
    [["21"], ["20"]],
    [["19", "18"]],  # unité combinée insta
    [["17"], ["16"], ["15"], ["14"]],
    [["13", "12"], ["11", "10"], ["8", "9"]],
    [["7"], ["6"], ["5"], ["4"], ["3"], ["2"], ["1"]],
    [["T1"], ["T2"], ["T3"], ["T4"], ["T5"], ["T6"]],
]


def places_unite(ids: list[str]) -> int:
    if set(ids) == {INSTA_A, INSTA_B}:
        return INSTA_COMBINE
    return sum(TABLE_PLACES.get(i, PLACES_PAR_TABLE) for i in ids)


def chercher_bloc(nb: int, occupees: set[str]) -> list[str] | None:
    """Cherche le plus petit bloc de tables voisines libres pour `nb` convives.
    Port de l'algorithme chercherBloc() du frontend (PlanDeSalle.tsx)."""
    meilleur, meilleur_score = None, float("inf")

    for chaine in CHAINES:
        for i in range(len(chaine)):
            bloc_ids: list[str] = []
            places = 0
            for j in range(i, len(chaine)):
                unite = chaine[j]
                if any(t in occupees for t in unite):
                    break
                bloc_ids += unite
                places += places_unite(unite)
                if places < nb:
                    continue
                score = (places - nb) * 10 + len(bloc_ids)
                if score < meilleur_score:
                    meilleur_score, meilleur = score, list(bloc_ids)
                break

    return meilleur


def purger_expirees(db: Session):
    pass


# --------------------------------------------------------------- endpoints --

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
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    minute = minutes_depuis(d.time)
    if not creneau_valide(d.date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    fenetre = fenetre_occupee(d.date, minute)

    reservation = TableReservation(
        first_name=d.first_name, last_name=d.last_name,
        email=d.email, phone=d.phone,
        date=d.date, time=d.time, guests=d.guests,
        note=d.note or "", language=d.language or "fr",
        status="nouvelle",
        table_ids=json.dumps(d.table_ids),
    )
    db.add(reservation)
    db.flush()

    for tid in d.table_ids:
        for m in fenetre:
            db.add(TableSlot(reservation_id=reservation.id, date=d.date, minute=m, table_id=str(tid)))

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        prises = db.execute(
            select(TableSlot.table_id).where(
                TableSlot.date == d.date,
                TableSlot.minute.in_(fenetre),
                TableSlot.table_id.in_([str(t) for t in d.table_ids]),
            ).distinct()
        ).scalars().all()
        raise HTTPException(status_code=409, detail={"table_ids": prises})

    def _notify_new():
        # SMS interne uniquement vers ALI_PHONE_NUMBER.
        # Court + sans emoji/URL pour rester sur un seul segment Twilio.
        send_admin_sms(
        f"Miss Chawarma 😊\n\n"
        f"Nouvelle réservation de table - "
        f"{d.first_name} {d.last_name} - {d.date} {d.time} - {d.guests} pers. "
        f"Dashboard: {ADMIN_DASHBOARD_URL}"
       )
        email_body = (
            f"<p>Nouvelle réservation reçue :</p>"
            f"<p>👤 {d.first_name} {d.last_name}<br>"
            f"📞 {d.phone}<br>📧 {d.email}<br>"
            f"📅 {d.date} à {d.time}<br>👥 {d.guests} personne(s)</p>"
            f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
        )
        send_email(SMTP_EMAIL, "🔔 Nouvelle réservation de table : Miss Chawarma", email_body, html=True)

    background_tasks.add_task(_notify_new)

    db.refresh(reservation)
    return {"id": reservation.id, "table_ids": d.table_ids, "status": reservation.status}


def _trouver_reservation_active(db: Session, reference: int, email: str) -> TableReservation:
    reservation = db.get(TableReservation, reference)
    if (
        not reservation
        or reservation.email.strip().lower() != email.strip().lower()
        or reservation.status == "annulée"
    ):
        raise HTTPException(status_code=404, detail="Réservation introuvable.")
    return reservation


@router.post("/lookup", response_model=TableReservationLookupOut)
def retrouver_reservation(d: TableReservationLookupIn, db: Session = Depends(get_db)):
    reservation = _trouver_reservation_active(db, d.reference, d.email)
    return {
        "id": reservation.id,
        "first_name": reservation.first_name,
        "last_name": reservation.last_name,
        "phone": reservation.phone,   # ⟵ AJOUT
        "date": reservation.date,
        "time": reservation.time,
        "guests": reservation.guests,
        "table_ids": json.loads(reservation.table_ids or "[]"),
        "status": reservation.status,
    }

@router.post("/modify", response_model=TableReservationOut)
def modifier_reservation(
    d: TableReservationModifyIn,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    reservation = _trouver_reservation_active(db, d.reference, d.email)

    if d.guests > MAX_CONVIVES:
        raise HTTPException(
            status_code=422,
            detail="Au-delà de 12 convives, contactez-nous directement pour une privatisation.",
        )

    minute = minutes_depuis(d.time)
    if not creneau_valide(d.date, minute):
        raise HTTPException(status_code=422, detail="Créneau hors des horaires d'ouverture.")

    fenetre = fenetre_occupee(d.date, minute)

    for slot in list(reservation.slots):
        db.delete(slot)
    db.flush()

    occupees = set(db.execute(
        select(TableSlot.table_id).where(
            TableSlot.date == d.date,
            TableSlot.minute.in_(fenetre),
        ).distinct()
    ).scalars().all())
    if d.first_name:
        reservation.first_name = d.first_name
    if d.last_name:
        reservation.last_name = d.last_name
    if d.phone:
        reservation.phone = d.phone

    if d.table_ids:
        if any(t in occupees for t in d.table_ids):
            db.rollback()
            raise HTTPException(status_code=409, detail="Une des tables choisies vient d'être prise.")
        if places_unite(d.table_ids) < d.guests and set(d.table_ids) != {INSTA_A, INSTA_B}:
            capacite = sum(TABLE_PLACES.get(t, PLACES_PAR_TABLE) for t in d.table_ids)
            if capacite < d.guests:
                db.rollback()
                raise HTTPException(status_code=422, detail="Pas assez de places sur les tables choisies.")
        nouvelles_tables = d.table_ids
    else:
        nouvelles_tables = chercher_bloc(d.guests, occupees)
        if nouvelles_tables is None:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail="Plus de table disponible pour ce créneau et ce nombre de convives.",
            )

    for tid in nouvelles_tables:
        for m in fenetre:
            db.add(TableSlot(reservation_id=reservation.id, date=d.date, minute=m, table_id=tid))

    reservation.date = d.date
    reservation.time = d.time
    reservation.guests = d.guests
    reservation.table_ids = json.dumps(nouvelles_tables)
    reservation.status = "nouvelle"

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Ce créneau vient d'être pris, réessayez.")

    def _notify_modif():
        send_admin_sms(
            f"Miss Chawarma: reservation modifiee - "
            f"{reservation.first_name} {reservation.last_name} - {d.date} {d.time} - {d.guests} pers. "
            f"Dashboard: {ADMIN_DASHBOARD_URL}"
        )
        email_body = (
            f"<p>Une réservation a été modifiée par le client :</p>"
            f"<p>👤 {reservation.first_name} {reservation.last_name}<br>"
            f"📅 Nouveau créneau : {d.date} à {d.time}<br>"
            f"👥 {d.guests} personne(s)</p>"
            f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
        )
        send_email(SMTP_EMAIL, "✏️ Réservation modifiée — Miss Chawarma", email_body, html=True)

    background_tasks.add_task(_notify_modif)

    db.refresh(reservation)
    return {"id": reservation.id, "table_ids": nouvelles_tables, "status": reservation.status}

@router.post("/cancel", response_model=TableReservationOut)
def annuler_reservation(
    d: TableReservationCancelIn,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    reservation = _trouver_reservation_active(db, d.reference, d.email)

    for slot in list(reservation.slots):
        db.delete(slot)
    reservation.status = "annulée"
    db.commit()

    def _notify_annulation():
        send_admin_sms(
            f"Miss Chawarma: reservation annulee - "
            f"{reservation.first_name} {reservation.last_name} - {reservation.date} {reservation.time} "
            f"Dashboard: {ADMIN_DASHBOARD_URL}"
        )
        email_body = (
            f"<p>Une réservation a été annulée par le client :</p>"
            f"<p>👤 {reservation.first_name} {reservation.last_name}<br>"
            f"📅 {reservation.date} à {reservation.time}<br>"
            f"👥 {reservation.guests} personne(s)</p>"
        )
        send_email(SMTP_EMAIL, "❌ Réservation annulée : Miss Chawarma", email_body, html=True)

    background_tasks.add_task(_notify_annulation)

    db.refresh(reservation)
    return {
        "id": reservation.id,
        "table_ids": json.loads(reservation.table_ids or "[]"),
        "status": reservation.status,
    }

   