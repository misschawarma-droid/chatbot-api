# delivery.py — Zones de livraison et frais associés.
#
# Reprend exactement la même grille que la référence fournie :
#   40€ minimum : 75014
#   50€ minimum : 75015, 75013, 75006, 75005, Montrouge
#   60€ minimum : 75007, 75008
#   70€ minimum : 75012, 75010, 75011, 75016, 75009, 75003
#   94 et 92 (hors Montrouge) : minimum 100€
#   Banlieue nord/ouest (93, 78, 95) : minimum 200€
#   Frais standard : 5€, sauf 75014 → 2€
#   Livraison gratuite au-dessus de 100€ de commande

from typing import Optional

DELIVERY_ZONES: dict[str, float] = {
    "75014": 40,
    "75015": 50,
    "75013": 50,
    "75006": 50,
    "75005": 50,
    "75007": 60,
    "75008": 60,
    "75012": 70,
    "75010": 70,
    "75011": 70,
    "75016": 70,
    "75009": 70,
    "75003": 70,
}

# Villes gérées par nom plutôt que par code postal
CITY_MINIMUMS: dict[str, float] = {
    "montrouge": 50,
}

# Minimum par département (préfixe du code postal), si aucune règle plus précise ne s'applique
DEPARTMENT_MINIMUMS: dict[str, float] = {
    "92": 100,
    "94": 100,
    "93": 200,  # banlieue nord (approximation)
    "78": 200,  # banlieue ouest (approximation)
    "95": 200,  # banlieue nord-ouest (approximation)
}

REDUCED_FEE_POSTAL_CODES: dict[str, float] = {
    "75014": 2,
}

STANDARD_FEE = 5.0
FREE_DELIVERY_THRESHOLD = 100.0


def calculate_delivery(postal_code: str, city: str, subtotal: float) -> dict:
    """Calcule le minimum de commande et les frais de livraison pour une adresse donnée."""
    postal_code = (postal_code or "").strip()
    city_norm = (city or "").strip().lower()

    minimum: Optional[float] = DELIVERY_ZONES.get(postal_code)
    if minimum is None:
        minimum = CITY_MINIMUMS.get(city_norm)
    if minimum is None and len(postal_code) >= 2:
        minimum = DEPARTMENT_MINIMUMS.get(postal_code[:2])

    fee = REDUCED_FEE_POSTAL_CODES.get(postal_code, STANDARD_FEE)
    if subtotal >= FREE_DELIVERY_THRESHOLD:
        fee = 0.0

    meets_minimum = minimum is None or subtotal >= minimum

    return {
        "minimum": minimum,
        "fee": fee,
        "meets_minimum": meets_minimum,
        "free_delivery_threshold": FREE_DELIVERY_THRESHOLD,
    }
