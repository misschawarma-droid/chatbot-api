# schemas.py — Schémas Pydantic (validation des requêtes/réponses)

from typing import List, Optional
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

class OrderItemIn(BaseModel):
    dish_id: int
    quantity: int
    removed_ingredients: Optional[List[str]] = []

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


class OrderOut(BaseModel):
    id: int
    subtotal: float
    delivery_fee: float
    total: float
    status: str
    payment_method: str
    payment_status: str

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
