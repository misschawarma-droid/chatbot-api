# models.py — Modèles de la base de données Miss Chawarma
# v2 : Dish enrichi (price_label, composition, allergènes bilingues)

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from database import Base


# ─────────────── MENU ───────────────

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name_fr = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=False)
    subtitle_fr = Column(String(200), default="")
    subtitle_en = Column(String(200), default="")
    position = Column(Integer, default=0)

    dishes = relationship("Dish", back_populates="category", cascade="all, delete")

    def __str__(self):
        return self.name_fr


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name_fr = Column(String(150), nullable=False)
    name_en = Column(String(150), nullable=False)
    short_fr = Column(Text, default="")           # description courte
    short_en = Column(Text, default="")
    price = Column(Float, nullable=False)          # prix utilisé pour le panier
    price_label_fr = Column(String(100), default="")  # ex : "8,90€ / 4 pièces · 15,90€ / 8 pièces"
    price_label_en = Column(String(100), default="")
    composition_fr = Column(Text, default="[]")   # liste JSON
    composition_en = Column(Text, default="[]")
    allergens_fr = Column(Text, default="[]")     # liste JSON
    allergens_en = Column(Text, default="[]")
    image_url = Column(String(300), default="")
    is_available = Column(Boolean, default=True)
    position = Column(Integer, default=0)

    category = relationship("Category", back_populates="dishes")

    def __str__(self):
        return f"{self.name_fr} ({self.price}€)"


# ─────────────── COMMANDES (panier / click & collect) ───────────────

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(150), nullable=False)
    customer_phone = Column(String(30), nullable=False)
    customer_email = Column(String(150), default="")
    pickup_time = Column(String(20), default="")  # ancien champ, conservé pour compatibilité
    note = Column(Text, default="")

    order_type = Column(String(20), default="emporter")  # "emporter" ou "livraison"
    requested_date = Column(String(20), default="")
    requested_time = Column(String(20), default="")
    address_street = Column(String(300), default="")
    address_extra = Column(String(300), default="")
    postal_code = Column(String(10), default="")
    city = Column(String(100), default="")

    subtotal = Column(Float, default=0.0)
    delivery_fee = Column(Float, default=0.0)
    total = Column(Float, nullable=False)

    payment_method = Column(String(20), default="sur_place")  # "carte" ou "sur_place"
    payment_status = Column(String(20), default="en_attente")  # en_attente / payé / échoué
    stripe_payment_intent_id = Column(String(200), default="")
    language = Column(String(2), default="fr")

    status = Column(String(30), default="nouvelle")
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("OrderItem", back_populates="order", cascade="all, delete")

    def __str__(self):
        return f"Commande #{self.id} — {self.customer_name} — {self.total}€"


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=True)
    dish_name = Column(String(150), nullable=False)
    unit_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    order = relationship("Order", back_populates="items")

    def __str__(self):
        return f"{self.quantity}× {self.dish_name}"


# ─────────────── RÉSERVATIONS ───────────────

class TableReservation(Base):
    __tablename__ = "table_reservations"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(30), nullable=False)
    date = Column(String(20), nullable=False)
    time = Column(String(10), nullable=False)
    guests = Column(Integer, nullable=False)
    note = Column(Text, default="")
    status = Column(String(30), default="nouvelle")
    language = Column(String(2), default="fr")  # "fr" ou "en" — langue du site au moment de la réservation
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"Table — {self.first_name} {self.last_name} — {self.date} {self.time} ({self.guests} pers.)"


class EventReservation(Base):
    __tablename__ = "event_reservations"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(80), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(30), nullable=False)
    date = Column(String(20), nullable=False)
    time = Column(String(10), nullable=False)
    guests = Column(Integer, nullable=False)
    details = Column(Text, default="")
    note = Column(Text, default="")
    status = Column(String(30), default="nouvelle")
    language = Column(String(2), default="fr")  # "fr" ou "en" — langue du site au moment de la réservation
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.event_type} — {self.first_name} {self.last_name} — {self.date} ({self.guests} pers.)"


# ─────────────── CONTACT ───────────────

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(30), default="")
    subject = Column(String(200), default="")
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    status = Column(String(30), default="nouveau")  # nouveau / répondu
    language = Column(String(2), default="fr")  # "fr" ou "en" — langue du site au moment de l'envoi
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.name} — {self.subject or self.message[:40]}"


# ─────────────── AVIS (saisis à la main dans l'admin — 100% gratuit) ───────────────

class ReviewsSummary(Base):
    """Une seule ligne : la note globale et le nombre total d'avis affichés
    (recopiés à la main depuis ta fiche Google Business, gratuitement)."""
    __tablename__ = "reviews_summary"

    id = Column(Integer, primary_key=True)
    rating = Column(Float, default=4.5)
    total = Column(Integer, default=0)

    def __str__(self):
        return f"Résumé avis — {self.rating}★ / {self.total} avis"


class Review(Base):
    """Un avis individuel, copié-collé à la main depuis Google Maps."""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(150), nullable=False)
    rating = Column(Integer, default=5)  # 1 à 5
    text = Column(Text, default="")
    relative_time = Column(String(50), default="")  # texte libre, ex : "il y a 2 semaines"
    is_visible = Column(Boolean, default=True)
    position = Column(Integer, default=0)  # ordre d'affichage
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.author_name} — {self.rating}★"
