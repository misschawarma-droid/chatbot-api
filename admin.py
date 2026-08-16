# admin.py — Interface d'administration SQLAdmin (/admin)
# Login/mot de passe définis dans .env : ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY

import json
import os
from sqladmin import Admin, ModelView, action
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse, HTMLResponse
from markupsafe import Markup, escape

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
from admin_theme import AdminBrandMiddleware
from admin_dashboard import register_admin_dashboard_routes
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
            and os.getenv("ADMIN_PASSWORD")
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

    column_list = [
        Category.name_fr,
        Category.name_en,
        Category.position,
    ]

    column_labels = {
        Category.name_fr: "Nom en français",
        Category.name_en: "Nom en anglais",
        Category.subtitle_fr: "Sous-titre en français",
        Category.subtitle_en: "Sous-titre en anglais",
        Category.position: "Ordre d’affichage",
    }

    column_searchable_list = [
        Category.name_fr,
        Category.name_en,
        Category.subtitle_fr,
        Category.subtitle_en,
    ]

    column_sortable_list = [
        Category.name_fr,
        Category.name_en,
        Category.position,
    ]

    column_default_sort = ("position", False)

    column_formatters = {
        Category.position: lambda model, attr: (
            f"Position {getattr(model, attr) + 1}"
        ),
    }

    form_columns = [
        Category.name_fr,
        Category.name_en,
        Category.subtitle_fr,
        Category.subtitle_en,
        Category.position,
    ]


class DishAdmin(ModelView, model=Dish):
    name = "Plat"
    name_plural = "Plats"
    icon = "fa-solid fa-utensils"

    column_list = [
        Dish.name_fr,
        Dish.category,
        Dish.price,
        Dish.is_available,
    ]

    column_labels = {
        Dish.name_fr: "Plat",
        Dish.category: "Catégorie",
        Dish.price: "Prix",
        Dish.is_available: "Disponibilité",
    }

    column_searchable_list = [
        Dish.name_fr,
    ]

    column_sortable_list = [
        Dish.name_fr,
        Dish.price,
        Dish.position,
        Dish.is_available,
    ]

    column_default_sort = ("position", False)

    column_formatters = {
        Dish.price: lambda model, attr: f"{getattr(model, attr):.2f} €".replace(".", ","),
        Dish.is_available: lambda model, attr: (
            "🟢 Disponible" if getattr(model, attr) else "🔴 Indisponible"
        ),
        Dish.category: lambda model, attr: (
            getattr(getattr(model, attr), "name_fr", "Sans catégorie")
        ),
    }

    form_columns = [
        Dish.name_fr,
        Dish.price,
        Dish.is_available,
        Dish.category,
        Dish.position,
    ]


