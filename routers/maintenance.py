from fastapi import APIRouter, Depends, HTTPException, Header
import os
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from database import get_db
from models import TableReservation, EventReservation, ContactMessage

router = APIRouter(prefix="/api/maintenance", tags=["maintenance"])
MAINTENANCE_SECRET = os.getenv("MAINTENANCE_SECRET")
@router.post("/purge-old-data")
def purge_old_data(
    db: Session = Depends(get_db),
    x_maintenance_key: str = Header(None),
):
    if not MAINTENANCE_SECRET or x_maintenance_key != MAINTENANCE_SECRET:
        raise HTTPException(status_code=403, detail="forbidden")

    seuil = datetime.utcnow() - timedelta(days=3 * 365)

    deleted_tables = db.query(TableReservation).filter(TableReservation.created_at < seuil).delete()
    deleted_events = db.query(EventReservation).filter(EventReservation.created_at < seuil).delete()
    deleted_contacts = db.query(ContactMessage).filter(ContactMessage.created_at < seuil).delete()

    db.commit()
    return {
        "status": "purged",
        "seuil": str(seuil),
        "deleted": {
            "table_reservations": deleted_tables,
            "event_reservations": deleted_events,
            "contact_messages": deleted_contacts,
        },
    }