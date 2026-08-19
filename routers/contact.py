from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from database import get_db
from models import ContactMessage
from schemas import ContactIn
from notifications import send_sms, send_email, ALI_PHONE, ADMIN_DASHBOARD_URL, SMTP_EMAIL

router = APIRouter(prefix="/api/contact", tags=["contact"])


def _notify_staff(name: str, email: str, message: str):
    sms_ali = f"🔔 Nouveau message contact de {name}. Dashboard : {ADMIN_DASHBOARD_URL}"
    if ALI_PHONE:
        send_sms(ALI_PHONE, sms_ali)

    email_body = (
        f"<p>Nouveau message reçu :</p>"
        f"<p>👤 {name}<br>📧 {email}</p>"
        f"<p>{message}</p>"
        f"<p><a href=\"{ADMIN_DASHBOARD_URL}\">Ouvrir le dashboard</a></p>"
    )
    send_email(SMTP_EMAIL, "🔔 Nouveau message contact — Miss Chawarma", email_body, html=True)


@router.post("")
def create_contact_message(payload: ContactIn, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    msg = ContactMessage(**payload.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)

    background_tasks.add_task(_notify_staff, msg.name, msg.email, msg.message)

    return {"id": msg.id, "status": "ok"}