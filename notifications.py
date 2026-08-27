# notifications.py — Envoi d'emails et de SMS automatiques (confirmation réservation,
# accusé de réception contact), en français ou en anglais selon la langue du site
# au moment de la soumission du formulaire.
#
# Email : API HTTP Brevo (SMTP classique bloqué par Render sur les ports sortants)
# SMS   : Twilio
#
# Variables d'environnement attendues dans .env :
#   SMTP_EMAIL=misschawarma@gmail.com              (adresse expéditrice, vérifiée sur Brevo)
#   BREVO_API_KEY=xkeysib-xxxxxxxxxxxxxxxxxxxxxxxx  (clé API générée dans Brevo -> SMTP et API)
#   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   TWILIO_FROM_NUMBER=+33xxxxxxxxx                (numéro fourni par Twilio)
#   ALI_PHONE_NUMBER=+33xxxxxxxxx                  (numéro d'Ali, notifications internes)
#
# Si une variable manque, la fonction correspondante ne plante pas : elle logue
# un avertissement et ne fait rien. Le statut "confirmée" / "lu" est toujours
# enregistré dans la base, même si l'email ou le SMS échoue.

from __future__ import annotations

import os
import logging
import unicodedata
import requests

logger = logging.getLogger("notifications")

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

ALI_PHONE = os.getenv("ALI_PHONE_NUMBER")
ADMIN_DASHBOARD_URL = os.getenv("ADMIN_DASHBOARD_URL", "https://chatbot-api-o6bw.onrender.com/admin/")


# ─────────────── Envoi bas niveau ───────────────

def send_email(to_email: str, subject: str, body: str, html: bool = False) -> bool:
    """Envoie un email via l'API HTTP Brevo. Retourne True si envoyé, False sinon
    (jamais d'exception) : le SMTP classique (port 587) est bloqué par Render."""
    if not BREVO_API_KEY or not SMTP_EMAIL:
        logger.warning("BREVO_API_KEY / SMTP_EMAIL manquant(s) : email non envoyé à %s", to_email)
        return False
    try:
        payload = {
            "sender": {"email": SMTP_EMAIL, "name": "Miss Chawarma"},
            "to": [{"email": to_email}],
            "subject": subject,
        }
        if html:
            payload["htmlContent"] = body
        else:
            payload["textContent"] = body

        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": BREVO_API_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json=payload,
            timeout=10,
        )
        if not response.ok:
            logger.error(
                "Brevo a refusé l'envoi (status %s) : %s",
                response.status_code, response.text,
            )
            return False
        return True
    except Exception:
        logger.exception("Échec de l'envoi d'email à %s", to_email)
        return False

def _normalize_phone_e164(phone: str, default_country_code: str = "33") -> str:
    """Convertit un numéro français local (07...) en format E.164 (+337...)
    requis par Twilio. Si le numéro est déjà au format international
    (commence par +), il est laissé tel quel."""
    cleaned = "".join(ch for ch in phone.strip() if ch.isdigit() or ch == "+")

    if cleaned.startswith("+"):
        return cleaned

    if cleaned.startswith("0") and len(cleaned) == 10:
        return f"+{default_country_code}{cleaned[1:]}"

    if len(cleaned) == 9:
        return f"+{default_country_code}{cleaned}"

    return cleaned


def send_sms(to_phone: str, body: str) -> bool:
    """Envoie un SMS via Twilio. Retourne True si envoyé, False sinon (jamais d'exception)."""
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_FROM_NUMBER:
        logger.warning("Identifiants Twilio manquants : SMS non envoyé à %s", to_phone)
        return False
    try:
        from twilio.rest import Client  # import local : optionnel si le SMS n'est pas utilisé

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        normalized_phone = _normalize_phone_e164(to_phone)
        message = client.messages.create(
            to=normalized_phone,
            from_=TWILIO_FROM_NUMBER,
            body=body,
        )
        logger.info(
            "SMS Twilio cree : sid=%s status=%s to=%s",
            getattr(message, "sid", "?"),
            getattr(message, "status", "?"),
            normalized_phone,
        )

        return True
    except Exception:
        logger.exception("Échec de l'envoi de SMS à %s", to_phone)
        return False


