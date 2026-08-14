# routers/orders.py — Commandes (click & collect + livraison), avec paiement Stripe optionnel.

import json
import os
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import (
    OrderIn,
    OrderOut,
    DeliveryCheckIn,
    DeliveryCheckOut,
    PaymentIntentOut,
)
from models import Dish, Order, OrderItem, Category
from delivery import calculate_delivery
from typing import Optional, Dict, List
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

            validate_choice_groups(dish, item.selected_choices, db)  # NOUVEAU

            qty = max(1, min(item.quantity, 50))  # bornes de sécurité
            subtotal += dish.price * qty
            order_items.append(
                OrderItem(
                    dish_id=dish.id,
                    dish_name=dish.name_fr,
                    unit_price=dish.price,
                    quantity=qty,
                    removed_ingredients=json.dumps(item.removed_ingredients or []),
                    selected_choices=json.dumps(
                        {k: v.dict() for k, v in item.selected_choices.items()}
                    ) if item.selected_choices else None,  # NOUVEAU
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
        if zone["call_required"]:
            raise HTTPException(
                status_code=400,
                detail=f"Cette adresse est hors de notre zone de livraison automatique. Merci d'appeler le {zone['call_phone']} pour passer votre commande.",
            )
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

def _validate_alternative_option(alt: dict, dish_ids: list[int], db: Session) -> bool:
    """Vérifie que dish_ids ⊆ ensemble éligible pour cette option d'alternative."""
    if "dish_ids" in alt:
        return set(dish_ids).issubset(set(alt["dish_ids"]))
    elif "source_category" in alt:
        eligible = db.query(Dish.id).join(Category, Dish.category_id == Category.id).filter(
            Category.name_fr == alt["source_category"]
        ).all()
        eligible_ids = {row[0] for row in eligible}
        return set(dish_ids).issubset(eligible_ids)
    return False
def validate_choice_groups(dish: Dish, selected_choices: Optional[Dict], db: Session):
    rules = json.loads(dish.customization_rules) if dish.customization_rules else {}
    choice_groups = rules.get("choice_groups")
    if not choice_groups:
        return

    if not selected_choices:
        raise HTTPException(400, f"Sélection requise pour {dish.name_fr}")

    for group in choice_groups:
        label = group["label"]
        selection = selected_choices.get(label)

        if group.get("type") == "alternative":
            if not selection or not selection.alternative:
                raise HTTPException(400, f"Choix requis pour « {label} »")
            alt = next((a for a in group["alternatives"] if a["name"] == selection.alternative), None)
            if not alt:
                raise HTTPException(400, f"Alternative inconnue pour « {label} »")
            if len(selection.dish_ids) != alt["count"]:
                raise HTTPException(400, f"« {selection.alternative} » nécessite {alt['count']} sélection(s)")
            if not _validate_alternative_option(alt, selection.dish_ids, db):
                raise HTTPException(400, f"Choix invalide pour « {label} »")
        else:
            max_count = group.get("max", 1)
            min_count = group.get("min", max_count)
            chosen_ids = selection.dish_ids if selection else []
            if not (min_count <= len(chosen_ids) <= max_count):
                raise HTTPException(400, f"Sélection invalide pour « {label} »")
            eligible = db.query(Dish.id).join(Category, Dish.category_id == Category.id).filter(
                Category.name_fr == group["source_category"]
            ).all()
            eligible_ids = {row[0] for row in eligible}
            if not set(chosen_ids).issubset(eligible_ids):
                raise HTTPException(400, f"Un choix pour « {label} » n'appartient pas à {group['source_category']}")

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