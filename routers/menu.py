# routers/menu.py — Lecture du menu complet (public)

import json
import time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Category, Dish

router = APIRouter(prefix="/api/menu", tags=["menu"])

# Cache mémoire : long (10 min) pour une vitesse maximale, mais invalidé
# immédiatement dès qu'un plat/catégorie est modifié via l'admin.
_menu_cache = {"data": None, "timestamp": 0}
CACHE_DURATION = 600  # 10 minutes


def invalidate_menu_cache():
    """À appeler dès qu'un plat ou une catégorie change (admin)."""
    _menu_cache["data"] = None
    _menu_cache["timestamp"] = 0


def _build_menu(db: Session):
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
                    "hidden": d.hidden,
                    "customization_rules": json.loads(d.customization_rules) if d.customization_rules and d.customization_rules != "null" else None,
                }
                for d in dishes
            ],
        })
    return result


@router.get("")
def get_menu(db: Session = Depends(get_db)):
    """Toutes les catégories avec leurs plats disponibles (structure complète FR/EN)."""
    now = time.time()
    if _menu_cache["data"] is not None and (now - _menu_cache["timestamp"]) < CACHE_DURATION:
        return _menu_cache["data"]

    result = _build_menu(db)
    _menu_cache["data"] = result
    _menu_cache["timestamp"] = now
    return result


@router.get("/category/{category_name}")
def get_dishes_by_category(category_name: str, db: Session = Depends(get_db)):
    dishes = db.query(Dish).filter(
        Dish.category == category_name,
        Dish.available == True
    ).all()
    return [
        {"id": d.id, "name": d.name, "price": d.price, "image": d.image_url}
        for d in dishes
    ]