class OrderAdmin(ModelView, model=Order):
    name = "Commande"
    name_plural = "Commandes"
    icon = "fa-solid fa-basket-shopping"

    column_list = [
        Order.id,
        Order.customer_name,
        Order.order_type,
        Order.address_street,
        Order.total,
        Order.payment_status,
        Order.status,
        Order.requested_date,
    ]

    column_labels = {
        Order.id: "N°",
        Order.customer_name: "Client",
        Order.order_type: "Réception",
        Order.address_street: "Destination",
        Order.total: "Total",
        Order.payment_status: "Paiement",
        Order.status: "État",
        Order.requested_date: "Créneau",
    }

    column_searchable_list = [
        Order.customer_name,
        Order.customer_phone,
        Order.customer_email,
        Order.address_street,
        Order.city,
        Order.postal_code,
    ]
    column_sortable_list = [
        Order.id,
        Order.total,
        Order.status,
        Order.requested_date,
        Order.created_at,
    ]
    column_default_sort = ("created_at", True)
    page_size = 20
    page_size_options = [10, 20, 50, 100]

    column_details_list = [
        Order.id,
        Order.customer_name,
        Order.customer_phone,
        Order.customer_email,
        Order.order_type,
        Order.requested_date,
        Order.requested_time,
        Order.address_street,
        Order.address_extra,
        Order.postal_code,
        Order.city,
        Order.subtotal,
        Order.delivery_fee,
        Order.total,
        Order.payment_method,
        Order.payment_status,
        Order.status,
        Order.note,
        Order.created_at,
    ]

    @staticmethod
    def _customer_formatter(model, attribute, request):
        name = escape(model.customer_name or "Client")
        phone = escape(model.customer_phone or "—")
        return Markup(
            f'<div style="min-width:170px">'
            f'<strong style="color:#163f21">{name}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">☎ {phone}</span>'
            f'</div>'
        )

    @staticmethod
    def _order_type_formatter(model, attribute, request):
        is_delivery = model.order_type == "livraison"
        label = "Livraison" if is_delivery else "À emporter"
        icon = "🚚" if is_delivery else "🏪"
        background = "#e8f4ea" if is_delivery else "#fff5df"
        color = "#1f6b2d" if is_delivery else "#9a6500"
        return Markup(
            f'<span style="display:inline-flex;align-items:center;gap:6px;'
            f'padding:6px 10px;border-radius:999px;background:{background};'
            f'color:{color};font-weight:700;font-size:12px;white-space:nowrap">'
            f'{icon} {label}</span>'
        )

    @staticmethod
    def _address_formatter(model, attribute, request):
        if model.order_type != "livraison":
            return Markup('<span style="color:#9aa0aa">Retrait au restaurant</span>')

        street = escape(model.address_street or "Adresse non renseignée")
        city_line = " ".join(
            part for part in [model.postal_code or "", model.city or ""] if part
        )
        city_line = escape(city_line or "—")
        return Markup(
            f'<div style="max-width:230px">'
            f'<strong style="color:#2d3748">📍 {street}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">{city_line}</span>'
            f'</div>'
        )

    @staticmethod
    def _money_formatter(model, attribute, request):
        value = float(model.total or 0)
        amount = f"{value:,.2f}".replace(",", " ").replace(".", ",")
        return Markup(
            f'<strong style="color:#c47d0e;font-size:15px;white-space:nowrap">'
            f'{amount} €</strong>'
        )

    @staticmethod
    def _payment_formatter(model, attribute, request):
        status = (model.payment_status or "en_attente").lower()
        method = "Carte" if model.payment_method == "carte" else "Sur place"
        styles = {
            "paye": ("Payé", "#e8f4ea", "#1f6b2d"),
            "payé": ("Payé", "#e8f4ea", "#1f6b2d"),
            "en_attente": ("En attente", "#fff5df", "#9a6500"),
            "echoue": ("Échoué", "#fdeaea", "#b42318"),
            "échoué": ("Échoué", "#fdeaea", "#b42318"),
        }
        label, background, color = styles.get(
            status, (status.replace("_", " ").title(), "#eef1f5", "#566070")
        )
        return Markup(
            f'<div style="min-width:110px">'
            f'<span style="display:inline-block;padding:5px 9px;border-radius:999px;'
            f'background:{background};color:{color};font-weight:700;font-size:12px">'
            f'{escape(label)}</span><br>'
            f'<span style="color:#7a8190;font-size:11px">{escape(method)}</span>'
            f'</div>'
        )

    @staticmethod
    def _status_formatter(model, attribute, request):
        value = (model.status or "nouvelle").lower()
        styles = {
            "nouvelle": ("Nouvelle", "#eaf2ff", "#2457a6"),
            "confirmée": ("Confirmée", "#e8f4ea", "#1f6b2d"),
            "confirmee": ("Confirmée", "#e8f4ea", "#1f6b2d"),
            "en préparation": ("En préparation", "#fff5df", "#9a6500"),
            "en_preparation": ("En préparation", "#fff5df", "#9a6500"),
            "prête": ("Prête", "#eee9ff", "#6941c6"),
            "prete": ("Prête", "#eee9ff", "#6941c6"),
            "livrée": ("Livrée", "#e8f4ea", "#1f6b2d"),
            "livree": ("Livrée", "#e8f4ea", "#1f6b2d"),
            "annulée": ("Annulée", "#fdeaea", "#b42318"),
            "annulee": ("Annulée", "#fdeaea", "#b42318"),
        }
        label, background, color = styles.get(
            value, (value.replace("_", " ").title(), "#eef1f5", "#566070")
        )
        return Markup(
            f'<span style="display:inline-block;padding:6px 10px;border-radius:999px;'
            f'background:{background};color:{color};font-weight:700;font-size:12px;'
            f'white-space:nowrap">{escape(label)}</span>'
        )

    @staticmethod
    def _slot_formatter(model, attribute, request):
        date = escape(model.requested_date or "Dès que possible")
        time = escape(model.requested_time or "")
        time_html = f'<br><strong style="color:#1f6b2d">{time}</strong>' if time else ""
        return Markup(
            f'<span style="white-space:nowrap;color:#606775;font-size:12px">'
            f'📅 {date}{time_html}</span>'
        )

    @staticmethod
    def _id_ticket_formatter(model, attribute, request):
        return Markup(
            f'<a href="/order-ticket/{model.id}" target="_blank" '
            f'class="ticket-trigger" data-order-id="{model.id}" '
            f'style="display:inline-flex;align-items:center;justify-content:center;'
            f'min-width:60px;padding:6px 12px;border-radius:999px;background:#1f6b2d;'
            f'color:#ffffff !important;font-weight:700;font-size:13px;'
            f'text-decoration:none;white-space:nowrap">'
            f'Ticket #{model.id}</a>'
        )

    column_formatters = {
        Order.id: _id_ticket_formatter,
        Order.customer_name: _customer_formatter,
        Order.order_type: _order_type_formatter,
        Order.address_street: _address_formatter,
        Order.total: _money_formatter,
        Order.payment_status: _payment_formatter,
        Order.status: _status_formatter,
        Order.requested_date: _slot_formatter,
    }

    can_create = False