def _admin_sms_text(body: str, max_length: int = 150) -> str:
    """Rend une notification admin courte et ASCII pour rester sur 1 segment SMS.

    Les emojis / accents peuvent faire passer Twilio en Unicode (UCS-2), ce qui
    réduit fortement la taille d'un segment. Pour les alertes internes, on
    retire donc les accents/emojis et on limite le texte à 150 caractères.
    """
    normalized = unicodedata.normalize("NFKD", body or "")
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    compact = " ".join(ascii_text.split())
    return compact[:max_length]


def send_admin_sms(body: str) -> bool:
    """Envoie une notification SMS uniquement au numéro admin ALI_PHONE_NUMBER."""
    if not ALI_PHONE:
        logger.warning("ALI_PHONE_NUMBER manquant : notification admin non envoyee")
        return False
    return send_sms(ALI_PHONE, _admin_sms_text(body))


# ─────────────── Modèles de messages (FR / EN) ───────────────

def _lang(language: str | None) -> str:
    return "en" if (language or "fr").lower().startswith("en") else "fr"


resolve_lang = _lang  # alias public, utilisé par admin.py


def table_issue_message(reservation) -> str:
    """Texte par défaut (modifiable dans l'admin) pour signaler un problème sur une réservation de table."""
    lang = _lang(reservation.language)
    if lang == "en":
        return (
            f"Hello {reservation.first_name}, we're experiencing an issue with your "
            f"reservation on {reservation.date} at {reservation.time} for {reservation.guests} "
            f"guest(s). Could you please get back to us so we can find a solution together?\n\n"
            f"Thank you,\nThe Miss Chawarma team"
        )
    return (
        f"Bonjour {reservation.first_name}, nous rencontrons un souci concernant votre "
        f"réservation du {reservation.date} à {reservation.time} pour {reservation.guests} "
        f"personne(s). Pourriez-vous nous recontacter afin qu'on trouve une solution ensemble ?\n\n"
        f"Merci,\nL'équipe Miss Chawarma"
    )


def event_issue_message(reservation) -> str:
    """Texte par défaut (modifiable dans l'admin) pour signaler un problème sur une réservation d'événement."""
    lang = _lang(reservation.language)
    if lang == "en":
        return (
            f"Hello {reservation.first_name}, we're experiencing an issue with your event "
            f"\"{reservation.event_type}\" on {reservation.date} at {reservation.time} for "
            f"{reservation.guests} guest(s). Could you please get back to us so we can find a "
            f"solution together?\n\nThank you,\nThe Miss Chawarma team"
        )
    return (
        f"Bonjour {reservation.first_name}, nous rencontrons un souci concernant votre "
        f"événement « {reservation.event_type} » du {reservation.date} à {reservation.time} "
        f"pour {reservation.guests} personne(s). Pourriez-vous nous recontacter afin qu'on "
        f"trouve une solution ensemble ?\n\nMerci,\nL'équipe Miss Chawarma"
    )


def issue_email_subject(language: str | None) -> str:
    return (
        "About your reservation : Miss Chawarma"
        if _lang(language) == "en"
        else "Concernant votre réservation : Miss Chawarma"
    )


def contact_reply_default_message(message) -> str:
    """Texte par défaut (modifiable dans l'admin) pour répondre personnellement à un contact."""
    lang = _lang(message.language)
    if lang == "en":
        return (
            f"Hello {message.name},\n\n"
            f"[Write your reply here]\n\n"
            f"Best regards,\nThe Miss Chawarma team"
        )
    return (
        f"Bonjour {message.name},\n\n"
        f"[Écrivez votre réponse ici]\n\n"
        f"Cordialement,\nL'équipe Miss Chawarma"
    )


def contact_reply_subject(language: str | None) -> str:
    return (
        "Reply to your message : Miss Chawarma"
        if _lang(language) == "en"
        else "Réponse à votre message : Miss Chawarma"
    )


MAPS_URL = "https://www.google.com/maps/place/Miss+Chawarma/@48.8662047,2.3775387,17z"


