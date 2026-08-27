# main.py — Backend Miss Chawarma
# Chatbot (existant) + Menu + Commandes + Réservations + Contact + Admin

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from admin import setup_admin
from routers import menu, orders, table_reservations, contact, verification, event_reservations
from routers import chatbot  # ← décommente après avoir créé routers/chatbot.py
from routers import stripe_webhook 
from routers import maintenance
from fastapi.middleware.gzip import GZipMiddleware
load_dotenv()
# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Miss Chawarma API")

# ─────────────── CORS ───────────────
ALLOWED_ORIGINS = [
    "https://misschawarma.fr",
    "https://www.misschawarma.fr",
    "https://misschawarma.netlify.app",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://192.168.1.29:8080",
    "http://172.20.10.2:8080",
    "http://10.86.1.217:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}):8080",
    allow_origins=[
        "https://idyllic-cat-4762a5.netlify.app",  # ⟵ AJOUT
        "https://misschawarma.fr", 
        "https://misschawarma.netlify.app",                 # ton domaine final, si différent
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────── Images du chatbot / du menu ───────────────
app.mount("/images", StaticFiles(directory="images"), name="images")

# ─────────────── Routers ───────────────
app.include_router(menu.router)
app.include_router(orders.router)
app.include_router(table_reservations.router)
app.include_router(contact.router)
app.include_router(chatbot.router)  # ← décommente après migration
app.include_router(stripe_webhook.router)
app.include_router(verification.router)
app.include_router(event_reservations.router)
app.include_router(maintenance.router)

app.add_middleware(GZipMiddleware, minimum_size=1000)
# ─────────────── Admin (/admin) ───────────────
setup_admin(app)


@app.get("/")
def health():
    return {"status": "ok", "service": "Miss Chawarma API"}
