# routers/contact.py — Messages du formulaire de contact

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ContactMessage
from schemas import ContactIn

router = APIRouter(prefix="/api/contact", tags=["contact"])


@router.post("")
def create_contact_message(payload: ContactIn, db: Session = Depends(get_db)):
    msg = ContactMessage(**payload.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {"id": msg.id, "status": "ok"}
