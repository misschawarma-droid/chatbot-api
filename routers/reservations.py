# routers/reservations.py — Réservations de table et d'événements

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import TableReservation, EventReservation
from schemas import TableReservationIn, EventReservationIn

router = APIRouter(prefix="/api/reservations", tags=["reservations"])


@router.post("/table")
def create_table_reservation(payload: TableReservationIn, db: Session = Depends(get_db)):
    reservation = TableReservation(**payload.model_dump())
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return {"id": reservation.id, "status": "ok"}


@router.post("/event")
def create_event_reservation(payload: EventReservationIn, db: Session = Depends(get_db)):
    reservation = EventReservation(**payload.model_dump())
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return {"id": reservation.id, "status": "ok"}
