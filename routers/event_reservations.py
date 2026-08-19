# routers/event_reservations.py — Réservations d'événements (anniversaire,
# séminaire, repas d'affaires, baby shower, soirée privée...)
#
# Les notifications à Ali (SMS + email) sont envoyées en tâche de fond
# (BackgroundTasks) : la réponse au client part immédiatement après
# l'enregistrement en base, sans attendre que Twilio/Gmail répondent.

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import EventReservation
from schemas import EventReservationIn
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/api/reservations/event", tags=["event-reservations"])


def _notify_staff(event_type, first_name, last_name, email, phone, date, time, guests, details, note):
    """Exécuté en arrière-plan, après que la réponse HTTP soit déjà partie."""
    sms_ali = (
        f"🔔 Nouvel événement : {first_name} {last_name} — \"{event_type}\" "
        f"le {date} à {time} pour {guests} pers. Dashboard : {ADMIN_DASHBOARD_URL}"
    )
    if ALI_PHONE:
        send_sms(ALI_PHONE, sms_ali)

    email_body = (
        f"<p>Nouvelle demande d'événement reçue :</p>"
        f"<p>🎉 {event_type}<br>"
        f"👤 {first_name} {last_name}<br>"
        f"📞 {phone}<br>"
        f"📧 {email}<br>"
        f"📅 {date} à {time}<br>"
        f"👥 {guests} personne(s)<br>"
        f"📝 {details or '—'}<br>"
        f"💬 {note or '—'}</p>"
        f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
    )
    send_email(SMTP_EMAIL, "🔔 Nouvelle demande d'événement — Miss Chawarma", email_body, html=True)


@router.post("", status_code=201)
def creer_reservation_event(
    d: EventReservationIn,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
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

    background_tasks.add_task(
        _notify_staff,
        d.event_type, d.first_name, d.last_name, d.email, d.phone,
        d.date, d.time, d.guests, d.details, d.note,
    )

    return {"id": reservation.id, "status": reservation.status}
