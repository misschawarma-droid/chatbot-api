# routers/stripe_webhook.py — Reçoit les événements Stripe (paiement réussi/échoué)
# et met à jour le statut de paiement de la commande correspondante.
#
# Variables d'environnement attendues :
#   STRIPE_SECRET_KEY=sk_test_... ou sk_live_...
#   STRIPE_WEBHOOK_SECRET=whsec_...  (généré par Stripe pour cet endpoint précis)

import os
import logging

from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Order

router = APIRouter(prefix="/api/stripe", tags=["stripe"])
logger = logging.getLogger("stripe_webhook")

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")


@router.post("/webhook")
async def stripe_webhook(request: Request):
    if not STRIPE_SECRET_KEY or not STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=503, detail="Stripe non configuré")

    import stripe

    stripe.api_key = STRIPE_SECRET_KEY
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except (ValueError, stripe.error.SignatureVerificationError):
        logger.warning("Signature Stripe invalide sur le webhook")
        raise HTTPException(status_code=400, detail="Signature invalide")

    db: Session = SessionLocal()
    try:
        if event["type"] == "payment_intent.succeeded":
            intent = event["data"]["object"]
            order = (
                db.query(Order)
                .filter(Order.stripe_payment_intent_id == intent["id"])
                .first()
            )
            if order:
                order.payment_status = "payé"
                order.status = "confirmée"
                db.commit()

        elif event["type"] == "payment_intent.payment_failed":
            intent = event["data"]["object"]
            order = (
                db.query(Order)
                .filter(Order.stripe_payment_intent_id == intent["id"])
                .first()
            )
            if order:
                order.payment_status = "échoué"
                db.commit()
    finally:
        db.close()

    return {"received": True}
