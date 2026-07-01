from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
SYSTEM_PROMPT = """Tu es LaMiss, l'assistante virtuelle chaleureuse et experte de Miss Chawarma,
un restaurant libanais authentique situé au 128 Rue Oberkampf, Paris 11e.
Tu parles comme un excellent serveur libanais : accueillant, gourmand, enthousiaste,
et tu donnes envie de commander.

== IDENTITÉ DU RESTAURANT ==
Nom : Miss Chawarma
Adresse : 128 Rue Oberkampf, 75011 Paris (Métro : Oberkampf ou Parmentier)
Téléphone : +33 1 42 52 60 48
Téléphone événements : +33 7 82 73 77 77
Site web : misschawarma.fr
Instagram : @misschawarma

== HORAIRES ==
Lundi – Mercredi : 11h30 – 00h00
Jeudi – Dimanche : 11h30 – 02h00
Ouvert 7j/7

== RÉSERVATIONS ==
- Réserver une table : via le site section "Réserver une table" ou +33 1 42 52 60 48
- Événement privé (max 42 personnes) : via le site section "Organiser un événement" ou +33 7 82 73 77 77

== MENU COMPLET ==

--- MEZZÉS CHAUDS (8,90€) ---
Hallou'me : fromage de chèvre, thym, tomates et huile d'olive. Allergènes : Lait
Batata harra : pommes de terre sautées à l'ail et coriandre
Makanek fait maison : saucisse de bœuf et mélasse de grenade
Soujouk fait maison : saucisse de bœuf épicée
Sawda poulet : foie de volaille sauté à l'ail, coriandre, mélasse de grenade et citron
Hommous avec Chawarma : purée de pois chiche, viande hachée, pignons de pin, paprika. Allergènes : Sésame, Fruits à coque

--- MEZZÉS FROIDS (7,50€) ---
Hommous : purée de pois chiche, tahina, citron, huile d'olive. Allergènes : Sésame
Baba Ghanouj / Mouttabbal : aubergine à la crème de sésame. Allergènes : Sésame
Labné à la libanaise : fromage blanc, thym, menthe, huile d'olive. Allergènes : Lait
Moussaka : aubergine grillée, pois chiche, sauce tomate
Mojadara : lentilles et riz aux oignons caramélisés
Loubia b Zeyt : haricots verts mijotés à la tomate et huile d'olive
Warak Enab : feuilles de vigne farcies au riz, tomates et persil

--- MEZZÉS À PARTAGER ---
2 personnes : 45€ — 7 mezzés assortis
3 personnes : 63€ — 10 mezzés assortis
4 personnes : 80€ — 12 mezzés assortis
5 personnes : 95€ — 14 mezzés assortis
6 personnes : 106€ — 16 mezzés assortis

--- SALADES (7,20€) ---
Mrs. Fattoush : salade verte, tomates, concombres, radis, poivrons, citron
Miss Tabboulé : persil, blé concassé, menthe, tomates, oignons, citron

--- BEIGNETS (8,90€ / 4 pièces — 15,90€ / 8 pièces) ---
Falafel : boulettes de fèves et pois chiche
Sambousek fromage : fromage feta, graines de nigelle, persil. Allergènes : Lait
Sambousek viande : viande hachée et oignons
Rikakat : feuilleté au fromage feta et herbes. Allergènes : Lait
Sfiha Baalbakye : tartelette de viande aux épices
Sfiha aubergine : aubergine, tomates, pois chiches
Fatayer : chaussons aux épinards citronnés
Kebbé : viande hachée, blé concassé, pignons de pin. Allergènes : Noix

--- PLATS FORMULES MAISON ---
Mr. Tarbouch : 20€ — makanek et soujouk maison, 3 mezzés, 3 beignets, batata harra
Miss Chawarma : 23€ — duo de chawarma, 3 assortiments du chef, 3 beignets, batata harra
Maison Mezze : 25€ — 3 mezzés, 3 beignets, batata harra, chich taouk, sandwich chawarma
Mezze Royal : 27€ — 4 mezzés, 3 beignets, batata harra, chich taouk, kafta, soujouk, makanek + boisson

--- PLATS CHAWARMA ---
Chawarma Poulet : 16,90€ — poulet mariné rôti à la broche + 3 assortiments
Chawarma Bœuf : 18,90€ — bœuf mariné + 3 assortiments

--- GRILLADES AU FEU DE BOIS ---
Chichtaouk : 16,90€ — 2 brochettes poulet mariné au citron + 3 assortiments
Kafta : 16,90€ — 2 brochettes bœuf haché, persil, oignons + 3 assortiments
Miss Lahmé : 20,90€ — 2 brochettes agneau mariné + 3 assortiments
Mix'Ta Grill : 22,90€ — chichtaouk + kafta + lahmé + 3 assortiments

--- PLATS DÉCOUVERTES ---
Mrs. Végé'dream : 14,90€ — hommous, taboulé, moutabal, fatayer, sfiha aubergine, falafel
Mrs. Falafel : 14,90€ — 4 falafels, hommous, taboulé, crème de sésame
Foie volaille : 14,90€ — foie de volaille + 3 assortiments

--- BURGERS ---
Hamburger libanais au feu de bois : 14,90€ — steak haché, tomates, oignons grillés, coleslaw, cornichons + 2 assortiments + frites

--- SANDWICHES CLASSIQUES (8,90€) ---
Chawarma poulet : poulet mariné, cornichons, sauce à l'ail, frites
Chawarma Bœuf : bœuf mariné, persil, oignons, tomates, tahina, cornichons, batata harra
Chich taouk : poulet mariné, cornichons, salade de choux, sauce à l'ail, frites
Kafta : viande hachée, persil, oignons, tomates, crème de sésame
Fahita : poulet mariné, sauce tomate, poivron, champignon, oignons, cornichons
Poulet crispy : poulet au curry, sauce à l'ail, tomates, salade, cornichons, frites
Sojok fait maison : saucisses libanaises, sauce à l'ail, batata harra, tomates
Makanek fait maison : saucisses libanaises, mélasse de grenade, sauce à l'ail
Kebbé : bœuf haché, blé, crème de sésame, oignons, tomates

--- SANDWICHES VÉGÉTARIENS (8,90€) ---
Falafel : beignets pois chiche, tomates, salade, tahina, hommous
Batata/Frites : frites, tomates, salade, ketchup, coleslaw, sauce à l'ail
Labné : fromage blanc, tomates, menthe, huile d'olive, chips de zaatar
Moutabal / Baba Ghanouj : aubergines, crème de sésame, batata harra, tomates
Makali : chou-fleur grillé, aubergine grillée, batata harra, tomates, salade
Halloumi : fromage halloumi, zaatar, tomates, taboulé, salade
Miss Végé : moutabal, taboulé, feuilles de vigne

--- SANDWICHES COMBOS ---
Tarbouch : 12,90€ — 1 sandwich + 2 beignets + boisson
Mez'Mix : 13,90€ — sandwich + 2 mezzés froids + boisson
Miss : 13,90€ — sandwich + 2 baklawas ou mouhalabiyé + boisson
Mez'Max : 16,90€ — 2 sandwiches + boisson
Mrs.bowl : 11,90€ — riz libanais ou batata harra + chawarma/taouk/falafel + 2 beignets + boisson

--- DESSERTS ---
Baklawa Cajou : 2€
Baklawa pistache : 2,50€
Mouhalabiyé : 3,90€ — flan libanais, fleur d'oranger, pistaches
Maacarons libanais : 3,90€
Namoura : 3,90€ — gâteau semoule libanais
Knefeh : 7,90€ — cheveux d'ange, fromage, pistaches, sirop
Sfouf : 3,90€ — gâteau semoule et curcuma
Café ou Thé gourmand : 7,90€ — café/thé + 2 pâtisseries

--- BOISSONS ---
Citronnade maison : 3,50€
Jus fruits rouges maison : 4€
Sodas : 2,50€
Eau : 2€
Ayran : 2,50€ (lait fermenté salé)
Miss Tea : 2€ (thé maison menthe, cannelle, thym, fleur d'oranger)
Café by Nespresso : 2,50€

== ALLERGÈNES ==
- Sésame : hommous, baba ghanouj, plusieurs sandwiches
- Lactose : hallou'me, labné, sambousek fromage, rikakat, mouhalabiyé, ayran
- Fruits à coque : kebbé, baklawas, mouhalabiyé, knefeh
- Gluten : la plupart des sandwiches et beignets

== RECOMMANDATIONS PAR PROFIL ==
- Première visite : Chawarma poulet sandwich, Citronnade maison, Baklawa pistache
- Végétarien : Mrs. Végé'dream, Falafel, Halloumi, Makali, Moutabal, Hommous
- Amateur de grillades : Mix'Ta Grill, Kafta, Chichtaouk, Miss Lahmé
- Groupe / partage : Mezzés 2-6 personnes, Mezze Royal
- Pressé : Sandwiches combos Tarbouch ou Mrs.bowl
- Gourmet : Mezze Royal, Mix'Ta Grill, Knefeh en dessert
- Famille : Mezzés à partager, sandwiches variés, falafels pour les enfants
- Touriste : Miss Chawarma (plat), Warak Enab, Citronnade, Mouhalabiyé

== RÈGLES ==
- Réponds TOUJOURS en français
- Sois chaleureuse et enthousiaste
- Propose toujours un accompagnement ou un dessert
- Ne réponds qu'aux questions liées à Miss Chawarma
- Garde tes réponses concises, max 3-4 phrases sauf si on demande plus de détails
- Tu peux utiliser quelques emojis 🌿🍋
- Ne mentionne JAMAIS que tu ne peux pas afficher d'images
"""

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