def table_reservation_confirmed(reservation) -> tuple[str, str, str]:
    """Retourne (sujet_email, corps_email_html, texte_sms) pour une réservation de table confirmée."""
    lang = _lang(reservation.language)
    if lang == "en":
        subject = "Your reservation at Miss Chawarma is confirmed ✅"
        body = (
            f"<p>Hello {reservation.first_name},</p>"
            f"<p>Great news : your reservation is confirmed!</p>"
            f"<p>📅 Date: {reservation.date}<br>"
            f"🕐 Time: {reservation.time}<br>"
            f"👥 Guests: {reservation.guests}</p>"
            f"<p>We can't wait to welcome you at "
            f"<a href=\"{MAPS_URL}\">Miss Chawarma</a>.</p>"
            f"<p>See you soon,<br>The Miss Chawarma team</p>"
        )
        sms = (
            f"Miss Chawarma 🌿 Hi {reservation.first_name}! Your table on {reservation.date} "
            f"at {reservation.time} for {reservation.guests} guest(s) is confirmed ✅ "
            f"We're waiting for you: {MAPS_URL} See you soon!"
        )
    else:
        subject = "Votre réservation chez Miss Chawarma est confirmée ✅"
        body = (
            f"<p>Bonjour {reservation.first_name},</p>"
            f"<p>Votre réservation est confirmée avec plaisir !</p>"
            f"<p>📅 Date : {reservation.date}<br>"
            f"🕐 Heure : {reservation.time}<br>"
            f"👥 Nombre de personnes : {reservation.guests}</p>"
            f"<p>Nous avons hâte de vous accueillir à "
            f"<a href=\"{MAPS_URL}\">Miss Chawarma</a>.</p>"
            f"<p>À très bientôt,<br>L'équipe Miss Chawarma</p>"
        )
        sms = (
            f"Miss Chawarma 🌿 Bonjour {reservation.first_name} ! Votre table du {reservation.date} "
            f"à {reservation.time} pour {reservation.guests} pers. est confirmée ✅ "
            f"On vous attend avec plaisir : {MAPS_URL} À très bientôt !"
        )
    return subject, body, sms


def event_reservation_confirmed(reservation) -> tuple[str, str, str]:
    """Retourne (sujet_email, corps_email, texte_sms) pour une réservation d'événement confirmée."""
    lang = _lang(reservation.language)
    if lang == "en":
        subject = "Your event at Miss Chawarma is confirmed ✅"
        body = (
            f"Hello {reservation.first_name},\n\n"
            f"Great news : your event \"{reservation.event_type}\" is confirmed!\n\n"
            f"📅 Date: {reservation.date}\n"
            f"🕐 Time: {reservation.time}\n"
            f"👥 Guests: {reservation.guests}\n\n"
            f"We can't wait to host you at Miss Chawarma.\n\n"
            f"See you soon,\nThe Miss Chawarma team"
        )
        sms = (
            f"Miss Chawarma 🌿 Hi {reservation.first_name}! Your event on {reservation.date} "
            f"at {reservation.time} for {reservation.guests} guest(s) is confirmed ✅ "
            f"See you at Miss Chawarma!"
        )
    else:
        subject = "Votre événement chez Miss Chawarma est confirmé ✅"
        body = (
            f"Bonjour {reservation.first_name},\n\n"
            f"Votre événement « {reservation.event_type} » est confirmé avec plaisir !\n\n"
            f"📅 Date : {reservation.date}\n"
            f"🕐 Heure : {reservation.time}\n"
            f"👥 Nombre de personnes : {reservation.guests}\n\n"
            f"Nous avons hâte de vous accueillir à Miss Chawarma.\n\n"
            f"À très bientôt,\nL'équipe Miss Chawarma"
        )
        sms = (
            f"Miss Chawarma 🌿 Bonjour {reservation.first_name} ! Votre événement du {reservation.date} "
            f"à {reservation.time} pour {reservation.guests} pers. est confirmé ✅ "
            f"Rendez-vous à Miss Chawarma !"
        )
    return subject, body, sms


def contact_acknowledgement(message) -> tuple[str, str]:
    """Retourne (sujet_email, corps_email) pour l'accusé de réception d'un message de contact."""
    lang = _lang(message.language)
    if lang == "en":
        subject = "We've received your message : Miss Chawarma"
        body = (
            f"Hello {message.name},\n\n"
            f"Thank you for reaching out! We've received your message and we'll "
            f"get back to you very soon.\n\n"
            f"See you soon,\nThe Miss Chawarma team"
        )
    else:
        subject = "Nous avons bien reçu votre message : Miss Chawarma"
        body = (
            f"Bonjour {message.name},\n\n"
            f"Merci de nous avoir contactés ! Nous avons bien reçu votre message "
            f"et nous vous répondrons très rapidement.\n\n"
            f"À très bientôt,\nL'équipe Miss Chawarma"
        )
    return subject, body
