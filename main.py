# main.py — Backend Miss Chawarma
# Chatbot (existant) + Menu + Commandes + Réservations + Contact + Admin


import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from admin import setup_admin
from routers import menu, orders, reservations, contact
from routers import chatbot  # ← décommente après avoir créé routers/chatbot.py
from routers import stripe_webhook 
load_dotenv()

# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Miss Chawarma API")

# ─────────────── CORS ───────────────
ALLOWED_ORIGINS = [
    "https://misschawarma.fr",
    "https://www.misschawarma.fr",
    "http://localhost:8080",
    "http://localhost:5173",
  #  "http://192.168.0.12:8080",  # ton IP locale de dev 
    "http://192.168.1.29:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────── Images du chatbot / du menu ───────────────
app.mount("/images", StaticFiles(directory="images"), name="images")

# ─────────────── Routers ───────────────
app.include_router(menu.router)
app.include_router(orders.router)
app.include_router(reservations.router)
app.include_router(contact.router)
app.include_router(chatbot.router)  # ← décommente après migration
app.include_router(stripe_webhook.router)
# ─────────────── Admin (/admin) ───────────────
setup_admin(app)


@app.get("/")
def health():
    return {"status": "ok", "service": "Miss Chawarma API"}
