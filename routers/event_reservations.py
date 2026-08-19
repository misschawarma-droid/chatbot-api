# routers/event_reservations.py — Réservations d'événements (anniversaire,
# séminaire, repas d'affaires, baby shower, soirée privée...)
#
# Contrairement aux réservations de table, il n'y a pas de vérification de
# créneau/disponibilité ici : chaque demande est manuellement traitée et
# confirmée par l'équipe depuis le dashboard admin (voir admin.py ->
# EventReservationAdmin.confirm_reservation).

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import EventReservation
from schemas import EventReservationIn
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/api/reservations/event", tags=["event-reservations"])


@router.post("", status_code=201)
def creer_reservation_event(d: EventReservationIn, db: Session = Depends(get_db)):
    reservation = EventReservation(
        event_type=d.event_type,
        first_name=d.first_name,
        last_name=d.last_name,
        email=d.email,
        phone=d.phone,
        date=d.date,
        time=d.time,
        guests=d.guests,
        details=d.details or "",
        note=d.note or "",
        language=d.language or "fr",
        status="nouvelle",
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    # Notification interne à Ali : SMS + email
    sms_ali = (
        f"🔔 Nouvel événement : {d.first_name} {d.last_name} — \"{d.event_type}\" "
        f"le {d.date} à {d.time} pour {d.guests} pers. Dashboard : {ADMIN_DASHBOARD_URL}"
    )
    if ALI_PHONE:
        send_sms(ALI_PHONE, sms_ali)

    email_body = (
        f"<p>Nouvelle demande d'événement reçue :</p>"
        f"<p>🎉 {d.event_type}<br>"
        f"👤 {d.first_name} {d.last_name}<br>"
        f"📞 {d.phone}<br>"
        f"📧 {d.email}<br>"
        f"📅 {d.date} à {d.time}<br>"
        f"👥 {d.guests} personne(s)<br>"
        f"📝 {d.details or '—'}<br>"
        f"💬 {d.note or '—'}</p>"
        f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
    )
    send_email(SMTP_EMAIL, "🔔 Nouvelle demande d'événement : Miss Chawarma", email_body, html=True)

    return {"id": reservation.id, "status": reservation.status}
