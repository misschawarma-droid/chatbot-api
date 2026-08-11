"""Routes du dashboard et du calendrier Miss Chawarma."""

from collections import Counter
from datetime import date, datetime
from typing import Any

from fastapi import Query, Request
from starlette.responses import JSONResponse

from database import SessionLocal
from models import Order, TableReservation, EventReservation, ContactMessage


def _iso_date(value: Any) -> str:
    """Convertit une date SQLAlchemy, datetime ou chaîne en YYYY-MM-DD."""
    if value is None:
        return ""

    if isinstance(value, datetime):
        return value.date().isoformat()

    if isinstance(value, date):
        return value.isoformat()

    text = str(value).strip()
    return text[:10]


def _display_time(value: Any) -> str:
    if value is None:
        return ""

    if hasattr(value, "strftime"):
        try:
            return value.strftime("%H:%M")
        except (TypeError, ValueError):
            pass

    text = str(value).strip()
    return text[:5]


def register_admin_dashboard_routes(app) -> None:
    @app.get("/admin-dashboard-data")
    async def admin_dashboard_data(request: Request):
        if not request.session.get("authenticated"):
            return JSONResponse({"detail": "Non autorisé"}, status_code=401)

        db = SessionLocal()
        try:
            return {
                "orders": db.query(Order).count(),
                "tables": db.query(TableReservation).count(),
                "events": db.query(EventReservation).count(),
                "messages": (
                    db.query(ContactMessage)
                    .filter(ContactMessage.is_read.is_(False))
                    .count()
                ),
            }
        finally:
            db.close()

    @app.get("/admin-calendar")
    async def admin_calendar(
        request: Request,
        year: int = Query(..., ge=2020, le=2100),
        month: int = Query(..., ge=1, le=12),
    ):
        """Nombre de réservations de tables et d'événements par jour."""
        if not request.session.get("authenticated"):
            return JSONResponse({"detail": "Non autorisé"}, status_code=401)

        db = SessionLocal()
        try:
            table_reservations = db.query(TableReservation).all()
            event_reservations = db.query(EventReservation).all()

            table_counts = Counter()
            event_counts = Counter()

            for reservation in table_reservations:
                value = _iso_date(reservation.date)
                if not value:
                    continue

                try:
                    reservation_date = date.fromisoformat(value)
                except ValueError:
                    continue

                if reservation_date.year == year and reservation_date.month == month:
                    table_counts[value] += 1

            for reservation in event_reservations:
                value = _iso_date(reservation.date)
                if not value:
                    continue

                try:
                    reservation_date = date.fromisoformat(value)
                except ValueError:
                    continue

                if reservation_date.year == year and reservation_date.month == month:
                    event_counts[value] += 1

            all_days = sorted(set(table_counts) | set(event_counts))
            days = {
                day: {
                    "tables": table_counts.get(day, 0),
                    "events": event_counts.get(day, 0),
                    "total": table_counts.get(day, 0) + event_counts.get(day, 0),
                }
                for day in all_days
            }

            return {
                "year": year,
                "month": month,
                "days": days,
                "totals": {
                    "tables": sum(table_counts.values()),
                    "events": sum(event_counts.values()),
                    "all": sum(table_counts.values()) + sum(event_counts.values()),
                },
            }
        finally:
            db.close()

    @app.get("/admin-calendar/day")
    async def admin_calendar_day(
        request: Request,
        selected_date: str = Query(..., alias="date"),
    ):
        """Détails des réservations de tables et événements d'une journée."""
        if not request.session.get("authenticated"):
            return JSONResponse({"detail": "Non autorisé"}, status_code=401)

        try:
            date.fromisoformat(selected_date)
        except ValueError:
            return JSONResponse(
                {"detail": "Date invalide. Format attendu : YYYY-MM-DD"},
                status_code=400,
            )

        db = SessionLocal()
        try:
            table_reservations = [
                reservation
                for reservation in db.query(TableReservation).all()
                if _iso_date(reservation.date) == selected_date
            ]
            event_reservations = [
                reservation
                for reservation in db.query(EventReservation).all()
                if _iso_date(reservation.date) == selected_date
            ]

            table_reservations.sort(
                key=lambda reservation: _display_time(reservation.time)
            )
            event_reservations.sort(
                key=lambda reservation: _display_time(reservation.time)
            )

            return {
                "date": selected_date,
                "counts": {
                    "tables": len(table_reservations),
                    "events": len(event_reservations),
                    "all": len(table_reservations) + len(event_reservations),
                },
                "tables": [
                    {
                        "id": reservation.id,
                        "first_name": reservation.first_name or "",
                        "last_name": reservation.last_name or "",
                        "phone": reservation.phone or "",
                        "email": reservation.email or "",
                        "time": _display_time(reservation.time),
                        "guests": reservation.guests or 0,
                        "status": reservation.status or "nouvelle",
                        "tables": reservation.table_ids or "",
                        "note": reservation.note or "",
                        "details_url": (
                            f"/admin/table-reservation/details/{reservation.id}"
                        ),
                    }
                    for reservation in table_reservations
                ],
                "events": [
                    {
                        "id": reservation.id,
                        "event_type": reservation.event_type or "Événement",
                        "first_name": reservation.first_name or "",
                        "last_name": reservation.last_name or "",
                        "phone": reservation.phone or "",
                        "email": reservation.email or "",
                        "time": _display_time(reservation.time),
                        "guests": reservation.guests or 0,
                        "status": reservation.status or "nouvelle",
                        "note": reservation.note or "",
                        "details_url": (
                            f"/admin/event-reservation/details/{reservation.id}"
                        ),
                    }
                    for reservation in event_reservations
                ],
            }
        finally:
            db.close()