class OrderItemAdmin(ModelView, model=OrderItem):
    name = "Article commandé"
    name_plural = "Articles commandés"
    icon = "fa-solid fa-receipt"

    column_list = [
        OrderItem.order_id,
        OrderItem.dish_name,
        OrderItem.quantity,
        OrderItem.unit_price,
        OrderItem.removed_ingredients,
        OrderItem.selected_choices,
    ]

    column_labels = {
        OrderItem.order_id: "Commande",
        OrderItem.dish_name: "Plat",
        OrderItem.quantity: "Quantité",
        OrderItem.unit_price: "Prix unitaire",
        OrderItem.removed_ingredients: "Sans",
        OrderItem.selected_choices: "Personnalisation",
    }

    @staticmethod
    def _selected_choices_formatter(model, attribute, request):
        raw = getattr(model, attribute)
        if not raw:
            return Markup('<span style="color:#9aa0aa">—</span>')
        try:
            data = json.loads(raw)
        except (TypeError, ValueError):
            return Markup('<span style="color:#9aa0aa">—</span>')
        if not data:
            return Markup('<span style="color:#9aa0aa">—</span>')

        all_ids = set()
        for sel in data.values():
            all_ids.update(sel.get("dish_ids") or [])

        db = SessionLocal()
        try:
            names = {}
            if all_ids:
                rows = db.query(Dish.id, Dish.name_fr).filter(Dish.id.in_(all_ids)).all()
                names = {row[0]: row[1] for row in rows}
        finally:
            db.close()

        lines = []
        for label, sel in data.items():
            dish_ids = sel.get("dish_ids") or []
            options = sel.get("options") or []
            sub_removed = sel.get("sub_removed") or []
            sub_choices = sel.get("sub_choices") or {}
            if dish_ids:
                counts = {}
                for did in dish_ids:
                    counts[did] = counts.get(did, 0) + 1
                parts = []
                for did, count in counts.items():
                    dish_name = names.get(did, f"#{did}")
                    parts.append(f"{dish_name} ×{count}" if count > 1 else dish_name)
                value = ", ".join(parts)
            elif options:
                value = ", ".join(options)
            else:
                value = "—"
            line = f'<strong style="color:#163f21">{escape(label)}</strong>: {escape(value)}'
            if sub_removed or sub_choices:
                extras = []
                if sub_removed:
                    extras.append(f"sans {', '.join(sub_removed)}")
                for sub_label, sub_vals in sub_choices.items():
                    if sub_vals:
                        extras.append(f"{sub_label}: {', '.join(sub_vals)}")
                if extras:
                    line += f'<br><span style="color:#7a8190;font-size:11px;margin-left:8px">↳ {escape(" · ".join(extras))}</span>'
            lines.append(line)

        return Markup(
            '<div style="font-size:12px;line-height:1.6;max-width:260px">'
            + "<br>".join(lines)
            + "</div>"
        )

    column_formatters = {
        OrderItem.order_id: lambda model, attr: (
            f"Commande #{getattr(model, attr)}"
        ),
        OrderItem.quantity: lambda model, attr: (
            f"× {getattr(model, attr)}"
        ),
        OrderItem.unit_price: lambda model, attr: (
            f"{getattr(model, attr):.2f} €".replace(".", ",")
        ),
        OrderItem.removed_ingredients: lambda model, attr: (
            ", ".join(json.loads(getattr(model, attr) or "[]")) or "—"
        ),
        OrderItem.selected_choices: _selected_choices_formatter,
    }

    column_searchable_list = [
        OrderItem.dish_name,
    ]

    column_sortable_list = [
        OrderItem.order_id,
        OrderItem.dish_name,
        OrderItem.quantity,
        OrderItem.unit_price,
    ]

    column_default_sort = ("order_id", True)

    can_create = False
    can_edit = False


