# notifications.py — Envoi d'emails et de SMS automatiques (confirmation réservation,
# accusé de réception contact), en français ou en anglais selon la langue du site
# au moment de la soumission du formulaire.
#
# Email : Gmail SMTP (mot de passe d'application, PAS ton mot de passe Gmail normal)
# SMS   : Twilio (compte d'essai gratuit)
#
# Variables d'environnement attendues dans .env :
#   SMTP_EMAIL=misschawarma@gmail.com
#   SMTP_APP_PASSWORD=xxxx xxxx xxxx xxxx        (16 caractères, généré sur myaccount.google.com)
#   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   TWILIO_FROM_NUMBER=+1xxxxxxxxxx               (numéro fourni par Twilio)
#
# Si une variable manque, la fonction correspondante ne plante pas : elle logue
# un avertissement et ne fait rien. Le statut "confirmée" / "lu" est toujours
# enregistré dans la base, même si l'email ou le SMS échoue.

from __future__ import annotations

import os
import logging
import smtplib
from email.mime.text import MIMEText

logger = logging.getLogger("notifications")

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_APP_PASSWORD = os.getenv("SMTP_APP_PASSWORD")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")


# ─────────────── Envoi bas niveau ───────────────

def send_email(to_email: str, subject: str, body: str) -> bool:
    """Envoie un email via Gmail SMTP. Retourne True si envoyé, False sinon (jamais d'exception)."""
    if not SMTP_EMAIL or not SMTP_APP_PASSWORD:
        logger.warning("SMTP_EMAIL / SMTP_APP_PASSWORD manquant(s) — email non envoyé à %s", to_email)
        return False
    try:
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_APP_PASSWORD)
            server.sendmail(SMTP_EMAIL, [to_email], msg.as_string())
        return True
    except Exception:
        logger.exception("Échec de l'envoi d'email à %s", to_email)
        return False


def send_sms(to_phone: str, body: str) -> bool:
    """Envoie un SMS via Twilio. Retourne True si envoyé, False sinon (jamais d'exception)."""
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_FROM_NUMBER:
        logger.warning("Identifiants Twilio manquants — SMS non envoyé à %s", to_phone)
        return False
    try:
        from twilio.rest import Client  # import local : optionnel si le SMS n'est pas utilisé

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(to=to_phone, from_=TWILIO_FROM_NUMBER, body=body)
        return True
    except Exception:
        logger.exception("Échec de l'envoi de SMS à %s", to_phone)
        return False


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
        "About your reservation — Miss Chawarma"
        if _lang(language) == "en"
        else "Concernant votre réservation — Miss Chawarma"
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
        "Reply to your message — Miss Chawarma"
        if _lang(language) == "en"
        else "Réponse à votre message — Miss Chawarma"
    )


def table_reservation_confirmed(reservation) -> tuple[str, str, str]:
    """Retourne (sujet_email, corps_email, texte_sms) pour une réservation de table confirmée."""
    lang = _lang(reservation.language)
    if lang == "en":
        subject = "Your reservation at Miss Chawarma is confirmed ✅"
        body = (
            f"Hello {reservation.first_name},\n\n"
            f"Great news — your reservation is confirmed!\n\n"
            f"📅 Date: {reservation.date}\n"
            f"🕐 Time: {reservation.time}\n"
            f"👥 Guests: {reservation.guests}\n\n"
            f"We can't wait to welcome you at 128 Rue Oberkampf, Paris 11e.\n\n"
            f"See you soon,\nThe Miss Chawarma team"
        )
        sms = (
            f"Miss Chawarma: your reservation on {reservation.date} at {reservation.time} "
            f"for {reservation.guests} guest(s) is confirmed ✅ See you soon!"
        )
    else:
        subject = "Votre réservation chez Miss Chawarma est confirmée ✅"
        body = (
            f"Bonjour {reservation.first_name},\n\n"
            f"Votre réservation est confirmée avec plaisir !\n\n"
            f"📅 Date : {reservation.date}\n"
            f"🕐 Heure : {reservation.time}\n"
            f"👥 Nombre de personnes : {reservation.guests}\n\n"
            f"Nous avons hâte de vous accueillir au 128 Rue Oberkampf, Paris 11e.\n\n"
            f"À très bientôt,\nL'équipe Miss Chawarma"
        )
        sms = (
            f"Miss Chawarma : votre réservation du {reservation.date} à {reservation.time} "
            f"pour {reservation.guests} pers. est confirmée ✅ À bientôt !"
        )
    return subject, body, sms


def event_reservation_confirmed(reservation) -> tuple[str, str, str]:
    """Retourne (sujet_email, corps_email, texte_sms) pour une réservation d'événement confirmée."""
    lang = _lang(reservation.language)
    if lang == "en":
        subject = f"Your event at Miss Chawarma is confirmed ✅"
        body = (
            f"Hello {reservation.first_name},\n\n"
            f"Great news — your event \"{reservation.event_type}\" is confirmed!\n\n"
            f"📅 Date: {reservation.date}\n"
            f"🕐 Time: {reservation.time}\n"
            f"👥 Guests: {reservation.guests}\n\n"
            f"We can't wait to host you at 128 Rue Oberkampf, Paris 11e.\n\n"
            f"See you soon,\nThe Miss Chawarma team"
        )
        sms = (
            f"Miss Chawarma: your event on {reservation.date} at {reservation.time} "
            f"for {reservation.guests} guest(s) is confirmed ✅"
        )
    else:
        subject = "Votre événement chez Miss Chawarma est confirmé ✅"
        body = (
            f"Bonjour {reservation.first_name},\n\n"
            f"Votre événement « {reservation.event_type} » est confirmé avec plaisir !\n\n"
            f"📅 Date : {reservation.date}\n"
            f"🕐 Heure : {reservation.time}\n"
            f"👥 Nombre de personnes : {reservation.guests}\n\n"
            f"Nous avons hâte de vous accueillir au 128 Rue Oberkampf, Paris 11e.\n\n"
            f"À très bientôt,\nL'équipe Miss Chawarma"
        )
        sms = (
            f"Miss Chawarma : votre événement du {reservation.date} à {reservation.time} "
            f"pour {reservation.guests} pers. est confirmé ✅"
        )
    return subject, body, sms


def contact_acknowledgement(message) -> tuple[str, str]:
    """Retourne (sujet_email, corps_email) pour l'accusé de réception d'un message de contact."""
    lang = _lang(message.language)
    if lang == "en":
        subject = "We've received your message — Miss Chawarma"
        body = (
            f"Hello {message.name},\n\n"
            f"Thank you for reaching out! We've received your message and we'll "
            f"get back to you very soon.\n\n"
            f"See you soon,\nThe Miss Chawarma team"
        )
    else:
        subject = "Nous avons bien reçu votre message — Miss Chawarma"
        body = (
            f"Bonjour {message.name},\n\n"
            f"Merci de nous avoir contactés ! Nous avons bien reçu votre message "
            f"et nous vous répondrons très rapidement.\n\n"
            f"À très bientôt,\nL'équipe Miss Chawarma"
        )
    return subject, body