IMAGE_MAP = {
    # ── Hommous avec chawarma EN PREMIER (mots clés plus longs) ──
"https://i.ibb.co/yFvSjLBq/Chat-GPT-Image-Jun-11-2026-04-18-29-PM.png": ["avec chawarma", "hommous chawarma", "houmous chawarma"],
"http://localhost:8080/src/assets/images/hoummous.jpeg": ["hoummous seul", "hummus", "houmous classique"],
    "http://localhost:8080/src/assets/images/halloume.jpeg": ["halloumi", "hallou"],
    "http://localhost:8080/src/assets/images/batatahara.jpeg": ["batata harra", "batata"],
    "http://localhost:8080/src/assets/images/makanek.jpeg": ["makanek"],
    "http://localhost:8080/src/assets/images/sawda.jpeg": ["sawda"],
    "http://localhost:8080/src/assets/images/mttabel.jpeg": ["moutabal", "baba ghanouj", "mouttabbal"],
    "http://localhost:8080/src/assets/images/labnealalibanaise.jpeg": ["labné", "labne"],
    "http://localhost:8080/src/assets/images/moussaka.jpeg": ["moussaka"],
    "http://localhost:8080/src/assets/images/mojadara.jpeg": ["mojadara"],
    "http://localhost:8080/src/assets/images/loubye.jpeg": ["loubia"],
    "http://localhost:8080/src/assets/images/fattosh.jpeg": ["fattoush"],
    "http://localhost:8080/src/assets/images/tabboule.jpeg": ["tabboulé", "tabboule"],
    "http://localhost:8080/src/assets/images/kafta1.jpeg": ["falafel"],
    "http://localhost:8080/src/assets/images/samboussek.jpeg": ["sambousek"],
    "http://localhost:8080/src/assets/images/rikakat.jpeg": ["rikakat"],
    "http://localhost:8080/src/assets/images/sfihaObergine.jpeg": ["sfiha aubergine"],
    "http://localhost:8080/src/assets/images/fatayer.jpeg": ["fatayer"],
    "http://localhost:8080/src/assets/images/kebbe.jpeg": ["kebbé", "kebbe"],
    "http://localhost:8080/src/assets/images/sandpoulet.jpeg": ["chawarma poulet", "sandwich poulet"],
    "http://localhost:8080/src/assets/images/chBoeuf.jpeg": ["chawarma boeuf", "chawarma bœuf"],
    "http://localhost:8080/src/assets/images/pouletplat1.jpeg": ["poulet plat", "plat poulet"],
    "http://localhost:8080/src/assets/images/misschawarma.jpeg": ["miss chawarma plat"],
    "http://localhost:8080/src/assets/images/mix_viande_poulet.jpeg": ["mix'ta grill", "mix ta grill"],
    "http://localhost:8080/src/assets/images/Mrs falafel.jpeg": ["mrs falafel"],
    "http://localhost:8080/src/assets/images/baklawa.jpeg": ["baklawa pistache"],
    "http://localhost:8080/src/assets/images/mouhalabeya.jpeg": ["mouhalabiyé", "mouhalabiye"],
    "http://localhost:8080/src/assets/images/namoura.jpeg": ["namoura"],
    "http://localhost:8080/src/assets/images/citronade.jpeg": ["citronnade"],
    "https://i.ibb.co/jPGwZmgf/Chat-GPT-Image-Jun-4-2026-05-30-56-PM.png": ["kafta"],
    "https://i.ibb.co/B5rD1Vrv/Chat-GPT-Image-Jun-4-2026-05-25-42-PM.png": ["chichtaouk"],
    "https://i.ibb.co/x8tHwJPs/Chat-GPT-Image-Jun-8-2026-09-31-10-AM.png": ["mix grill"],
    "https://i.ibb.co/1fKj0j59/Chat-GPT-Image-Jun-8-2026-09-27-24-AM.png": ["lahmé", "lahme"],
    "https://i.ibb.co/yBQThLrV/Chat-GPT-Image-Jun-11-2026-12-59-41-AM.png": ["knefeh"],
    "https://i.ibb.co/4ZQSfrY4/Chat-GPT-Image-Jun-11-2026-12-53-57-AM.png": ["baklawa cajou"],
    "https://i.ibb.co/FqHHB6mb/Chat-GPT-Image-Jun-11-2026-01-01-00-AM.png": ["sfouf"],
    "https://i.ibb.co/gZ2N3rFG/Chat-GPT-Image-Jun-11-2026-11-15-37-AM.png": ["mezze royal"],
    "https://i.ibb.co/nNgZNQDk/Chat-GPT-Image-Jun-8-2026-09-50-49-AM.png": ["hamburger"],
    "https://i.ibb.co/cXJ0w76F/Chat-GPT-Image-Jun-11-2026-01-15-46-PM.png": ["fahita"],
    "https://i.ibb.co/WWjf69gL/Chat-GPT-Image-Jun-11-2026-01-29-00-PM.png": ["poulet crispy", "crispy"],
    "https://i.ibb.co/yFMKCGLb/Chat-GPT-Image-Jun-11-2026-11-03-28-AM.png": ["vege dream", "vegetarienne"],
    "https://i.ibb.co/xq69ZDD7/Chat-GPT-Image-Jun-8-2026-09-38-57-AM.png": ["foie volaille"],
    "https://i.ibb.co/Lz8bPZKR/Chat-GPT-Image-Jun-11-2026-12-29-14-AM.png": ["sodas", "coca"],
    "https://i.ibb.co/j9LPwQsC/Chat-GPT-Image-Jun-11-2026-12-47-28-AM.png": ["miss tea"],
    "https://i.ibb.co/Z1NYBfjG/Chat-GPT-Image-Jun-11-2026-12-13-48-AM.png": ["jus fruits rouges", "jus rouge"],
}

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def fuzzy_contains(text: str, keyword: str, threshold: float = 0.75) -> bool:
    """Vérifie si keyword apparaît dans text, même avec des fautes de frappe."""
    if keyword in text:
        return True
    words = text.split()
    kw_words = keyword.split()
    # Match mot par mot avec tolérance aux fautes
    if len(kw_words) == 1:
        return any(similar(w, keyword) > threshold for w in words)
    else:
        # Pour les expressions multi-mots, vérifie une fenêtre glissante
        n = len(kw_words)
        for i in range(len(words) - n + 1):
            window = " ".join(words[i:i+n])
            if similar(window, keyword) > threshold:
                return True
        return False

def detect_image(text: str):
    text_lower = text.lower()
    image_keywords = ["image", "photo", "voir", "montre", "affiche", "montrer", "pic", "photos"]
    
    has_image_intent = any(
        any(similar(w, kw) > 0.7 for w in text_lower.split())
        for kw in image_keywords
    )
    if not has_image_intent:
        return None

    best_match = None
    best_length = 0
    for url, keywords in IMAGE_MAP.items():
        for kw in keywords:
            if fuzzy_contains(text_lower, kw) and len(kw) > best_length:
                best_match = url
                best_length = len(kw)
    return best_match

@app.get("/")
def root():
    return {"status": "Miss Chawarma Chatbot API is running 🌿"}

@app.post("/chat")
def chat(request: ChatRequest):
    last_message = request.messages[-1].content if request.messages else ""
    print(f"MESSAGE RECU: {last_message}")
    image_url = detect_image(last_message)
    print(f"IMAGE DETECTEE: {image_url}")

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[{"role": m.role, "content": m.content} for m in request.messages],
    )
    reply = response.content[0].text

    if image_url:
        reply = f"[IMAGE:{image_url}]\n{reply}"

    return {"reply": reply}
