# admin.py — Interface d'administration SQLAdmin (/admin)
# Login/mot de passe définis dans .env : ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY

import os
from sqladmin import Admin, ModelView, action
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse, HTMLResponse

from database import engine, SessionLocal
from models import (
    Category,
    Dish,
    Order,
    OrderItem,
    TableReservation,
    EventReservation,
    ContactMessage,
    Review,
    ReviewsSummary,
)
from notifications import (
    send_email,
    send_sms,
    table_reservation_confirmed,
    event_reservation_confirmed,
    contact_acknowledgement,
    table_issue_message,
    event_issue_message,
    issue_email_subject,
    contact_reply_default_message,
    contact_reply_subject,
)


# ─────────────── Page « Signaler un problème » / « Répondre » (formulaire éditable) ───────────────

def _issue_form_html(
    action_path: str,
    cancel_url: str,
    heading: str,
    subtitle: str,
    default_message: str,
    show_sms: bool = True,
    quoted: str | None = None,
) -> str:
    """Petite page HTML autonome : message pré-rempli, modifiable, avant envoi réel.
    `quoted`, si fourni, affiche le message original en lecture seule au-dessus du champ éditable."""
    escaped_message = (
        default_message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )
    sms_checkbox = (
        '<label class="checkbox"><input type="checkbox" name="send_sms" checked> Envoyer par SMS</label>'
        if show_sms
        else ""
    )
    quoted_block = ""
    if quoted:
        escaped_quoted = quoted.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        quoted_block = f"""
        <div class="quoted">
          <div class="quoted-label">Message reçu :</div>
          <div class="quoted-text">{escaped_quoted}</div>
        </div>"""
    return f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{heading}</title>