class TableReservationAdmin(ModelView, model=TableReservation):
    name = "Réservation table"
    name_plural = "Réservations tables"
    icon = "fa-solid fa-chair"

    column_list = [
        TableReservation.last_name,
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
    ]

    column_labels = {
        TableReservation.last_name: "Client",
        TableReservation.date: "Date",
        TableReservation.time: "Heure",
        TableReservation.guests: "Convives",
        TableReservation.status: "Statut",
    }

    column_formatters = {
        TableReservation.last_name: lambda model, attr: (
            f"👤 {getattr(model, attr).title()}"
        ),
        TableReservation.date: lambda model, attr: (
            getattr(model, attr).strftime("%d/%m/%Y")
            if hasattr(getattr(model, attr), "strftime")
            else str(getattr(model, attr))
        ),
        TableReservation.time: lambda model, attr: (
            f"🕒 {getattr(model, attr)}"
        ),
        TableReservation.guests: lambda model, attr: (
            f"👥 {getattr(model, attr)} personne"
            if getattr(model, attr) == 1
            else f"👥 {getattr(model, attr)} personnes"
        ),
        TableReservation.status: lambda model, attr: {
            "nouvelle": "🟡 Nouvelle",
            "confirmée": "🟢 Confirmée",
            "problème signalé": "🔴 Problème signalé",
            "annulée": "⚫ Annulée",
        }.get(
            str(getattr(model, attr)).lower(),
            str(getattr(model, attr)).capitalize(),
        ),
    }

    column_searchable_list = [
        TableReservation.last_name,
        TableReservation.phone,
        TableReservation.email,
    ]

    column_sortable_list = [
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
        TableReservation.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        TableReservation.id,
        TableReservation.first_name,
        TableReservation.last_name,
        TableReservation.phone,
        TableReservation.email,
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
        TableReservation.table_ids,
        TableReservation.note,
        TableReservation.created_at,
    ]

    can_create = False

    @action(
        name="confirm",
        label="✅ Confirmer (email + SMS)",
        confirmation_message=(
            "Confirmer la/les réservation(s) sélectionnée(s) "
            "et envoyer un email + SMS de confirmation ?"
        ),
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
            request.url_for("admin:list", identity=self.identity),
            status_code=302,
        )

    @action(
        name="report-issue",
        label="🚨 Signaler un problème",
        add_in_detail=True,
        add_in_list=True,
    )
    async def report_issue(self, request: Request):
        pks = [pk for pk in request.query_params.get("pks", "").split(",") if pk]

        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity),
                status_code=302,
            )

        db = SessionLocal()
        try:
            reservation = db.get(TableReservation, int(pks[0]))

            if not reservation:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity),
                    status_code=302,
                )

            default_message = table_issue_message(reservation)

            title = (
                f"{reservation.first_name} "
                f"{reservation.last_name} — "
                f"{reservation.date} "
                f"{reservation.time} "
                f"({reservation.guests} pers.)"
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
        EventReservation.event_type,
        EventReservation.last_name,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
    ]

    column_labels = {
        EventReservation.event_type: "Événement",
        EventReservation.last_name: "Client",
        EventReservation.date: "Date",
        EventReservation.time: "Heure",
        EventReservation.guests: "Convives",
        EventReservation.status: "Statut",
    }

    column_formatters = {
        EventReservation.event_type: lambda model, attr: {
            "anniversaire": "🎂 Anniversaire",
            "mariage": "💍 Mariage",
            "entreprise": "💼 Entreprise",
            "privé": "✨ Événement privé",
            "prive": "✨ Événement privé",
        }.get(
            str(getattr(model, attr) or "").lower(),
            f"✨ {str(getattr(model, attr) or 'Événement').title()}",
        ),

        EventReservation.last_name: lambda model, attr: (
            f"👤 {str(getattr(model, attr) or 'Client').title()}"
        ),

        EventReservation.date: lambda model, attr: (
            getattr(model, attr).strftime("%d/%m/%Y")
            if hasattr(getattr(model, attr), "strftime")
            else str(getattr(model, attr) or "—")
        ),

        EventReservation.time: lambda model, attr: (
            f"🕒 {getattr(model, attr) or '—'}"
        ),

        EventReservation.guests: lambda model, attr: (
            f"👥 {getattr(model, attr)} personne"
            if getattr(model, attr) == 1
            else f"👥 {getattr(model, attr)} personnes"
        ),

        EventReservation.status: lambda model, attr: {
            "nouvelle": "🟡 Nouvelle",
            "confirmée": "🟢 Confirmée",
            "confirmee": "🟢 Confirmée",
            "en attente": "🟠 En attente",
            "en_attente": "🟠 En attente",
            "problème signalé": "🔴 Problème signalé",
            "probleme signale": "🔴 Problème signalé",
            "annulée": "⚫ Annulée",
            "annulee": "⚫ Annulée",
        }.get(
            str(getattr(model, attr) or "").lower(),
            str(getattr(model, attr) or "Inconnu").capitalize(),
        ),
    }

    column_searchable_list = [
        EventReservation.event_type,
        EventReservation.last_name,
        EventReservation.phone,
        EventReservation.email,
    ]

    column_sortable_list = [
        EventReservation.event_type,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
        EventReservation.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        EventReservation.id,
        EventReservation.event_type,
        EventReservation.first_name,
        EventReservation.last_name,
        EventReservation.phone,
        EventReservation.email,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
        EventReservation.note,
        EventReservation.created_at,
    ]

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
        ContactMessage.name,
        ContactMessage.subject,
        ContactMessage.message,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.created_at,
    ]

    column_labels = {
        ContactMessage.name: "Contact",
        ContactMessage.subject: "Sujet",
        ContactMessage.message: "Message",
        ContactMessage.status: "Statut",
        ContactMessage.is_read: "Lecture",
        ContactMessage.created_at: "Reçu le",
    }

    column_searchable_list = [
        ContactMessage.name,
        ContactMessage.email,
        ContactMessage.subject,
        ContactMessage.message,
    ]

    column_sortable_list = [
        ContactMessage.name,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        ContactMessage.id,
        ContactMessage.name,
        ContactMessage.email,
        ContactMessage.phone,
        ContactMessage.subject,
        ContactMessage.message,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.language,
        ContactMessage.created_at,
    ]

    @staticmethod
    def _contact_formatter(model, attribute, request):
        name = escape(model.name or "Contact")
        email = escape(model.email or "—")

        return Markup(
            f'<div style="min-width:170px">'
            f'<strong style="color:#163f21">👤 {name}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">{email}</span>'
            f'</div>'
        )

    @staticmethod
    def _subject_formatter(model, attribute, request):
        subject = escape(model.subject or "Sans objet")
        return Markup(f'<strong style="color:#2d3748">{subject}</strong>')

    @staticmethod
    def _message_formatter(model, attribute, request):
        message = str(model.message or "").strip()

        if not message:
            return Markup('<span style="color:#9aa0aa">Aucun message</span>')

        preview = message[:90]
        if len(message) > 90:
            preview += "…"

        return Markup(
            f'<div style="max-width:320px;color:#667085;'
            f'font-size:13px;line-height:1.45">'
            f'{escape(preview)}'
            f'</div>'
        )

    @staticmethod
    def _status_formatter(model, attribute, request):
        status = str(model.status or "nouveau").lower()

        styles = {
            "nouveau": ("Nouveau", "#eaf2ff", "#2457a6"),
            "lu": ("Lu", "#fff5df", "#9a6500"),
            "répondu": ("Répondu", "#e8f4ea", "#1f6b2d"),
            "repondu": ("Répondu", "#e8f4ea", "#1f6b2d"),
            "archivé": ("Archivé", "#eef1f5", "#566070"),
            "archive": ("Archivé", "#eef1f5", "#566070"),
        }

        label, background, color = styles.get(
            status,
            (status.replace("_", " ").title(), "#eef1f5", "#566070"),
        )

        return Markup(
            f'<span style="display:inline-block;padding:6px 10px;'
            f'border-radius:999px;background:{background};'
            f'color:{color};font-weight:700;font-size:12px;'
            f'white-space:nowrap">{escape(label)}</span>'
        )

    @staticmethod
    def _read_formatter(model, attribute, request):
        if model.is_read:
            return Markup('<span style="color:#1f6b2d;font-weight:700">✓ Lu</span>')

        return Markup('<span style="color:#c47d0e;font-weight:700">● Non lu</span>')

    @staticmethod
    def _date_formatter(model, attribute, request):
        value = model.created_at

        if not value:
            return "—"

        if hasattr(value, "strftime"):
            return value.strftime("%d/%m/%Y à %H:%M")

        return str(value)

    column_formatters = {
        ContactMessage.name: _contact_formatter,
        ContactMessage.subject: _subject_formatter,
        ContactMessage.message: _message_formatter,
        ContactMessage.status: _status_formatter,
        ContactMessage.is_read: _read_formatter,
        ContactMessage.created_at: _date_formatter,
    }

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


