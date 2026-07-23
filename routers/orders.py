# routers/orders.py — Commandes (click & collect + livraison), avec paiement Stripe optionnel.

import os
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Dish, Order, OrderItem
from schemas import (
    OrderIn,
    OrderOut,
    DeliveryCheckIn,
    DeliveryCheckOut,
    PaymentIntentOut,
)
from delivery import calculate_delivery

router = APIRouter(prefix="/api/orders", tags=["orders"])
logger = logging.getLogger("orders")

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")


@router.post("/delivery-check", response_model=DeliveryCheckOut)
def delivery_check(payload: DeliveryCheckIn):
    """Renvoie le minimum de commande et les frais de livraison pour un code postal donné."""
    return calculate_delivery(payload.postal_code, payload.city or "", payload.subtotal)


@router.post("", response_model=OrderOut)
def create_order(payload: OrderIn, db: Session = Depends(get_db)):
    """Crée une commande. Le sous-total est recalculé côté serveur à partir des prix
    en base (jamais confiance aux prix envoyés par le frontend). Si livraison, vérifie
    aussi que le montant minimum de la zone est bien atteint."""
    if not payload.items:
        raise HTTPException(status_code=400, detail="Le panier est vide")

    if payload.order_type not in ("emporter", "livraison"):
        raise HTTPException(status_code=400, detail="order_type invalide")
    if payload.payment_method not in ("carte", "sur_place"):
        raise HTTPException(status_code=400, detail="payment_method invalide")

    subtotal = 0.0
    order_items = []
    for item in payload.items:
        dish = db.query(Dish).filter(Dish.id == item.dish_id, Dish.is_available).first()
        if not dish:
            raise HTTPException(
                status_code=400, detail=f"Plat indisponible (id={item.dish_id})"
            )
        qty = max(1, min(item.quantity, 50))  # bornes de sécurité
        subtotal += dish.price * qty
        order_items.append(
            OrderItem(
                dish_id=dish.id,
                dish_name=dish.name_fr,
                unit_price=dish.price,
                quantity=qty,
            )
        )
    subtotal = round(subtotal, 2)

    delivery_fee = 0.0
    if payload.order_type == "livraison":
        if not payload.postal_code or not payload.address_street:
            raise HTTPException(
                status_code=400, detail="Adresse incomplète pour une livraison"
            )
        zone = calculate_delivery(payload.postal_code, payload.city or "", subtotal)
        if not zone["meets_minimum"]:
            raise HTTPException(
                status_code=400,
                detail=f"Montant minimum de {zone['minimum']}€ non atteint pour cette zone",
            )
        delivery_fee = zone["fee"]

    total = round(subtotal + delivery_fee, 2)

    order = Order(
        customer_name=f"{payload.first_name.strip()} {payload.last_name.strip()}".strip(),
        customer_phone=payload.phone.strip(),
        customer_email=(payload.email or "").strip(),
        note=payload.note or "",
        order_type=payload.order_type,
        requested_date=payload.requested_date or "",
        requested_time=payload.requested_time or "",
        address_street=payload.address_street or "",
        address_extra=payload.address_extra or "",
        postal_code=payload.postal_code or "",
        city=payload.city or "",
        subtotal=subtotal,
        delivery_fee=delivery_fee,
        total=total,
        payment_method=payload.payment_method,
        payment_status="en_attente",
        language=payload.language or "fr",
    )
    order.items = order_items

    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.post("/{order_id}/create-payment-intent", response_model=PaymentIntentOut)
def create_payment_intent(order_id: int, db: Session = Depends(get_db)):
    """Crée un PaymentIntent Stripe pour le montant total de la commande."""
    if not STRIPE_SECRET_KEY:
        raise HTTPException(
            status_code=503,
            detail="Le paiement en ligne n'est pas encore configuré (STRIPE_SECRET_KEY manquant)",
        )

    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Commande introuvable")
    if order.payment_method != "carte":
        raise HTTPException(
            status_code=400, detail="Cette commande n'est pas payée par carte"
        )

    import stripe

    stripe.api_key = STRIPE_SECRET_KEY

    try:
        intent = stripe.PaymentIntent.create(
            amount=round(order.total * 100),  # Stripe attend des centimes
            currency="eur",
            payment_method_types=["card"],  # inclut automatiquement Apple Pay / Google Pay
            metadata={"order_id": str(order.id)},
        )
    except Exception:
        logger.exception("Échec de la création du PaymentIntent Stripe")
        raise HTTPException(status_code=502, detail="Erreur lors de la préparation du paiement")

    order.stripe_payment_intent_id = intent.id
    db.commit()

    return {"client_secret": intent.client_secret, "amount": order.total}
