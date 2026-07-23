# routers/menu.py — Lecture du menu complet (public)

import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Category

router = APIRouter(prefix="/api/menu", tags=["menu"])


@router.get("")
def get_menu(db: Session = Depends(get_db)):
    """Toutes les catégories avec leurs plats disponibles (structure complète FR/EN)."""
    categories = db.query(Category).order_by(Category.position).all()
    result = []
    for cat in categories:
        dishes = sorted(
            [d for d in cat.dishes if d.is_available],
            key=lambda d: d.position,
        )
        result.append({
            "id": cat.id,
            "name_fr": cat.name_fr,
            "name_en": cat.name_en,
            "subtitle_fr": cat.subtitle_fr,
            "subtitle_en": cat.subtitle_en,
            "dishes": [
                {
                    "id": d.id,
                    "name_fr": d.name_fr,
                    "name_en": d.name_en,
                    "short_fr": d.short_fr,
                    "short_en": d.short_en,
                    "price": d.price,
                    "price_label_fr": d.price_label_fr,
                    "price_label_en": d.price_label_en,
                    "composition_fr": json.loads(d.composition_fr or "[]"),
                    "composition_en": json.loads(d.composition_en or "[]"),
                    "allergens_fr": json.loads(d.allergens_fr or "[]"),
                    "allergens_en": json.loads(d.allergens_en or "[]"),
                    "image_url": d.image_url,
                }
                for d in dishes
            ],
        })
    return result