def setup_admin(app):
    authentication_backend = AdminAuth(secret_key=os.getenv("SECRET_KEY", "change-me"))
    admin = Admin(
        app,
        engine,
        title="Miss Chawarma - Admin",
        authentication_backend=authentication_backend,
    )
    admin.add_view(CategoryAdmin)
    admin.add_view(DishAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(OrderItemAdmin)
    admin.add_view(TableReservationAdmin)
    admin.add_view(EventReservationAdmin)
    admin.add_view(ContactMessageAdmin)
    register_admin_dashboard_routes(app)

    from starlette.middleware.sessions import SessionMiddleware

    app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "change-me"))
    app.add_middleware(AdminBrandMiddleware)

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

    @app.get("/order-ticket/{order_id}")
    async def order_ticket(order_id: int, request: Request):
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        db = SessionLocal()
        try:
            order = db.get(Order, order_id)
            if not order:
                return HTMLResponse("<h1>Commande introuvable</h1>", status_code=404)

            items = db.query(OrderItem).filter(OrderItem.order_id == order_id).all()

            all_dish_ids = set()
            for item in items:
                if item.selected_choices:
                    try:
                        data = json.loads(item.selected_choices)
                        for sel in data.values():
                            all_dish_ids.update(sel.get("dish_ids") or [])
                    except (TypeError, ValueError):
                        pass

            dish_names = {}
            if all_dish_ids:
                rows = db.query(Dish.id, Dish.name_fr).filter(Dish.id.in_(all_dish_ids)).all()
                dish_names = {row[0]: row[1] for row in rows}

            def format_choices(raw):
                if not raw:
                    return ""
                try:
                    data = json.loads(raw)
                except (TypeError, ValueError):
                    return ""
                lines = []
                for label, sel in data.items():
                    dish_ids = sel.get("dish_ids") or []
                    options = sel.get("options") or []
                    if dish_ids:
                        counts = {}
                        for did in dish_ids:
                            counts[did] = counts.get(did, 0) + 1
                        parts = []
                        for did, count in counts.items():
                            name = dish_names.get(did, f"#{did}")
                            parts.append(f"{name} x{count}" if count > 1 else name)
                        value = ", ".join(parts)
                    elif options:
                        value = ", ".join(options)
                    else:
                        value = ""
                    if value:
                        lines.append(f"<strong>{escape(label)}:</strong> {escape(value)}")
                    sub_removed = sel.get("sub_removed") or []
                    sub_choices = sel.get("sub_choices") or {}
                    extras = []
                    if sub_removed:
                        extras.append(f"sans {', '.join(sub_removed)}")
                    for sub_label, sub_vals in sub_choices.items():
                        if sub_vals:
                            extras.append(f"{sub_label}: {', '.join(sub_vals)}")
                    if extras:
                        lines.append(f'<span class="sub">↳ {escape(" · ".join(extras))}</span>')
                return "<br>".join(lines)

            items_html = ""
            for item in items:
                removed = ", ".join(json.loads(item.removed_ingredients or "[]"))
                choices_html = format_choices(item.selected_choices)
                items_html += f"""
                <div class="item">
                  <div class="item-head">
                    <span class="qty">×{item.quantity}</span>
                    <span class="name">{escape(item.dish_name)}</span>
                    <span class="price">{item.unit_price:.2f} €</span>
                  </div>
                  {f'<div class="removed">Sans : {escape(removed)}</div>' if removed else ''}
                  {f'<div class="choices">{choices_html}</div>' if choices_html else ''}
                </div>"""

            html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Commande #{order.id}</title>
