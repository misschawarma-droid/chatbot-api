# delivery.py — Zones de livraison et frais associés.
#
# Grille :
#   Paris intra-muros (par arrondissement) :
#     20€ : 75011
#     25€ : 75003, 75004, 75010, 75019, 75020
#     50€ : 75001, 75002, 75005, 75006, 75009, 75012, 75018
#     60€ : 75007, 75008, 75013, 75014, 75017
#     70€ : 75015, 75016
#   Proche banlieue (< 5 km) : 30€ minimum
#   Banlieue élargie (5-10 km) : 50€ minimum
#   Au-delà : appel obligatoire au +33 7 82 73 77 77 (pas de commande en ligne)
#   Frais standard : 5€, sauf 75011 → 2€
#   Livraison gratuite au-dessus de 100€ de commande

import unicodedata
from typing import Optional

PARIS_ZONES: dict[str, float] = {
    "75011": 20,
    "75003": 25,
    "75004": 25,
    "75010": 25,
    "75019": 25,
    "75020": 25,
    "75001": 50,
    "75002": 50,
    "75005": 50,
    "75006": 50,
    "75009": 50,
    "75012": 50,
    "75018": 50,
    "75007": 60,
    "75008": 60,
    "75013": 60,
    "75014": 60,
    "75017": 60,
    "75015": 70,
    "75016": 70,
}

NEAR_SUBURB_CITIES: set[str] = {
    "le pre-saint-gervais",
    "les lilas",
    "bagnolet",
    "pantin",
    "montreuil",
    "saint-mande",
    "vincennes",
}

FAR_SUBURB_CITIES: set[str] = {
    "charenton-le-pont",
    "ivry-sur-seine",
    "le kremlin-bicetre",
    "gentilly",
    "montrouge",
    "malakoff",
    "clichy",
    "saint-ouen-sur-seine",
    "saint-ouen",
    "aubervilliers",
    "villejuif",
    "nogent-sur-marne",
    "levallois-perret",
    "issy-les-moulineaux",
    "vanves",
    "arcueil",
    "maisons-alfort",
    "alfortville",
    "neuilly-sur-seine",
    "romainville",
    "saint-denis",
}

NEAR_SUBURB_MINIMUM = 30.0
FAR_SUBURB_MINIMUM = 50.0

CALL_REQUIRED_PHONE = "+33 7 82 73 77 77"

STANDARD_FEE = 5.0
REDUCED_FEE_POSTAL_CODES: dict[str, float] = {
    "75011": 2.0,
}

FREE_DELIVERY_THRESHOLD = 100.0


def _normalize(text: str) -> str:
    """Passe en minuscules et retire les accents pour un matching robuste
    (ex: 'Saint-Mandé' et 'saint-mande' doivent matcher)."""
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))


def calculate_delivery(postal_code: str, city: str, subtotal: float) -> dict:
    """Calcule le minimum de commande et les frais de livraison pour une adresse donnée.

    Si l'adresse est hors du périmètre couvert (ni Paris, ni banlieue listée),
    renvoie call_required=True : la commande en ligne doit être bloquée et le
    client redirigé vers un appel téléphonique.
    """
    postal_code = (postal_code or "").strip()
    city_norm = _normalize(city or "")

    minimum: Optional[float] = PARIS_ZONES.get(postal_code)
    call_required = False

    if minimum is None:
        if city_norm in NEAR_SUBURB_CITIES:
            minimum = NEAR_SUBURB_MINIMUM
        elif city_norm in FAR_SUBURB_CITIES:
            minimum = FAR_SUBURB_MINIMUM
        else:
            call_required = True

    fee = REDUCED_FEE_POSTAL_CODES.get(postal_code, STANDARD_FEE)
    if subtotal >= FREE_DELIVERY_THRESHOLD:
        fee = 0.0

    meets_minimum = (not call_required) and (minimum is None or subtotal >= minimum)

    return {
        "minimum": minimum,
        "fee": fee,
        "meets_minimum": meets_minimum,
        "free_delivery_threshold": FREE_DELIVERY_THRESHOLD,
        "call_required": call_required,
        "call_phone": CALL_REQUIRED_PHONE if call_required else None,
    }