<style>
  body {{ font-family: -apple-system, Arial, sans-serif; background: #f7f0e4; margin: 0; padding: 40px 20px; }}
  .card {{ max-width: 640px; margin: 0 auto; background: white; border-radius: 10px;
           padding: 32px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
  h1 {{ color: #1f6b2d; font-size: 20px; margin-top: 0; }}
  .subtitle {{ color: #666; font-size: 14px; margin-bottom: 20px; }}
  .quoted {{ background: #f7f0e4; border-left: 3px solid #c47d0e; border-radius: 4px;
             padding: 12px 14px; margin-bottom: 18px; }}
  .quoted-label {{ font-size: 12px; color: #888; margin-bottom: 4px; }}
  .quoted-text {{ font-size: 14px; color: #444; white-space: pre-wrap; }}
  textarea {{ width: 100%; min-height: 180px; font-size: 14px; padding: 12px;
              border: 1px solid #ccc; border-radius: 6px; font-family: inherit;
              box-sizing: border-box; resize: vertical; }}
  label.checkbox {{ display: inline-flex; align-items: center; gap: 6px; margin-right: 20px;
                     font-size: 14px; color: #333; margin-top: 14px; }}
  .actions {{ margin-top: 24px; display: flex; gap: 12px; }}
  button, a.btn {{ padding: 10px 20px; border-radius: 6px; border: none; font-size: 14px;
                   cursor: pointer; text-decoration: none; display: inline-block; }}
  .confirm {{ background: #1f6b2d; color: white; font-weight: 600; }}
  .cancel {{ background: #eee; color: #333; }}
</style>
</head>
<body>
  <div class="card">
    <h1>{heading}</h1>
    <div class="subtitle">{subtitle}</div>
    {quoted_block}
    <form method="post" action="{action_path}">
      <textarea name="message">{escaped_message}</textarea>
      <div>
        <label class="checkbox"><input type="checkbox" name="send_email" checked> Envoyer par email</label>
        {sms_checkbox}
      </div>
      <div class="actions">
        <button type="submit" class="confirm">Confirmer l'envoi</button>
        <a class="btn cancel" href="{cancel_url}">Annuler</a>
      </div>
    </form>
  </div>
</body>
</html>
"""


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username", "")
        password = form.get("password", "")
        if (
            username == os.getenv("ADMIN_USERNAME", "admin")
            and password == os.getenv("ADMIN_PASSWORD", "")
            and os.getenv("ADMIN_PASSWORD")  # refuse si pas de mot de passe défini
        ):
            request.session.update({"authenticated": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("authenticated", False)


class CategoryAdmin(ModelView, model=Category):
    name = "Catégorie"
    name_plural = "Catégories"
    icon = "fa-solid fa-list"
    column_list = [Category.id, Category.name_fr, Category.position]
    column_default_sort = ("position", False)


class DishAdmin(ModelView, model=Dish):
    name = "Plat"
    name_plural = "Plats"
    icon = "fa-solid fa-utensils"
    column_list = [Dish.id, Dish.name_fr, Dish.price, Dish.is_available, Dish.category]
    column_searchable_list = [Dish.name_fr]
    column_sortable_list = [Dish.price, Dish.position]


class OrderAdmin(ModelView, model=Order):
    name = "Commande"
    name_plural = "Commandes"
    icon = "fa-solid fa-basket-shopping"
    column_list = [
        Order.id,
        Order.customer_name,
        Order.customer_phone,
        Order.order_type,
        Order.city,
        Order.subtotal,
        Order.delivery_fee,
        Order.total,
        Order.payment_method,
        Order.payment_status,
        Order.status,
        Order.requested_date,
        Order.requested_time,
        Order.created_at,
    ]
    column_default_sort = ("created_at", True)
    can_create = False  # les commandes viennent du site


class OrderItemAdmin(ModelView, model=OrderItem):
    name = "Ligne de commande"
    name_plural = "Lignes de commande"
    icon = "fa-solid fa-receipt"
    column_list = [OrderItem.order_id, OrderItem.dish_name, OrderItem.quantity, OrderItem.unit_price]
    can_create = False


class TableReservationAdmin(ModelView, model=TableReservation):
    name = "Réservation table"
    name_plural = "Réservations tables"
    icon = "fa-solid fa-chair"
    column_list = [
        TableReservation.id,
        TableReservation.last_name,
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
    ]
    column_default_sort = ("created_at", True)
    can_create = False

    @action(
        name="confirm",
        label="✅ Confirmer (email + SMS)",
        confirmation_message="Confirmer la/les réservation(s) sélectionnée(s) et envoyer un email + SMS de confirmation ?",
    )
    async def confirm_reservation(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                reservation = db.get(TableReservation, int(pk))
                if not reservation:
                    continue
                reservation.status = "confirmée"
                db.commit()
                db.refresh(reservation)

                subject, body, sms_text = table_reservation_confirmed(reservation)
                send_email(reservation.email, subject, body)
                send_sms(reservation.phone, sms_text)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity), status_code=302
        )

    @action(
        name="report-issue",
        label="🚨 Signaler un problème",
        add_in_detail=True,
        add_in_list=True,
    )
    async def report_issue(self, request: Request):
        pks = [p for p in request.query_params.get("pks", "").split(",") if p]
        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity), status_code=302
            )
        db = SessionLocal()
        try:
            reservation = db.get(TableReservation, int(pks[0]))
            if not reservation:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity), status_code=302
                )
            default_message = table_issue_message(reservation)
            title = (
                f"{reservation.first_name} {reservation.last_name} — "
                f"{reservation.date} {reservation.time} ({reservation.guests} pers.)"
            )
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/reservation-issue/table/{pks[0]}/send",
                cancel_url="/admin/table-reservation/list",
                heading="🚨 Signaler un problème",
                subtitle=title,
                default_message=default_message,
                show_sms=True,
            )
        )


class EventReservationAdmin(ModelView, model=EventReservation):
    name = "Réservation événement"
    name_plural = "Réservations événements"
    icon = "fa-solid fa-champagne-glasses"
    column_list = [
        EventReservation.id,
        EventReservation.event_type,
        EventReservation.last_name,
        EventReservation.date,
        EventReservation.guests,
        EventReservation.status,
    ]
    column_default_sort = ("created_at", True)
    can_create = False

    @action(
        name="confirm",
        label="✅ Confirmer (email + SMS)",
        confirmation_message="Confirmer la/les réservation(s) sélectionnée(s) et envoyer un email + SMS de confirmation ?",
    )
    async def confirm_reservation(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                reservation = db.get(EventReservation, int(pk))
                if not reservation:
                    continue
                reservation.status = "confirmée"
                db.commit()
                db.refresh(reservation)

                subject, body, sms_text = event_reservation_confirmed(reservation)
                send_email(reservation.email, subject, body)
                send_sms(reservation.phone, sms_text)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity), status_code=302
        )

    @action(
        name="report-issue",
        label="🚨 Signaler un problème",
        add_in_detail=True,
        add_in_list=True,
    )
    async def report_issue(self, request: Request):
        pks = [p for p in request.query_params.get("pks", "").split(",") if p]
        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity), status_code=302
            )
        db = SessionLocal()
        try:
            reservation = db.get(EventReservation, int(pks[0]))
            if not reservation:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity), status_code=302
                )
            default_message = event_issue_message(reservation)
            title = (
                f"{reservation.event_type} — {reservation.first_name} {reservation.last_name} — "
                f"{reservation.date} {reservation.time} ({reservation.guests} pers.)"
            )
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/reservation-issue/event/{pks[0]}/send",
                cancel_url="/admin/event-reservation/list",
                heading="🚨 Signaler un problème",
                subtitle=title,
                default_message=default_message,
                show_sms=True,
            )
        )


class ContactMessageAdmin(ModelView, model=ContactMessage):
    name = "Message contact"
    name_plural = "Messages contact"
    icon = "fa-solid fa-envelope"
    column_list = [
        ContactMessage.id,
        ContactMessage.name,
        ContactMessage.subject,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.created_at,
    ]
    column_default_sort = ("created_at", True)
    can_create = False

    @action(
        name="acknowledge",
        label="✅ Accusé de réception (email)",
        confirmation_message="Envoyer un email « nous vous répondrons bientôt » au(x) contact(s) sélectionné(s) ?",
    )
    async def acknowledge_message(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                message = db.get(ContactMessage, int(pk))
                if not message:
                    continue
                message.is_read = True
                db.commit()
                db.refresh(message)

                subject, body = contact_acknowledgement(message)
                send_email(message.email, subject, body)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity), status_code=302
        )

    @action(
        name="reply",
        label="✉️ Répondre",
        add_in_detail=True,
        add_in_list=True,
    )
    async def reply_to_message(self, request: Request):
        pks = [p for p in request.query_params.get("pks", "").split(",") if p]
        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity), status_code=302
            )
        db = SessionLocal()
        try:
            message = db.get(ContactMessage, int(pks[0]))
            if not message:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity), status_code=302
                )
            default_message = contact_reply_default_message(message)
            title = f"{message.name} ({message.email})"
            original = message.message
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/contact-reply/{pks[0]}/send",
                cancel_url="/admin/contact-message/list",
                heading="✉️ Répondre au message",
                subtitle=title,
                default_message=default_message,
                show_sms=False,
                quoted=original,
            )
        )


class ReviewAdmin(ModelView, model=Review):
    name = "Avis"
    name_plural = "Avis (site)"
    icon = "fa-solid fa-star"
    column_list = [
        Review.id,
        Review.author_name,
        Review.rating,
        Review.relative_time,
        Review.is_visible,
        Review.position,
    ]
    column_default_sort = ("position", False)
    form_columns = [
        Review.author_name,
        Review.rating,
        Review.text,
        Review.relative_time,
        Review.is_visible,
        Review.position,
    ]


class ReviewsSummaryAdmin(ModelView, model=ReviewsSummary):
    name = "Résumé des avis"
    name_plural = "Résumé des avis"
    icon = "fa-solid fa-chart-simple"
    column_list = [ReviewsSummary.id, ReviewsSummary.rating, ReviewsSummary.total]


def setup_admin(app):
    authentication_backend = AdminAuth(secret_key=os.getenv("SECRET_KEY", "change-me"))
    admin = Admin(
        app,
        engine,
        title="Miss Chawarma — Admin",
        authentication_backend=authentication_backend,
    )
    admin.add_view(CategoryAdmin)
    admin.add_view(DishAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(OrderItemAdmin)
    admin.add_view(TableReservationAdmin)
    admin.add_view(EventReservationAdmin)
    admin.add_view(ContactMessageAdmin)
    admin.add_view(ReviewAdmin)
    admin.add_view(ReviewsSummaryAdmin)

    # SQLAdmin monte son propre sous-programme sur /admin (qui intercepte tout ce préfixe) :
    # notre route personnalisée doit donc vivre EN DEHORS de /admin. On lui donne sa propre
    # SessionMiddleware (même SECRET_KEY) pour pouvoir lire la session de connexion admin.
    from starlette.middleware.sessions import SessionMiddleware

    app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "change-me"))

    @app.post("/reservation-issue/{kind}/{pk}/send")
    async def send_issue(kind: str, pk: int, request: Request):
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        form = await request.form()
        message = (form.get("message") or "").strip()
        send_email_flag = form.get("send_email") == "on"
        send_sms_flag = form.get("send_sms") == "on"

        Model = TableReservation if kind == "table" else EventReservation
        db = SessionLocal()
        try:
            reservation = db.get(Model, pk)
            if reservation and message:
                if send_email_flag:
                    send_email(
                        reservation.email, issue_email_subject(reservation.language), message
                    )
                if send_sms_flag:
                    send_sms(reservation.phone, message)
                reservation.status = "problème signalé"
                db.commit()
        finally:
            db.close()

        identity = "table-reservation" if kind == "table" else "event-reservation"
        return RedirectResponse(f"/admin/{identity}/list", status_code=302)

    @app.post("/contact-reply/{pk}/send")
    async def send_contact_reply(pk: int, request: Request):
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        form = await request.form()
        message_text = (form.get("message") or "").strip()
        send_email_flag = form.get("send_email") == "on"

        db = SessionLocal()
        try:
            contact_message = db.get(ContactMessage, pk)
            if contact_message and message_text:
                if send_email_flag:
                    send_email(
                        contact_message.email,
                        contact_reply_subject(contact_message.language),
                        message_text,
                    )
                contact_message.status = "répondu"
                contact_message.is_read = True
                db.commit()
        finally:
            db.close()

        return RedirectResponse("/admin/contact-message/list", status_code=302)

    return admin
