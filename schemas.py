# schemas.py — Schémas Pydantic (validation des requêtes/réponses)

from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, Field


# ─────────────── MENU ───────────────

class DishOut(BaseModel):
    id: int
    name_fr: str
    name_en: str
    description_fr: str
    description_en: str
    price: float
    image_url: str
    is_available: bool
    customization_rules: Optional[str] = None

    class Config:
        from_attributes = True


class CategoryOut(BaseModel):
    id: int
    name_fr: str
    name_en: str
    subtitle_fr: str
    subtitle_en: str
    dishes: List[DishOut]

    class Config:
        from_attributes = True


# ─────────────── COMMANDES ───────────────
class ChoiceSelection(BaseModel):
    dish_ids: List[int] = []
    alternative: Optional[str] = None
    options: Optional[List[str]] = None
    sub_removed: Optional[List[str]] = None
    sub_choices: Optional[Dict[str, List[str]]] = None
    sub_removed_by_unit: Optional[List[List[str]]] = None       # NOUVEAU
    sub_choices_by_unit: Optional[List[Dict[str, List[str]]]] = None  # NOUVEAU

class OrderItemIn(BaseModel):
    dish_id: int
    quantity: int
    removed_ingredients: Optional[List[str]] = []
    selected_choices: Optional[Dict[str, ChoiceSelection]] = None
    note: Optional[str] = None

class OrderIn(BaseModel):
    order_type: str  # "emporter" ou "livraison"
    first_name: str
    last_name: str
    email: Optional[str] = ""
    phone: str
    requested_date: Optional[str] = ""
    requested_time: Optional[str] = ""
    address_street: Optional[str] = ""
    address_extra: Optional[str] = ""
    postal_code: Optional[str] = ""
    city: Optional[str] = ""
    note: Optional[str] = ""
    payment_method: str  # "carte" ou "sur_place"
    language: Optional[str] = "fr"
    items: List[OrderItemIn]
    coupon_code: Optional[str] = None


class OrderOut(BaseModel):
    id: int
    subtotal: float
    delivery_fee: float
    total: float
    status: str
    payment_method: str
    payment_status: str
    new_coupon_code: Optional[str] = None

    class Config:
        from_attributes = True


class DeliveryCheckIn(BaseModel):
    postal_code: str
    city: Optional[str] = ""
    subtotal: float = 0.0


class DeliveryCheckOut(BaseModel):
    minimum: Optional[float] = None
    fee: float
    meets_minimum: bool
    free_delivery_threshold: float
    call_required: bool = False
    call_phone: Optional[str] = None


class PaymentIntentOut(BaseModel):
    client_secret: str
    amount: float


# ─────────────── RÉSERVATIONS ───────────────

class TableReservationIn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date: str
    time: str
    guests: int
    note: Optional[str] = ""
    language: Optional[str] = "fr"
    table_ids: List[str] = Field(min_length=1, max_length=6)  # ⟵ AJOUT
 
 
class TableReservationOut(BaseModel):  # ⟵ AJOUT — réponse après création
    id: int
    table_ids: List[str]
    status: str
 
    class Config:
        from_attributes = True
 
 
class TableAvailabilityOut(BaseModel):  # ⟵ AJOUT — réponse de /availability
    occupied_table_ids: List[str]
 # À ajouter dans schemas.py, juste après TableAvailabilityOut

class TableReservationLookupIn(BaseModel):
    reference: int
    email: EmailStr

class TableReservationLookupOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str          # ⟵ AJOUT
    date: str
    time: str
    guests: int
    table_ids: List[str]
    status: str

    class Config:
        from_attributes = True

class TableReservationModifyIn(BaseModel):
    reference: int
    email: EmailStr
    date: str
    time: str
    guests: int
    table_ids: Optional[List[str]] = None 
    first_name: Optional[str] = None   # ⟵ AJOUT
    last_name: Optional[str] = None    # ⟵ AJOUT
    phone: Optional[str] = None        # ⟵ AJOUT

class TableReservationCancelIn(BaseModel):
    reference: int
    email: EmailStr

class TableReservationLookupIn(BaseModel):
    reference: int
    email: EmailStr


    class Config:
        from_attributes = True



class TableReservationCancelIn(BaseModel):
    reference: int
    email: EmailStr


class EventReservationIn(BaseModel):
    event_type: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date: str
    time: str
    guests: int
    details: Optional[str] = ""
    note: Optional[str] = ""
    language: Optional[str] = "fr"


# ─────────────── CONTACT ───────────────

class ContactIn(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = ""
    subject: Optional[str] = ""
    message: str
    language: Optional[str] = "fr"

class CouponCheckIn(BaseModel):
    code: str
    email: str
    phone: str

class CouponCheckOut(BaseModel):
    valid: bool
    discount_percent: Optional[int] = None
    message: Optional[str] = None

class SendVerificationCodeIn(BaseModel):
    email: str

class SendVerificationCodeOut(BaseModel):
    sent: bool
    message: Optional[str] = None

class VerifyCodeIn(BaseModel):
    email: str
    code: str

class VerifyCodeOut(BaseModel):
    verified: bool
    message: Optional[str] = None