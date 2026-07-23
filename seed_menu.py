# seed_menu.py — Remplit la base avec le menu complet (menu_data.py)
# Lance : python seed_menu.py

import json
from database import Base, engine, SessionLocal
from models import Category, Dish
from menu_data import MENU_DATA


def euro(price: float) -> str:
    """20.0 -> '20€', 8.9 -> '8,90€'"""
    if price == int(price):
        return f"{int(price)}€"
    return f"{price:.2f}".replace(".", ",") + "€"


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Category).count() > 0:
            print("⚠️  La base contient déjà des catégories. Abandon pour éviter les doublons.")
            print("    → Vide les tables 'dishes' et 'categories' (phpMyAdmin) puis relance.")
            return

        total_dishes = 0
        for cat_pos, cat in enumerate(MENU_DATA):
            category = Category(
                name_fr=cat["name_fr"],
                name_en=cat["name_en"],
                subtitle_fr=cat.get("subtitle_fr", ""),
                subtitle_en=cat.get("subtitle_en", ""),
                position=cat_pos,
            )
            db.add(category)
            db.flush()

            for dish_pos, d in enumerate(cat["dishes"]):
                db.add(Dish(
                    category_id=category.id,
                    name_fr=d["name_fr"],
                    name_en=d["name_en"],
                    short_fr=d.get("short_fr", ""),
                    short_en=d.get("short_en", ""),
                    price=d["price"],
                    price_label_fr=d.get("label_fr", euro(d["price"])),
                    price_label_en=d.get("label_en", euro(d["price"])),
                    composition_fr=json.dumps(d.get("comp_fr", []), ensure_ascii=False),
                    composition_en=json.dumps(d.get("comp_en", []), ensure_ascii=False),
                    allergens_fr=json.dumps(d.get("all_fr", []), ensure_ascii=False),
                    allergens_en=json.dumps(d.get("all_en", []), ensure_ascii=False),
                    image_url=d.get("image", ""),
                    position=dish_pos,
                ))
                total_dishes += 1

        db.commit()
        print(f"✅ {len(MENU_DATA)} catégories et {total_dishes} plats insérés !")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
