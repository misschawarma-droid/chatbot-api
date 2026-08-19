# routers/contact.py — Messages du formulaire de contact

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ContactMessage
from schemas import ContactIn
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/api/contact", tags=["contact"])


@router.post("")
def create_contact_message(payload: ContactIn, db: Session = Depends(get_db)):
    msg = ContactMessage(**payload.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)

    # Notification interne à Ali : SMS + email
    sms_ali = (
        f"🔔 Nouveau message contact de {msg.name}. "
        f"Dashboard : {ADMIN_DASHBOARD_URL}"
    )
    if ALI_PHONE:
        send_sms(ALI_PHONE, sms_ali)

    email_body = (
        f"<p>Nouveau message reçu :</p>"
        f"<p>👤 {msg.name}<br>"
        f"📧 {msg.email}</p>"
        f"<p>{msg.message}</p>"
        f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
    )
    send_email(SMTP_EMAIL, "🔔 Nouveau message contact : Miss Chawarma", email_body, html=True)

    return {"id": msg.id, "status": "ok"}