<style>
  body {{ font-family: -apple-system, Arial, sans-serif; background: #f7f0e4; margin: 0; padding: 24px; color: #222; }}
  .ticket {{ max-width: 420px; margin: 0 auto; background: white; border-radius: 12px;
             padding: 24px; box-shadow: 0 2px 14px rgba(0,0,0,0.10); }}
  h1 {{ font-size: 20px; margin: 0 0 4px; color: #1f6b2d; }}
  .meta {{ font-size: 13px; color: #666; margin-bottom: 16px; }}
  .meta strong {{ color: #333; }}
  .badge {{ display: inline-block; padding: 4px 10px; border-radius: 999px; font-size: 12px;
            font-weight: 700; background: #fff5df; color: #9a6500; margin-bottom: 12px; }}
  .item {{ padding: 12px 0; border-bottom: 1px dashed #ddd; }}
  .item:last-child {{ border-bottom: none; }}
  .item-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 8px; font-size: 15px; font-weight: 700; }}
  .qty {{ color: #1f6b2d; }}
  .name {{ flex: 1; }}
  .price {{ color: #c47d0e; }}
  .removed {{ font-size: 12px; color: #b42318; margin-top: 4px; }}
  .choices {{ font-size: 12px; color: #444; margin-top: 4px; line-height: 1.5; }}
  .choices .sub {{ color: #7a8190; margin-left: 8px; }}
  .total-row {{ display: flex; justify-content: space-between; margin-top: 16px; padding-top: 12px;
                border-top: 2px solid #1f6b2d; font-size: 18px; font-weight: 800; color: #1f6b2d; }}
  .note {{ margin-top: 12px; padding: 10px; background: #fff5df; border-radius: 8px; font-size: 13px; }}
  .print-btn {{ display: block; width: 100%; margin-top: 20px; padding: 12px; border: none;
                border-radius: 8px; background: #1f6b2d; color: white; font-size: 14px;
                font-weight: 700; cursor: pointer; }}
  @media print {{
    body {{ background: white; padding: 0; }}
    .ticket {{ box-shadow: none; max-width: 100%; }}
    .print-btn {{ display: none; }}
  }}
</style>
</head>
<body>
  <div class="ticket">
    <span class="badge">Commande #{order.id}</span>
    <h1>{escape(order.customer_name)}</h1>
    <div class="meta">
      ☎ {escape(order.customer_phone)}<br>
      <strong>{'Livraison' if order.order_type == 'livraison' else 'À emporter'}</strong>
      {f' · {escape(order.address_street)}, {escape(order.city)}' if order.order_type == 'livraison' else ''}<br>
      📅 {escape(order.requested_date or '')} {escape(order.requested_time or '')}
    </div>

    {items_html}

    <div class="total-row">
      <span>Total</span>
      <span>{order.total:.2f} €</span>
    </div>

    {f'<div class="note">📝 {escape(order.note)}</div>' if order.note else ''}

    <button class="print-btn" onclick="window.print()">🖨️ Imprimer le ticket</button>
  </div>
</body>
</html>
"""
            return HTMLResponse(html)
        finally:
            db.close()

    return admin