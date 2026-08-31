# admin.py — Interface d'administration SQLAdmin (/admin)
# Login/mot de passe définis dans .env : ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY

import json
import os
from urllib.parse import parse_qsl, urlencode
from sqladmin import Admin, ModelView, action
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse, HTMLResponse
from markupsafe import Markup, escape
from routers.menu import invalidate_menu_cache
from database import engine, SessionLocal
from models import (
    Category,
    Dish,
    Order,
    OrderItem,
    TableReservation,
    EventReservation,
    ContactMessage,
    Review,
    ReviewsSummary,
)
from admin_theme import AdminBrandMiddleware
from admin_dashboard import register_admin_dashboard_routes

ORDER_FILTER_PAGE_SIZE = 5000  # charge toutes les commandes pour les filtres UX
from notifications import (
    send_email,
    send_sms,
    table_reservation_confirmed,
    event_reservation_confirmed,
    contact_acknowledgement,
    table_issue_message,
    event_issue_message,
    issue_email_subject,
    contact_reply_default_message,
    contact_reply_subject,
)


# ─────────────── Correctif mobile : cartes Catégories compactes ───────────────

CATEGORY_COMPACT_CARDS_PATCH = r"""
<style id="mc-category-compact-cards-patch">
/* =========================================================
   CATÉGORIES — CARTES MOBILE COMPACTES
   S'applique uniquement à /admin/category/list.
   Les cartes Plats / Commandes / Réservations restent inchangées.
========================================================= */
@media(max-width:575.98px){

  .card.mc-category-card-mode .mc-mobile-cards{
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:9px!important;
    padding:10px 9px 16px!important;
    align-items:start!important;
  }

  .card.mc-category-card-mode .mc-mobile-record-card{
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.11)!important;
    border-radius:15px!important;
    background:linear-gradient(145deg,#fffefb 0%,#fbf9f2 100%)!important;
    box-shadow:0 6px 16px rgba(18,63,29,.055)!important;
  }

  /* Écrase la hauteur de 154px utilisée par les cartes génériques. */
  .card.mc-category-card-mode .mc-mobile-card-summary{
    position:relative!important;
    width:100%!important;
    min-height:110px!important;
    height:auto!important;
    padding:15px 12px 11px!important;
    display:block!important;
    background:transparent!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-main{
    width:100%!important;
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    padding:0 32px 29px 0!important;
    display:block!important;
    border:0!important;
    background:transparent!important;
    text-align:left!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-title{
    margin:0!important;
    color:#174623!important;
    font-size:13.5px!important;
    font-weight:900!important;
    line-height:1.24!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-subtitle{
    margin-top:6px!important;
    color:#818895!important;
    font-size:10px!important;
    font-weight:650!important;
    line-height:1.28!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  /* Ces éléments sont propres aux plats, donc aucun espace réservé ici. */
  .card.mc-category-card-mode .mc-mobile-card-quick,
  .card.mc-category-card-mode .mc-mobile-card-photo-wrap,
  .card.mc-category-card-mode .mc-mobile-state-dot{
    display:none!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-chevron{
    position:absolute!important;
    right:9px!important;
    bottom:9px!important;
    width:28px!important;
    min-width:28px!important;
    height:28px!important;
    min-height:28px!important;
    padding:0!important;
    display:grid!important;
    place-items:center!important;
    border:1px solid rgba(31,107,45,.09)!important;
    border-radius:9px!important;
    background:#edf4eb!important;
    color:#174623!important;
    font-size:14px!important;
    line-height:1!important;
  }

  .card.mc-category-card-mode
  .mc-mobile-record-card.mc-open
  .mc-mobile-card-chevron{
    color:#805500!important;
    background:#fff0c7!important;
  }

  /* Une catégorie ouverte utilise toute la largeur. */
  .card.mc-category-card-mode .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }

  .card.mc-category-card-mode
  .mc-mobile-record-card.mc-open
  .mc-mobile-card-summary{
    min-height:88px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-details{
    padding:0 12px 12px!important;
    border-top:1px solid rgba(31,107,45,.07)!important;
    background:linear-gradient(
      180deg,
      rgba(247,240,228,.20),
      rgba(255,255,255,0)
    )!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-grid{
    padding-top:8px!important;
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:6px!important;
  }

  .card.mc-category-card-mode .mc-mobile-detail-row{
    min-height:auto!important;
    padding:8px 9px!important;
    display:grid!important;
    grid-template-columns:90px minmax(0,1fr)!important;
    gap:9px!important;
    align-items:center!important;
    border:1px solid rgba(31,107,45,.065)!important;
    border-radius:10px!important;
    background:rgba(255,255,255,.75)!important;
  }

  .card.mc-category-card-mode .mc-mobile-detail-label{
    padding:0!important;
    color:#79847b!important;
    font-size:7.8px!important;
    font-weight:900!important;
    letter-spacing:.07em!important;
  }

  .card.mc-category-card-mode .mc-mobile-detail-value{
    color:#26362a!important;
    font-size:11px!important;
    line-height:1.35!important;
  }
}

@media(max-width:380px){
  .card.mc-category-card-mode .mc-mobile-cards{
    gap:7px!important;
    padding-left:7px!important;
    padding-right:7px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-summary{
    min-height:102px!important;
    padding:13px 10px 9px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-main{
    padding-right:29px!important;
    padding-bottom:27px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-title{
    font-size:12px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-subtitle{
    margin-top:5px!important;
    font-size:9px!important;
  }

  .card.mc-category-card-mode .mc-mobile-card-chevron{
    right:7px!important;
    bottom:7px!important;
    width:26px!important;
    min-width:26px!important;
    height:26px!important;
    min-height:26px!important;
  }
}
</style>

<script id="mc-category-compact-cards-script">
(function(){
  var categoryPath = '/admin/category/list';

  function isCategoryList(){
    return window.location.pathname.replace(/\/+$/,'') === categoryPath;
  }

  function applyCategoryCompactMode(){
    if (!isCategoryList()) return;

    document.querySelectorAll('.card.mc-mobile-card-mode').forEach(function(card){
      card.classList.add('mc-category-card-mode');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyCategoryCompactMode);
  } else {
    applyCategoryCompactMode();
  }

  /* Les cartes sont parfois reconstruites après une recherche instantanée.
     On réapplique donc simplement la classe au nouveau bloc. */
  var observerStarted = false;

  function startObserver(){
    if (observerStarted || !isCategoryList() || !document.body) return;
    observerStarted = true;

    var observer = new MutationObserver(function(){
      applyCategoryCompactMode();
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startObserver);
  } else {
    startObserver();
  }
})();
</script>
"""


class CategoryCompactCardsMiddleware:
    """Ajoute le correctif visuel des cartes Catégories sur mobile."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        path = scope.get("path", "")

        if (
            scope.get("type") != "http"
            or path.rstrip("/") != "/admin/category/list"
        ):
            await self.app(scope, receive, send)
            return

        response_start = None
        chunks = []

        async def capture_send(message):
            nonlocal response_start

            if message["type"] == "http.response.start":
                response_start = message
                return

            if message["type"] != "http.response.body":
                await send(message)
                return

            chunks.append(message.get("body", b""))

            if message.get("more_body", False):
                return

            body = b"".join(chunks)
            headers = (
                list(response_start.get("headers", []))
                if response_start
                else []
            )

            content_type = next(
                (
                    value.decode("latin-1").lower()
                    for key, value in headers
                    if key.lower() == b"content-type"
                ),
                "",
            )

            if "text/html" in content_type and b"</head>" in body:
                body = body.replace(
                    b"</head>",
                    CATEGORY_COMPACT_CARDS_PATCH.encode("utf-8") + b"</head>",
                    1,
                )

                headers = [
                    (key, value)
                    for key, value in headers
                    if key.lower() != b"content-length"
                ]
                headers.append(
                    (b"content-length", str(len(body)).encode("ascii"))
                )

            if response_start:
                response_start["headers"] = headers
                await send(response_start)

            await send({
                "type": "http.response.body",
                "body": body,
                "more_body": False,
            })

        await self.app(scope, receive, capture_send)



# ─────────────── Commandes : UX plus claire + filtres réception/paiement/état ───────────────

ORDER_UX_PATCH = r"""
<style id="mc-order-ux-patch">
/* =========================================================
   COMMANDES — UX + DESIGN SPÉCIFIQUE
   S'applique uniquement à /admin/order/list.
========================================================= */

.mc-order-desktop-filters,
.mc-order-mobile-filters{
  border:1px solid rgba(31,107,45,.10);
  border-radius:20px;
  background:
    radial-gradient(circle at 100% 0, rgba(228,184,63,.15), transparent 120px),
    linear-gradient(135deg,#f8fbf6,#fffaf0);
  box-shadow:0 10px 24px rgba(18,63,29,.05);
}

.mc-order-filter-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
}

.mc-order-filter-title{
  display:flex;
  align-items:center;
  gap:9px;
  color:var(--mc-dark);
  font-size:13px;
  font-weight:850;
}

.mc-order-filter-title::before{
  content:"⌘";
  width:30px;
  height:30px;
  display:grid;
  place-items:center;
  border-radius:10px;
  background:#edf4eb;
  color:var(--mc-green);
  font-family:Georgia,serif;
  font-size:18px;
}

.mc-order-filter-subtitle{
  margin-top:4px;
  color:#7a857d;
  font-size:11px;
  line-height:1.45;
}

.mc-order-filter-reset{
  min-height:42px!important;
  padding:0 15px!important;
  border:1px solid rgba(196,125,14,.18)!important;
  border-radius:13px!important;
  background:#fff7e7!important;
  color:#8f6200!important;
  font-size:11px!important;
  font-weight:850!important;
  white-space:nowrap;
}

.mc-order-filter-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:12px;
  margin-top:14px;
}

.mc-order-filter-field{
  display:grid;
  gap:6px;
  min-width:0;
}

.mc-order-filter-label{
  color:#728078;
  font-size:9px;
  font-weight:900;
  letter-spacing:.08em;
  text-transform:uppercase;
}

.mc-order-filter-select{
  width:100%;
  min-height:44px!important;
  padding:0 38px 0 13px!important;
  border:1px solid rgba(31,107,45,.15)!important;
  border-radius:13px!important;
  background:#fff!important;
  color:#24402a!important;
  font-size:12px!important;
  font-weight:750!important;
  box-shadow:none!important;
}

.mc-order-filter-select:focus{
  border-color:var(--mc-green)!important;
  box-shadow:0 0 0 4px rgba(31,107,45,.08)!important;
}

.mc-order-filter-result{
  margin-top:12px;
  color:#6f7c73;
  font-size:11px;
  font-weight:750;
}

.mc-order-empty-state{
  margin-top:14px;
  padding:28px 18px;
  border:1px dashed rgba(31,107,45,.16);
  border-radius:16px;
  background:rgba(255,255,255,.68);
  color:#78827b;
  text-align:center;
  font-size:12px;
}

/* SQLAdmin n’a plus besoin de pagination sur la page Commandes :
   toutes les commandes sont déjà chargées pour les filtres. */
.card.mc-order-ux-mode .card-footer{
  display:none!important;
}


/* ---------- Ticket cliquable : visible comme un reçu, pas comme un badge ---------- */
.mc-order-ux-mode .ticket-trigger,
.ticket-trigger.mc-ticket-trigger{
  position:relative!important;
  min-width:118px;
  min-height:52px;
  padding:8px 10px;
  display:inline-grid!important;
  grid-template-columns:30px minmax(0,1fr) 24px;
  align-items:center;
  gap:8px;
  overflow:visible!important;
  border:1px solid rgba(196,125,14,.27)!important;
  border-radius:12px!important;
  background:
    radial-gradient(circle at 0 50%, var(--mc-paper,#fffdf8) 0 5px, transparent 5.6px),
    radial-gradient(circle at 100% 50%, var(--mc-paper,#fffdf8) 0 5px, transparent 5.6px),
    linear-gradient(145deg,#fffdf8 0%,#fff9e9 100%)!important;
  color:#173f21!important;
  box-shadow:0 7px 18px rgba(18,63,29,.075)!important;
  text-decoration:none!important;
  white-space:nowrap!important;
  isolation:isolate;
  transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease!important;
}

.mc-order-ux-mode .ticket-trigger:hover,
.ticket-trigger.mc-ticket-trigger:hover{
  color:#173f21!important;
  border-color:rgba(196,125,14,.48)!important;
  box-shadow:0 11px 23px rgba(18,63,29,.12)!important;
  transform:translateY(-2px)!important;
}

.ticket-trigger.mc-ticket-trigger::after{
  content:"";
  position:absolute;
  left:38px;
  top:8px;
  bottom:8px;
  border-left:1px dashed rgba(196,125,14,.34);
  pointer-events:none;
}

.mc-ticket-receipt-icon{
  width:26px;
  height:30px;
  display:grid;
  place-items:center;
  color:#c58a00;
  font-size:22px;
  line-height:1;
}

.mc-ticket-copy{
  min-width:0;
  display:grid;
  gap:1px;
  text-align:left;
}

.mc-ticket-kicker{
  color:#927229;
  font-size:7px;
  font-weight:950;
  letter-spacing:.17em;
  line-height:1;
}

.mc-ticket-number{
  color:#174623;
  font-family:Georgia,"Times New Roman",serif;
  font-size:16px;
  font-weight:800;
  line-height:1.05;
}

.mc-ticket-open{
  width:23px;
  height:23px;
  display:grid;
  place-items:center;
  border:1px solid rgba(31,107,45,.12);
  border-radius:50%;
  background:rgba(255,255,255,.78);
  color:#1f6b2d;
  font-family:Arial,sans-serif;
  font-size:18px;
  font-weight:800;
  line-height:1;
}

/* petit trait perforé sous le ticket, comme un vrai talon */
.mc-order-ux-mode .mc-mobile-card-title{
  position:relative;
}

/* ---------- Desktop table toolbar ---------- */
@media(min-width:576px){
  .mc-order-desktop-filters{
    margin:18px 22px 16px;
    padding:18px;
  }

  .mc-order-desktop-table-row-hidden{
    display:none!important;
  }
}

/* ---------- Mobile order page ---------- */
@media(max-width:575.98px){
  .card.mc-order-ux-mode{
    border-radius:22px!important;
    overflow:hidden!important;
    background:
      linear-gradient(180deg,rgba(255,253,248,.98),rgba(250,247,238,.98))!important;
  }

  .card.mc-order-ux-mode .card-header{
    padding:16px 16px 13px!important;
    gap:8px!important;
    background:
      radial-gradient(circle at 95% 0,rgba(228,184,63,.18),transparent 120px),
      linear-gradient(120deg,#fffdf8,#fbf4e5)!important;
  }

  .card.mc-order-ux-mode .card-title{
    font-size:24px!important;
    line-height:1.1!important;
  }

  .card.mc-order-ux-mode .card-body{
    padding:12px!important;
    background:rgba(255,253,248,.92)!important;
    border-bottom:1px solid rgba(31,107,45,.08);
  }

  .card.mc-order-ux-mode .card-body form{
    position:relative!important;
    display:grid!important;
    grid-template-columns:1fr auto auto!important;
    gap:8px!important;
    align-items:center!important;
  }

  .card.mc-order-ux-mode .card-body form::before{
    content:"⌕";
    position:absolute;
    left:15px;
    top:13px;
    z-index:2;
    color:#4f7057;
    font-family:Georgia,serif;
    font-size:24px;
    line-height:1;
    pointer-events:none;
  }

  .card.mc-order-ux-mode input[name="search"]{
    grid-column:1 / -1!important;
    width:100%!important;
    min-height:50px!important;
    padding:0 44px 0 43px!important;
    border:1px solid rgba(31,107,45,.15)!important;
    border-radius:16px!important;
    background:linear-gradient(180deg,#fff,#fffdf8)!important;
    box-shadow:0 7px 18px rgba(18,63,29,.055)!important;
    color:#1e3825!important;
    font-size:15px!important;
  }

  .card.mc-order-ux-mode input[name="search"]:focus{
    border-color:rgba(31,107,45,.42)!important;
    box-shadow:
      0 0 0 4px rgba(31,107,45,.085),
      0 9px 20px rgba(18,63,29,.07)!important;
  }

  .card.mc-order-ux-mode .card-body form button[type="submit"],
  .card.mc-order-ux-mode .card-body form input[type="submit"]{
    display:none!important;
  }

  .card.mc-order-ux-mode .card-body form .dropdown .btn,
  .card.mc-order-ux-mode .card-body form .btn-group .btn,
  .card.mc-order-ux-mode .card-body form > .btn{
    min-height:42px!important;
    padding:0 14px!important;
    border-radius:13px!important;
    background:#f5f7f3!important;
    border:1px solid rgba(31,107,45,.09)!important;
    color:#243126!important;
    font-size:11px!important;
    font-weight:800!important;
    box-shadow:none!important;
  }

  .card.mc-order-ux-mode .mc-mobile-cards{
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:12px!important;
    padding:12px 10px 18px!important;
    align-items:start!important;
  }

  .mc-order-mobile-filters{
    grid-column:1 / -1!important;
    padding:12px;
    margin-bottom:2px;
    border-radius:18px;
  }

  .mc-order-mobile-filters .mc-order-filter-title{
    font-size:12px;
  }

  .mc-order-mobile-filters .mc-order-filter-subtitle{
    font-size:10px;
  }

  .mc-order-mobile-filters .mc-order-filter-grid{
    grid-template-columns:1fr 1fr;
    gap:8px;
    margin-top:12px;
  }

  .mc-order-mobile-filters .mc-order-filter-field:nth-child(3){
    grid-column:1 / -1;
  }

  .mc-order-mobile-filters .mc-order-filter-select{
    min-height:39px!important;
    font-size:10.5px!important;
    border-radius:11px!important;
  }

  .mc-order-mobile-filters .mc-order-filter-reset{
    min-height:34px!important;
    padding:0 10px!important;
    font-size:9px!important;
    border-radius:10px!important;
  }

  .mc-order-mobile-filters .mc-order-filter-result{
    font-size:9px;
    margin-top:9px;
  }

  .card.mc-order-ux-mode .mc-mobile-record-card{
    min-width:0!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.12)!important;
    border-radius:20px!important;
    background:
      radial-gradient(circle at 104% -4%,rgba(228,184,63,.12),transparent 88px),
      linear-gradient(145deg,#fffefb 0%,#fcfaf4 100%)!important;
    box-shadow:
      0 10px 24px rgba(18,63,29,.065),
      inset 0 1px 0 rgba(255,255,255,.8)!important;
    transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease!important;
  }

  .card.mc-order-ux-mode .mc-mobile-record-card:active{
    transform:scale(.995)!important;
  }

  .card.mc-order-ux-mode .mc-mobile-record-card::before{
    content:"";
    position:absolute;
    left:0;
    top:0;
    bottom:0;
    width:3px;
    opacity:1;
    background:linear-gradient(180deg,var(--mc-green),var(--mc-gold));
  }

  .card.mc-order-ux-mode .mc-mobile-card-summary{
    position:relative!important;
    min-height:0!important;
    height:auto!important;
    padding:15px 13px 13px!important;
    display:block!important;
    background:transparent!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-main{
    width:100%!important;
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    /* Le bouton ⋮ est en bas : on garde uniquement l'espace vertical.
       Ainsi TOTAL + CRÉNEAU utilisent toute la largeur de la carte. */
    padding:0 0 38px 0!important;
    display:block!important;
    border:0!important;
    background:transparent!important;
    text-align:left!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title{
    width:100%!important;
    max-width:100%!important;
    min-height:0!important;
    margin:0 0 9px!important;
    padding:0!important;
    display:block!important;
    overflow:visible!important;
    border:0!important;
    border-radius:0!important;
    background:transparent!important;
    box-shadow:none!important;
    color:inherit!important;
    white-space:normal!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title::after{
    content:"";
    display:block;
    width:100%;
    margin-top:10px;
    border-bottom:1px dashed rgba(196,125,14,.28);
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .ticket-trigger{
    width:100%!important;
    min-width:0!important;
    min-height:62px!important;
    padding:9px 9px!important;
    grid-template-columns:34px minmax(0,1fr) 27px!important;
    gap:9px!important;
    border-radius:14px!important;
    box-shadow:0 8px 18px rgba(18,63,29,.075)!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .ticket-trigger::after{
    left:43px!important;
    top:9px!important;
    bottom:9px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .mc-ticket-receipt-icon{
    width:30px!important;
    height:34px!important;
    font-size:25px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .mc-ticket-kicker{
    font-size:7px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .mc-ticket-number{
    font-size:21px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .mc-ticket-open{
    width:27px!important;
    height:27px!important;
    font-size:20px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-subtitle{
    margin-top:10px!important;
    color:#707989!important;
    font-size:10.2px!important;
    font-weight:750!important;
    line-height:1.38!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  /* Résumé commande : hiérarchie claire et cartes plus légères. */
  .mc-order-card-shell{
    margin-top:12px;
    display:grid;
    gap:11px;
  }

  .mc-order-card-chips{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:6px;
  }

  .mc-order-chip{
    min-height:25px;
    max-width:100%;
    padding:0 10px;
    display:inline-flex;
    align-items:center;
    overflow:hidden;
    border-radius:999px;
    font-size:8.5px;
    font-weight:900;
    letter-spacing:.01em;
    line-height:1;
    text-overflow:ellipsis;
    white-space:nowrap;
  }

  .mc-order-chip.mc-reception{
    color:#246735;
    background:linear-gradient(180deg,#f1f9ef,#e8f5e6);
    border:1px solid rgba(47,132,59,.15);
  }

  .mc-order-chip.mc-payment{
    color:#8b6200;
    background:linear-gradient(180deg,#fff8df,#fff0c5);
    border:1px solid rgba(211,154,0,.18);
  }

  .mc-order-chip.mc-status-green{
    color:#1f6b2d;
    background:#e9f5eb;
    border:1px solid rgba(31,107,45,.12);
  }

  .mc-order-chip.mc-status-yellow{
    color:#9b6b00;
    background:#fff1ca;
    border:1px solid rgba(196,125,14,.18);
  }

  .mc-order-chip.mc-status-red{
    color:#a0362d;
    background:#fff0ee;
    border:1px solid rgba(198,63,53,.18);
  }

  /* TOTAL + CRÉNEAU : une seule ligne pleine largeur, sans petits carreaux.
     Le contenu respire davantage et les montants longs (ex. 26,70 €)
     restent entièrement visibles. */
  .mc-order-card-metrics{
    width:100%!important;
    display:grid;
    grid-template-columns:minmax(0,.88fr) minmax(0,1.12fr);
    gap:0;
    align-items:stretch;
    margin-top:2px;
    padding:11px 0 10px;
    border-top:1px solid rgba(31,107,45,.10);
    border-bottom:1px solid rgba(31,107,45,.10);
    background:transparent;
  }

  .mc-order-card-metric{
    min-width:0;
    min-height:58px;
    padding:2px 11px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    border:0!important;
    border-radius:0!important;
    background:transparent!important;
    box-shadow:none!important;
  }

  .mc-order-total-box{
    overflow:visible!important;
    padding-left:2px!important;
    padding-right:10px!important;
  }

  .mc-order-slot-box{
    padding-left:13px!important;
    border-left:1px solid rgba(31,107,45,.11)!important;
  }

  .mc-order-card-metric-label{
    color:#7b857d;
    font-size:7.4px;
    font-weight:900;
    letter-spacing:.10em;
    text-transform:uppercase;
  }

  .mc-order-card-metric-value{
    margin-top:6px;
    min-width:0;
    color:#1b4424;
    font-size:10.5px;
    font-weight:850;
    line-height:1.22;
  }

  .mc-order-total-box .mc-order-card-metric-value.mc-total{
    width:100%!important;
    max-width:none!important;
    min-width:0!important;
    overflow:visible!important;
    color:#ba7c00!important;
    font-size:clamp(14px,3.1vw,18px)!important;
    font-weight:950!important;
    line-height:1!important;
    letter-spacing:-.035em!important;
    white-space:nowrap!important;
    text-overflow:unset!important;
  }

  .mc-order-slot{
    min-width:0;
    display:grid;
    grid-template-columns:1fr;
    align-items:start;
    gap:4px;
  }

  .mc-order-slot-date{
    min-width:0;
    color:#576377;
    font-size:9.2px;
    font-weight:750;
    white-space:nowrap;
  }

  .mc-order-slot-time{
    color:#246735;
    font-size:11.8px;
    font-weight:950;
    white-space:nowrap;
  }

  .mc-order-card-destination{
    padding:0 2px;
    color:#7a827f;
    font-size:9px;
    line-height:1.35;
  }

  .mc-order-card-destination strong{
    color:#57625a;
    font-weight:850;
  }

  .card.mc-order-ux-mode .mc-mobile-card-chevron{
    position:absolute!important;
    right:9px!important;
    bottom:9px!important;
    width:29px!important;
    min-width:29px!important;
    height:29px!important;
    min-height:29px!important;
    display:grid!important;
    place-items:center!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:10px!important;
    background:#edf4eb!important;
    color:#174623!important;
    font-size:14px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }

  .card.mc-order-ux-mode .mc-mobile-record-card.mc-open .mc-mobile-card-summary{
    min-height:0!important;
    height:auto!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-details{
    padding:0 13px 14px!important;
    border-top:1px solid rgba(31,107,45,.07)!important;
    background:linear-gradient(180deg,rgba(247,240,228,.22),rgba(255,255,255,0))!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-grid{
    padding-top:6px!important;
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:7px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-detail-row{
    min-height:auto!important;
    padding:9px 10px!important;
    display:grid!important;
    grid-template-columns:86px minmax(0,1fr)!important;
    gap:10px!important;
    align-items:center!important;
    border:1px solid rgba(31,107,45,.065)!important;
    border-radius:11px!important;
    background:rgba(255,255,255,.78)!important;
  }

  .card.mc-order-ux-mode .mc-mobile-detail-label{
    color:#79847b!important;
    font-size:7.7px!important;
    font-weight:900!important;
    letter-spacing:.08em!important;
  }

  .card.mc-order-ux-mode .mc-mobile-detail-value{
    color:#26362a!important;
    font-size:11.2px!important;
    line-height:1.42!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-actions{
    margin-top:9px!important;
    padding-top:10px!important;
    gap:8px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-actions a,
  .card.mc-order-ux-mode .mc-mobile-card-actions button{
    width:36px!important;
    min-width:36px!important;
    height:36px!important;
    min-height:36px!important;
    border-radius:10px!important;
    box-shadow:none!important;
  }

  .mc-order-filter-hidden{
    display:none!important;
  }

  .mc-order-empty-state{
    grid-column:1 / -1!important;
    margin-top:0;
    font-size:11px;
    padding:20px 14px;
  }
}

@media(max-width:380px){
  .card.mc-order-ux-mode .mc-mobile-cards{
    gap:9px!important;
    padding-left:8px!important;
    padding-right:8px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-summary{
    min-height:0!important;
    height:auto!important;
    padding:13px 10px 10px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-main{
    padding-right:0!important;
    padding-bottom:36px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .mc-ticket-number{
    font-size:18px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-title .ticket-trigger{
    min-height:58px!important;
    grid-template-columns:31px minmax(0,1fr) 25px!important;
    gap:7px!important;
  }

  .card.mc-order-ux-mode .mc-mobile-card-subtitle{
    margin-top:9px!important;
    font-size:10px!important;
  }

  .mc-order-total-box .mc-order-card-metric-value.mc-total{
    font-size:13.5px!important;
  }
}
</style>

<script id="mc-order-ux-script">
(function(){
  var ORDER_PATH = '/admin/order/list';
  var observerStarted = false;
  var scheduled = false;

  function currentLang(){
    return localStorage.getItem('mc_admin_lang') || 'fr';
  }

  var I18N = {
    fr: {
      filterTitle: 'Filtres rapides',
      filterSubtitle: 'Repérez vite les commandes par état, paiement et réception.',
      reception: 'Réception',
      payment: 'Paiement',
      status: 'État',
      allReception: 'Toutes les réceptions',
      allPayment: 'Tous les paiements',
      allStatus: 'Tous les états',
      reset: 'Réinitialiser',
      shownZero: 'Aucune commande affichée',
      shownOne: '1 commande affichée',
      shownMany: '__count__ commandes affichées',
      noResult: 'Aucune commande ne correspond à ces filtres.',
      total: 'Total',
      slot: 'Créneau',
      destination: 'Destination'
    },
    en: {
      filterTitle: 'Quick filters',
      filterSubtitle: 'Spot orders faster by status, payment and reception.',
      reception: 'Method',
      payment: 'Payment',
      status: 'Status',
      allReception: 'All methods',
      allPayment: 'All payments',
      allStatus: 'All statuses',
      reset: 'Reset',
      shownZero: 'No orders shown',
      shownOne: '1 order shown',
      shownMany: '__count__ orders shown',
      noResult: 'No order matches these filters.',
      total: 'Total',
      slot: 'Time slot',
      destination: 'Destination'
    }
  };

  function t(key){
    var lang = currentLang();
    return (I18N[lang] && I18N[lang][key]) || I18N.fr[key] || key;
  }

  function isOrderList(){
    return window.location.pathname.replace(/\/+$/,'') === ORDER_PATH;
  }

  function clean(value){
    return (value || '').toString().replace(/\s+/g,' ').trim();
  }

  function norm(value){
    return clean(value).toLowerCase();
  }

  function escapeHtml(value){
    var div = document.createElement('div');
    div.textContent = value == null ? '' : String(value);
    return div.innerHTML;
  }

  function prettyCount(count){
    if (count === 0) return t('shownZero');
    if (count === 1) return t('shownOne');
    return t('shownMany').replace('__count__', String(count));
  }

  function matchesLabel(label, variants){
    var n = norm(label);
    return variants.indexOf(n) !== -1;
  }

  function statusTone(value){
    var v = norm(value);
    if (
      v.indexOf('annul') !== -1 || v.indexOf('cancel') !== -1 ||
      v.indexOf('échou') !== -1 || v.indexOf('failed') !== -1 ||
      v.indexOf('probl') !== -1 || v.indexOf('issue') !== -1
    ) return 'red';

    if (
      v.indexOf('confirm') !== -1 || v.indexOf('livr') !== -1 ||
      v.indexOf('delivered') !== -1 || v.indexOf('payé') !== -1 ||
      v.indexOf('paid') !== -1 || v.indexOf('prête') !== -1 ||
      v.indexOf('ready') !== -1
    ) return 'green';

    return 'yellow';
  }

  function getOrderDataFromCard(record){
    var data = {
      client: '',
      reception: '',
      payment: '',
      status: '',
      total: '',
      slot: '',
      destination: ''
    };

    var subtitle = record.querySelector('.mc-mobile-card-subtitle');
    if (subtitle) data.client = clean(subtitle.textContent);

    Array.prototype.slice.call(
      record.querySelectorAll('.mc-mobile-detail-row')
    ).forEach(function(row){
      var labelEl = row.querySelector('.mc-mobile-detail-label');
      var valueEl = row.querySelector('.mc-mobile-detail-value');
      if (!labelEl || !valueEl) return;

      var label = clean(labelEl.textContent);
      var value = clean(valueEl.textContent);

      if (!data.client && matchesLabel(label, ['client','customer'])) data.client = value;
      else if (matchesLabel(label, ['réception','reception','method'])) data.reception = value;
      else if (matchesLabel(label, ['paiement','payment'])) data.payment = value;
      else if (matchesLabel(label, ['état','etat','statut','status'])) data.status = value;
      else if (matchesLabel(label, ['total'])) data.total = value;
      else if (matchesLabel(label, ['créneau','creneau','time slot'])) data.slot = value;
      else if (matchesLabel(label, ['destination'])) data.destination = value;
    });

    return data;
  }

  function buildChip(value, cssClass){
    if (!clean(value)) return '';
    return '<span class="mc-order-chip ' + cssClass + '">' + escapeHtml(value) + '</span>';
  }

  function isDefaultNewStatus(value){
    var v = norm(value);
    return v === 'nouvelle' || v === 'new';
  }

  function prettyPayment(value){
    var v = clean(value);
    if (!v) return '';
    return v
      .replace(/(En attente|Payé|Échoué)(Carte|Sur place)/i, '$1 · $2')
      .replace(/(Pending|Paid|Failed)(Card|On site)/i, '$1 · $2')
      .replace(/\s*·\s*/g, ' · ');
  }

  function splitOrderSlot(value){
    var raw = clean(value).replace(/^📅\s*/, '');
    var match = raw.match(/^(\d{4}-\d{2}-\d{2})\s*(\d{1,2}:\d{2})?$/);

    if (match) {
      return {date: match[1], time: match[2] || ''};
    }

    var timeMatch = raw.match(/(\d{1,2}:\d{2})$/);
    if (timeMatch) {
      return {
        date: clean(raw.slice(0, timeMatch.index)),
        time: timeMatch[1]
      };
    }

    return {date: raw || '—', time: ''};
  }

  function enhanceOrderCards(){
    if (!isOrderList() || window.innerWidth > 575.98) return;

    var card = document.querySelector('.card.mc-mobile-card-mode');
    if (!card) return;

    card.classList.add('mc-order-ux-mode');

    Array.prototype.slice.call(
      card.querySelectorAll('.mc-mobile-record-card')
    ).forEach(function(record){
      if (record.dataset.mcOrderEnhanced === '1') return;

      var data = getOrderDataFromCard(record);

      var paymentLabel = prettyPayment(data.payment);

      record.dataset.mcOrderReception = norm(data.reception);
      record.dataset.mcOrderPayment = norm(paymentLabel);
      record.dataset.mcOrderStatus = norm(data.status);
      record.dataset.mcOrderReceptionLabel = data.reception;
      record.dataset.mcOrderPaymentLabel = paymentLabel;
      record.dataset.mcOrderStatusLabel = data.status;

      var main = record.querySelector('.mc-mobile-card-main');
      if (!main) return;

      /* Le ticket est un vrai contrôle interactif. On le sort du bouton
         générique qui ouvre les détails afin d'éviter un lien imbriqué
         dans un <button> et de rendre le clic sur le reçu indépendant. */
      var ticketTitle = main.querySelector('.mc-mobile-card-title');
      if (
        ticketTitle &&
        ticketTitle.querySelector('.ticket-trigger') &&
        main.parentNode
      ) {
        main.parentNode.insertBefore(ticketTitle, main);
      }

      var shell = document.createElement('div');
      shell.className = 'mc-order-card-shell';

      /* Le texte "Nouvelle" est volontairement masqué :
         le point jaune en haut de la carte suffit pour cet état par défaut. */
      var statusChip = isDefaultNewStatus(data.status)
        ? ''
        : buildChip(data.status, 'mc-status-' + statusTone(data.status));

      var chipsHtml =
        '<div class="mc-order-card-chips">' +
          buildChip(data.reception, 'mc-reception') +
          buildChip(paymentLabel, 'mc-payment') +
          statusChip +
        '</div>';

      var slot = splitOrderSlot(data.slot);

      var metricsHtml =
        '<div class="mc-order-card-metrics">' +
          '<div class="mc-order-card-metric mc-order-total-box">' +
            '<div class="mc-order-card-metric-label">' + escapeHtml(t('total')) + '</div>' +
            '<div class="mc-order-card-metric-value mc-total">' + escapeHtml(data.total || '—') + '</div>' +
          '</div>' +
          '<div class="mc-order-card-metric mc-order-slot-box">' +
            '<div class="mc-order-card-metric-label">' + escapeHtml(t('slot')) + '</div>' +
            '<div class="mc-order-card-metric-value mc-order-slot">' +
              '<span class="mc-order-slot-date">📅 ' + escapeHtml(slot.date || '—') + '</span>' +
              (slot.time ? '<span class="mc-order-slot-time">' + escapeHtml(slot.time) + '</span>' : '') +
            '</div>' +
          '</div>' +
        '</div>';

      var destinationHtml = '';
      var destination = clean(data.destination);
      var receptionNorm = norm(data.reception);
      var redundantPickupDestination =
        (receptionNorm.indexOf('emporter') !== -1 || receptionNorm.indexOf('pickup') !== -1) &&
        (norm(destination).indexOf('retrait au restaurant') !== -1 ||
         norm(destination).indexOf('pickup at restaurant') !== -1);

      if (destination && !redundantPickupDestination) {
        destinationHtml =
          '<div class="mc-order-card-destination"><strong>' +
          escapeHtml(t('destination')) + ':</strong> ' +
          escapeHtml(destination) +
          '</div>';
      }

      shell.innerHTML = chipsHtml + metricsHtml + destinationHtml;
      main.appendChild(shell);
      record.dataset.mcOrderEnhanced = '1';
    });
  }

  function buildOptionList(records, datasetLabelKey, datasetValueKey, allLabel){
    var map = {};
    records.forEach(function(record){
      var value = clean(record.dataset[datasetValueKey] || '');
      var label = clean(record.dataset[datasetLabelKey] || '');
      if (!value || !label) return;
      map[value] = label;
    });

    var keys = Object.keys(map).sort(function(a,b){
      return map[a].localeCompare(map[b], 'fr', {sensitivity:'base'});
    });

    return '<option value="">' + escapeHtml(allLabel) + '</option>' +
      keys.map(function(key){
        return '<option value="' + escapeHtml(key) + '">' +
          escapeHtml(map[key]) +
        '</option>';
      }).join('');
  }

  function initOrderMobileFilters(){
    if (!isOrderList() || window.innerWidth > 575.98) return;

    var card = document.querySelector('.card.mc-mobile-card-mode');
    if (!card) return;

    card.classList.add('mc-order-ux-mode');

    var wrap = card.querySelector('.mc-mobile-cards');
    if (!wrap) return;

    var records = Array.prototype.slice.call(
      wrap.querySelectorAll('.mc-mobile-record-card')
    );
    if (!records.length) return;

    var signature = records.length + '|' + records.map(function(record){
      var title = record.querySelector('.mc-mobile-card-title');
      return clean(title ? title.textContent : '');
    }).join('|');

    if (
      wrap.dataset.mcOrderFilterSignature === signature &&
      wrap.querySelector('.mc-order-mobile-filters')
    ) return;

    var oldFilter = wrap.querySelector('.mc-order-mobile-filters');
    if (oldFilter) oldFilter.remove();

    var oldEmpty = wrap.querySelector('.mc-order-empty-state');
    if (oldEmpty) oldEmpty.remove();

    var filter = document.createElement('section');
    filter.className = 'mc-order-mobile-filters';
    filter.innerHTML =
      '<div class="mc-order-filter-head">' +
        '<div>' +
          '<div class="mc-order-filter-title">' + escapeHtml(t('filterTitle')) + '</div>' +
          '<div class="mc-order-filter-subtitle">' + escapeHtml(t('filterSubtitle')) + '</div>' +
        '</div>' +
        '<button type="button" class="mc-order-filter-reset">' + escapeHtml(t('reset')) + '</button>' +
      '</div>' +
      '<div class="mc-order-filter-grid">' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('reception')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="reception">' +
            buildOptionList(records, 'mcOrderReceptionLabel', 'mcOrderReception', t('allReception')) +
          '</select>' +
        '</label>' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('payment')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="payment">' +
            buildOptionList(records, 'mcOrderPaymentLabel', 'mcOrderPayment', t('allPayment')) +
          '</select>' +
        '</label>' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('status')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="status">' +
            buildOptionList(records, 'mcOrderStatusLabel', 'mcOrderStatus', t('allStatus')) +
          '</select>' +
        '</label>' +
      '</div>' +
      '<div class="mc-order-filter-result"></div>';

    var empty = document.createElement('div');
    empty.className = 'mc-order-empty-state';
    empty.textContent = t('noResult');
    empty.style.display = 'none';

    wrap.insertBefore(filter, records[0]);
    wrap.appendChild(empty);

    var reception = filter.querySelector('[data-order-filter="reception"]');
    var payment = filter.querySelector('[data-order-filter="payment"]');
    var status = filter.querySelector('[data-order-filter="status"]');
    var reset = filter.querySelector('.mc-order-filter-reset');
    var result = filter.querySelector('.mc-order-filter-result');

    function apply(){
      var wantedReception = clean(reception.value);
      var wantedPayment = clean(payment.value);
      var wantedStatus = clean(status.value);

      var visible = 0;

      records.forEach(function(record){
        var show =
          (!wantedReception || clean(record.dataset.mcOrderReception) === wantedReception) &&
          (!wantedPayment || clean(record.dataset.mcOrderPayment) === wantedPayment) &&
          (!wantedStatus || clean(record.dataset.mcOrderStatus) === wantedStatus);

        record.classList.toggle('mc-order-filter-hidden', !show);
        if (show) visible += 1;
      });

      result.textContent = prettyCount(visible);
      empty.style.display = visible === 0 ? 'block' : 'none';
    }

    reception.addEventListener('change', apply);
    payment.addEventListener('change', apply);
    status.addEventListener('change', apply);

    reset.addEventListener('click', function(){
      reception.value = '';
      payment.value = '';
      status.value = '';
      apply();
    });

    wrap.dataset.mcOrderFilterSignature = signature;
    apply();
  }

  function getHeaderIndexMap(table){
    var map = {};
    Array.prototype.slice.call(table.querySelectorAll('thead th')).forEach(function(th, index){
      var label = norm(th.textContent);
      if (!label) return;
      map[label] = index;
    });
    return map;
  }

  function findIndex(map, variants){
    for (var i = 0; i < variants.length; i++) {
      if (map.hasOwnProperty(variants[i])) return map[variants[i]];
    }
    return -1;
  }

  function initOrderDesktopFilters(){
    if (!isOrderList() || window.innerWidth <= 575.98) return;

    var card = document.querySelector('.card');
    if (!card) return;

    var tableResponsive = card.querySelector('.table-responsive');
    var table = tableResponsive ? tableResponsive.querySelector('table') : null;
    if (!table) return;

    var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    if (!rows.length) return;

    var signature = rows.length + '|' + rows.map(function(row){
      return clean(row.textContent).slice(0, 120);
    }).join('|');

    if (
      card.dataset.mcOrderDesktopSignature === signature &&
      card.querySelector('.mc-order-desktop-filters')
    ) return;

    Array.prototype.slice.call(card.querySelectorAll('.mc-order-desktop-filters,.mc-order-empty-state')).forEach(function(el){
      el.remove();
    });

    var headerMap = getHeaderIndexMap(table);
    var receptionIndex = findIndex(headerMap, ['réception','reception','method']);
    var paymentIndex = findIndex(headerMap, ['paiement','payment']);
    var statusIndex = findIndex(headerMap, ['état','etat','statut','status']);

    if (receptionIndex < 0 && paymentIndex < 0 && statusIndex < 0) return;

    var rowData = rows.map(function(row){
      var cells = row.children;
      var reception = receptionIndex >= 0 && cells[receptionIndex] ? clean(cells[receptionIndex].textContent) : '';
      var payment = paymentIndex >= 0 && cells[paymentIndex] ? clean(cells[paymentIndex].textContent) : '';
      var status = statusIndex >= 0 && cells[statusIndex] ? clean(cells[statusIndex].textContent) : '';
      return {
        row: row,
        reception: reception,
        payment: payment,
        status: status
      };
    });

    function buildDesktopOptions(key, allLabel){
      var map = {};
      rowData.forEach(function(item){
        var value = clean(item[key]);
        if (!value) return;
        map[norm(value)] = value;
      });

      var keys = Object.keys(map).sort(function(a,b){
        return map[a].localeCompare(map[b], 'fr', {sensitivity:'base'});
      });

      return '<option value="">' + escapeHtml(allLabel) + '</option>' +
        keys.map(function(key){
          return '<option value="' + escapeHtml(key) + '">' + escapeHtml(map[key]) + '</option>';
        }).join('');
    }

    var panel = document.createElement('section');
    panel.className = 'mc-order-desktop-filters';
    panel.innerHTML =
      '<div class="mc-order-filter-head">' +
        '<div>' +
          '<div class="mc-order-filter-title">' + escapeHtml(t('filterTitle')) + '</div>' +
          '<div class="mc-order-filter-subtitle">' + escapeHtml(t('filterSubtitle')) + '</div>' +
        '</div>' +
        '<button type="button" class="mc-order-filter-reset">' + escapeHtml(t('reset')) + '</button>' +
      '</div>' +
      '<div class="mc-order-filter-grid">' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('reception')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="reception">' +
            buildDesktopOptions('reception', t('allReception')) +
          '</select>' +
        '</label>' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('payment')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="payment">' +
            buildDesktopOptions('payment', t('allPayment')) +
          '</select>' +
        '</label>' +
        '<label class="mc-order-filter-field">' +
          '<span class="mc-order-filter-label">' + escapeHtml(t('status')) + '</span>' +
          '<select class="mc-order-filter-select" data-order-filter="status">' +
            buildDesktopOptions('status', t('allStatus')) +
          '</select>' +
        '</label>' +
      '</div>' +
      '<div class="mc-order-filter-result"></div>';

    var empty = document.createElement('div');
    empty.className = 'mc-order-empty-state';
    empty.textContent = t('noResult');
    empty.style.display = 'none';

    tableResponsive.insertAdjacentElement('beforebegin', panel);
    tableResponsive.insertAdjacentElement('afterend', empty);

    var reception = panel.querySelector('[data-order-filter="reception"]');
    var payment = panel.querySelector('[data-order-filter="payment"]');
    var status = panel.querySelector('[data-order-filter="status"]');
    var reset = panel.querySelector('.mc-order-filter-reset');
    var result = panel.querySelector('.mc-order-filter-result');

    function apply(){
      var wantedReception = clean(reception.value);
      var wantedPayment = clean(payment.value);
      var wantedStatus = clean(status.value);

      var visible = 0;

      rowData.forEach(function(item){
        var show =
          (!wantedReception || norm(item.reception) === wantedReception) &&
          (!wantedPayment || norm(item.payment) === wantedPayment) &&
          (!wantedStatus || norm(item.status) === wantedStatus);

        item.row.classList.toggle('mc-order-desktop-table-row-hidden', !show);
        if (show) visible += 1;
      });

      result.textContent = prettyCount(visible);
      empty.style.display = visible === 0 ? 'block' : 'none';
    }

    reception.addEventListener('change', apply);
    payment.addEventListener('change', apply);
    status.addEventListener('change', apply);

    reset.addEventListener('click', function(){
      reception.value = '';
      payment.value = '';
      status.value = '';
      apply();
    });

    card.dataset.mcOrderDesktopSignature = signature;
    apply();
  }

  function run(){
    if (!isOrderList()) return;

    /* Active le mode Commandes sur mobile ET desktop.
       Cela masque aussi la pagination native, devenue inutile puisque
       le serveur renvoie toutes les commandes en une seule fois. */
    var orderCard = document.querySelector('.card');
    if (orderCard) orderCard.classList.add('mc-order-ux-mode');

    enhanceOrderCards();
    initOrderMobileFilters();
    initOrderDesktopFilters();
  }

  function scheduleRun(){
    if (scheduled) return;
    scheduled = true;
    window.requestAnimationFrame(function(){
      scheduled = false;
      run();
    });
  }

  function startObserver(){
    if (observerStarted || !document.body || !isOrderList()) return;
    observerStarted = true;

    var observer = new MutationObserver(function(){
      scheduleRun();
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function(){
      scheduleRun();
      startObserver();
    });
  } else {
    scheduleRun();
    startObserver();
  }

  window.addEventListener('resize', scheduleRun);
})();
</script>
"""


class OrderUXMiddleware:
    """Injecte l'amélioration UX spécifique à la liste des commandes."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        path = scope.get("path", "")

        if (
            scope.get("type") != "http"
            or path.rstrip("/") != "/admin/order/list"
        ):
            await self.app(scope, receive, send)
            return

        # IMPORTANT : le filtre UX lit les lignes présentes dans le DOM.
        # SQLAdmin pagine normalement la liste, donc un filtre JavaScript ne
        # peut voir que la page courante. On force ici une seule grande page
        # côté serveur, sans rechargement supplémentaire dans le navigateur.
        forward_scope = dict(scope)

        # Taille réellement dynamique : on compte les commandes présentes
        # en base afin de ne pas dépendre d'une limite fixe (20, 100, 5000…).
        # Ainsi les filtres travaillent bien sur TOUTES les commandes.
        db = SessionLocal()
        try:
            all_orders_page_size = max(db.query(Order.id).count(), 1)
        except Exception:
            # Fallback de sécurité si le count échoue exceptionnellement.
            all_orders_page_size = ORDER_FILTER_PAGE_SIZE
        finally:
            db.close()

        raw_query = scope.get("query_string", b"").decode("latin-1")
        query_items = parse_qsl(raw_query, keep_blank_values=True)
        query_items = [
            (key, value)
            for key, value in query_items
            if key not in {"page", "pageSize", "page_size"}
        ]
        query_items.extend([
            ("pageSize", str(all_orders_page_size)),
            ("page", "1"),
        ])
        forward_scope["query_string"] = urlencode(query_items).encode("latin-1")

        response_start = None
        chunks = []

        async def capture_send(message):
            nonlocal response_start

            if message["type"] == "http.response.start":
                response_start = message
                return

            if message["type"] != "http.response.body":
                await send(message)
                return

            chunks.append(message.get("body", b""))

            if message.get("more_body", False):
                return

            body = b"".join(chunks)
            headers = (
                list(response_start.get("headers", []))
                if response_start
                else []
            )

            content_type = next(
                (
                    value.decode("latin-1").lower()
                    for key, value in headers
                    if key.lower() == b"content-type"
                ),
                "",
            )

            if "text/html" in content_type and b"</head>" in body:
                body = body.replace(
                    b"</head>",
                    ORDER_UX_PATCH.encode("utf-8") + b"</head>",
                    1,
                )

                headers = [
                    (key, value)
                    for key, value in headers
                    if key.lower() != b"content-length"
                ]
                headers.append(
                    (b"content-length", str(len(body)).encode("ascii"))
                )

            if response_start:
                response_start["headers"] = headers
                await send(response_start)

            await send({
                "type": "http.response.body",
                "body": body,
                "more_body": False,
            })

        await self.app(forward_scope, receive, capture_send)



# ─────────────── Page « Signaler un problème » / « Répondre » (formulaire éditable) ───────────────

def _issue_form_html(
    action_path: str,
    cancel_url: str,
    heading: str,
    subtitle: str,
    default_message: str,
    show_sms: bool = True,
    quoted: str | None = None,
) -> str:
    """Petite page HTML autonome : message pré-rempli, modifiable, avant envoi réel.
    `quoted`, si fourni, affiche le message original en lecture seule au-dessus du champ éditable."""
    escaped_message = (
        default_message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )
    sms_checkbox = (
        '<label class="checkbox"><input type="checkbox" name="send_sms" checked> Envoyer par SMS</label>'
        if show_sms
        else ""
    )
    quoted_block = ""
    if quoted:
        escaped_quoted = quoted.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        quoted_block = f"""
        <div class="quoted">
          <div class="quoted-label">Message reçu :</div>
          <div class="quoted-text">{escaped_quoted}</div>
        </div>"""
    return f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{heading}</title>
<style>
  body {{ font-family: -apple-system, Arial, sans-serif; background: #f7f0e4; margin: 0; padding: 40px 20px; }}
  .card {{ max-width: 640px; margin: 0 auto; background: white; border-radius: 10px;
           padding: 32px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
  h1 {{ color: #1f6b2d; font-size: 20px; margin-top: 0; }}
  .subtitle {{ color: #666; font-size: 14px; margin-bottom: 20px; }}
  .quoted {{ background: #f7f0e4; border-left: 3px solid #c47d0e; border-radius: 4px;
             padding: 12px 14px; margin-bottom: 18px; }}
  .quoted-label {{ font-size: 12px; color: #888; margin-bottom: 4px; }}
  .quoted-text {{ font-size: 14px; color: #444; white-space: pre-wrap; }}
  textarea {{ width: 100%; min-height: 180px; font-size: 14px; padding: 12px;
              border: 1px solid #ccc; border-radius: 6px; font-family: inherit;
              box-sizing: border-box; resize: vertical; }}
  label.checkbox {{ display: inline-flex; align-items: center; gap: 6px; margin-right: 20px;
                     font-size: 14px; color: #333; margin-top: 14px; }}
  .actions {{ margin-top: 24px; display: flex; gap: 12px; }}
  button, a.btn {{ padding: 10px 20px; border-radius: 6px; border: none; font-size: 14px;
                   cursor: pointer; text-decoration: none; display: inline-block; }}
  .confirm {{ background: #1f6b2d; color: white; font-weight: 600; }}
  .cancel {{ background: #eee; color: #333; }}
</style>
</head>
<body>
  <div class="card">
    <h1>{heading}</h1>
    <div class="subtitle">{subtitle}</div>
    {quoted_block}
    <form method="post" action="{action_path}">
      <textarea name="message">{escaped_message}</textarea>
      <div>
        <label class="checkbox"><input type="checkbox" name="send_email" checked> Envoyer par email</label>
        {sms_checkbox}
      </div>
      <div class="actions">
        <button type="submit" class="confirm">Confirmer l'envoi</button>
        <a class="btn cancel" href="{cancel_url}">Annuler</a>
      </div>
    </form>
  </div>
</body>
</html>
"""


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username", "")
        password = form.get("password", "")
        if (
            username == os.getenv("ADMIN_USERNAME", "admin")
            and password == os.getenv("ADMIN_PASSWORD", "")
            and os.getenv("ADMIN_PASSWORD")
        ):
            request.session.update({"authenticated": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("authenticated", False)


class CategoryAdmin(ModelView, model=Category):
    name = "Catégorie"
    name_plural = "Catégories"
    icon = "fa-solid fa-list"

    column_list = [
        Category.name_fr,
        Category.name_en,
        Category.position,
    ]

    column_labels = {
        Category.name_fr: "Nom en français",
        Category.name_en: "Nom en anglais",
        Category.subtitle_fr: "Sous-titre en français",
        Category.subtitle_en: "Sous-titre en anglais",
        Category.position: "Ordre d’affichage",
    }

    column_searchable_list = [
        Category.name_fr,
        Category.name_en,
        Category.subtitle_fr,
        Category.subtitle_en,
    ]

    column_sortable_list = [
        Category.name_fr,
        Category.name_en,
        Category.position,
    ]

    column_default_sort = ("position", False)

    column_formatters = {
        Category.position: lambda model, attr: (
            f"Position {getattr(model, attr) + 1}"
        ),
    }

    form_columns = [
        Category.name_fr,
        Category.name_en,
        Category.subtitle_fr,
        Category.subtitle_en,
        Category.position,
    ]

    async def after_model_change(self, data, model, is_created, request) -> None:
        invalidate_menu_cache()

    async def after_model_delete(self, model, request) -> None:
        invalidate_menu_cache()
class DishAdmin(ModelView, model=Dish):
    name = "Plat"
    name_plural = "Plats"
    icon = "fa-solid fa-utensils"

    column_list = [
        Dish.image_url,
        Dish.name_fr,
        Dish.category,
        Dish.price,
        Dish.is_available,
    ]

    column_labels = {
        Dish.image_url: "Photo",
        Dish.name_fr: "Plat",
        Dish.category: "Catégorie",
        Dish.price: "Prix",
        Dish.is_available: "Disponibilité",
    }

    column_searchable_list = [
        Dish.name_fr,
    ]

    column_sortable_list = [
        Dish.name_fr,
        Dish.price,
        Dish.position,
        Dish.is_available,
    ]

    column_default_sort = ("position", False)

    @staticmethod
    def _image_formatter(model, attribute, request):
        url = getattr(model, attribute) or ""
        if not url:
            return Markup('<span style="color:#9aa0aa">—</span>')
        safe_url = escape(url)
        return Markup(
            f'<img src="{safe_url}" alt="" loading="lazy" '
            f'style="width:44px;height:44px;object-fit:cover;border-radius:10px;'
            f'box-shadow:0 2px 6px rgba(18,63,29,.12)">'
        )

    column_formatters = {
        Dish.image_url: _image_formatter,
        Dish.price: lambda model, attr: f"{getattr(model, attr):.2f} €".replace(".", ","),
        Dish.is_available: lambda model, attr: (
            "🟢 Disponible" if getattr(model, attr) else "🔴 Indisponible"
        ),
        Dish.category: lambda model, attr: (
            getattr(getattr(model, attr), "name_fr", "Sans catégorie")
        ),
    }

    form_columns = [
        Dish.name_fr,
        Dish.price,
        Dish.is_available,
        Dish.category,
        Dish.position,
        Dish.image_url,
    ]
    async def after_model_change(self, data, model, is_created, request) -> None:
        invalidate_menu_cache()

    async def after_model_delete(self, model, request) -> None:
        invalidate_menu_cache()

class OrderAdmin(ModelView, model=Order):
    name = "Commande"
    name_plural = "Commandes"
    icon = "fa-solid fa-basket-shopping"

    column_list = [
        Order.id,
        Order.customer_name,
        Order.order_type,
        Order.address_street,
        Order.total,
        Order.payment_status,
        Order.status,
        Order.requested_date,
    ]

    column_labels = {
        Order.id: "N°",
        Order.customer_name: "Client",
        Order.order_type: "Réception",
        Order.address_street: "Destination",
        Order.total: "Total",
        Order.payment_status: "Paiement",
        Order.status: "État",
        Order.requested_date: "Créneau",
    }

    column_searchable_list = [
        Order.customer_name,
        Order.customer_phone,
        Order.customer_email,
        Order.address_street,
        Order.city,
        Order.postal_code,
    ]
    column_sortable_list = [
        Order.id,
        Order.total,
        Order.status,
        Order.requested_date,
        Order.created_at,
    ]
    column_default_sort = ("created_at", True)
    # Les filtres UX Commandes travaillent côté navigateur.
    # On charge donc toutes les commandes dans la réponse SQLAdmin au lieu
    # de limiter le DOM à la page courante.
    page_size = ORDER_FILTER_PAGE_SIZE
    page_size_options = [ORDER_FILTER_PAGE_SIZE]

    column_details_list = [
        Order.id,
        Order.customer_name,
        Order.customer_phone,
        Order.customer_email,
        Order.order_type,
        Order.requested_date,
        Order.requested_time,
        Order.address_street,
        Order.address_extra,
        Order.postal_code,
        Order.city,
        Order.subtotal,
        Order.delivery_fee,
        Order.total,
        Order.payment_method,
        Order.payment_status,
        Order.status,
        Order.note,
        Order.created_at,
    ]

    @staticmethod
    def _customer_formatter(model, attribute, request):
        name = escape(model.customer_name or "Client")
        phone = escape(model.customer_phone or "—")
        return Markup(
            f'<div style="min-width:170px">'
            f'<strong style="color:#163f21">{name}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">☎ {phone}</span>'
            f'</div>'
        )

    @staticmethod
    def _normalized_order_type(value):
        """Normalise les différentes valeurs possibles venant du frontend."""
        raw = (value or "").strip().lower()
        normalized = (
            raw.replace("-", "_")
               .replace(" ", "_")
               .replace("à", "a")
               .replace("é", "e")
               .replace("è", "e")
               .replace("ê", "e")
        )

        delivery_values = {
            "livraison",
            "delivery",
            "deliver",
            "home_delivery",
            "livraison_domicile",
            "livraison_a_domicile",
            "a_domicile",
            "domicile",
        }
        pickup_values = {
            "a_emporter",
            "emporter",
            "pickup",
            "pick_up",
            "takeaway",
            "take_away",
            "retrait",
            "retrait_restaurant",
            "retrait_au_restaurant",
            "click_collect",
            "click_and_collect",
            "sur_place_retrait",
        }

        if normalized in delivery_values:
            return "livraison"
        if normalized in pickup_values:
            return "a_emporter"
        return normalized or "a_emporter"

    @staticmethod
    def _order_type_formatter(model, attribute, request):
        order_type = OrderAdmin._normalized_order_type(model.order_type)

        if order_type == "livraison":
            label = "Livraison"
            icon = "🚚"
            background = "#e8f4ea"
            color = "#1f6b2d"
        elif order_type == "a_emporter":
            label = "À emporter"
            icon = "🏪"
            background = "#fff5df"
            color = "#9a6500"
        else:
            # Valeur inconnue : on ne la transforme surtout pas en "À emporter".
            label = (model.order_type or "Autre").replace("_", " ").replace("-", " ").title()
            icon = "📦"
            background = "#eef1f5"
            color = "#566070"

        return Markup(
            f'<span style="display:inline-flex;align-items:center;gap:6px;'
            f'padding:6px 10px;border-radius:999px;background:{background};'
            f'color:{color};font-weight:700;font-size:12px;white-space:nowrap">'
            f'{icon} {escape(label)}</span>'
        )

    @staticmethod
    def _address_formatter(model, attribute, request):
        if OrderAdmin._normalized_order_type(model.order_type) != "livraison":
            return Markup('<span style="color:#9aa0aa">Retrait au restaurant</span>')

        street = escape(model.address_street or "Adresse non renseignée")
        city_line = " ".join(
            part for part in [model.postal_code or "", model.city or ""] if part
        )
        city_line = escape(city_line or "—")
        return Markup(
            f'<div style="max-width:230px">'
            f'<strong style="color:#2d3748">📍 {street}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">{city_line}</span>'
            f'</div>'
        )

    @staticmethod
    def _money_formatter(model, attribute, request):
        value = float(model.total or 0)
        amount = f"{value:,.2f}".replace(",", " ").replace(".", ",")
        return Markup(
            f'<strong style="color:#c47d0e;font-size:15px;white-space:nowrap">'
            f'{amount} €</strong>'
        )

    @staticmethod
    def _payment_formatter(model, attribute, request):
        status = (model.payment_status or "en_attente").lower()
        method = "Carte" if model.payment_method == "carte" else "Sur place"
        styles = {
            "paye": ("Payé", "#e8f4ea", "#1f6b2d"),
            "payé": ("Payé", "#e8f4ea", "#1f6b2d"),
            "en_attente": ("En attente", "#fff5df", "#9a6500"),
            "echoue": ("Échoué", "#fdeaea", "#b42318"),
            "échoué": ("Échoué", "#fdeaea", "#b42318"),
        }
        label, background, color = styles.get(
            status, (status.replace("_", " ").title(), "#eef1f5", "#566070")
        )
        return Markup(
            f'<div style="min-width:110px">'
            f'<span style="display:inline-block;padding:5px 9px;border-radius:999px;'
            f'background:{background};color:{color};font-weight:700;font-size:12px">'
            f'{escape(label)}</span>'
            f'<span style="color:#c6a044;font-size:11px">&nbsp;·&nbsp;</span>'
            f'<span style="color:#7a8190;font-size:11px">{escape(method)}</span>'
            f'</div>'
        )

    @staticmethod
    def _status_formatter(model, attribute, request):
        value = (model.status or "nouvelle").lower()
        styles = {
            "nouvelle": ("Nouvelle", "#eaf2ff", "#2457a6"),
            "confirmée": ("Confirmée", "#e8f4ea", "#1f6b2d"),
            "confirmee": ("Confirmée", "#e8f4ea", "#1f6b2d"),
            "en préparation": ("En préparation", "#fff5df", "#9a6500"),
            "en_preparation": ("En préparation", "#fff5df", "#9a6500"),
            "prête": ("Prête", "#eee9ff", "#6941c6"),
            "prete": ("Prête", "#eee9ff", "#6941c6"),
            "livrée": ("Livrée", "#e8f4ea", "#1f6b2d"),
            "livree": ("Livrée", "#e8f4ea", "#1f6b2d"),
            "annulée": ("Annulée", "#fdeaea", "#b42318"),
            "annulee": ("Annulée", "#fdeaea", "#b42318"),
        }
        label, background, color = styles.get(
            value, (value.replace("_", " ").title(), "#eef1f5", "#566070")
        )
        return Markup(
            f'<span style="display:inline-block;padding:6px 10px;border-radius:999px;'
            f'background:{background};color:{color};font-weight:700;font-size:12px;'
            f'white-space:nowrap">{escape(label)}</span>'
        )

    @staticmethod
    def _slot_formatter(model, attribute, request):
        date = escape(model.requested_date or "Dès que possible")
        time = escape(model.requested_time or "")
        time_html = (
            f'<span style="display:inline-block;width:8px"></span>'
            f'<strong style="color:#1f6b2d">{time}</strong>'
            if time else ""
        )
        return Markup(
            f'<span style="white-space:nowrap;color:#606775;font-size:12px">'
            f'📅 {date}{time_html}</span>'
        )

    @staticmethod
    def _id_ticket_formatter(model, attribute, request):
        """Affiche un vrai mini-ticket cliquable ouvrant le reçu en popup."""
        return Markup(
            f'<a href="/order-ticket/{model.id}" target="_blank" '
            f'class="ticket-trigger mc-ticket-trigger" data-order-id="{model.id}" '
            f'aria-label="Ouvrir le reçu de la commande #{model.id}" '
            f'title="Voir le reçu de la commande #{model.id}">'
            f'<span class="mc-ticket-receipt-icon" aria-hidden="true">▤</span>'
            f'<span class="mc-ticket-copy">'
            f'<span class="mc-ticket-kicker">TICKET</span>'
            f'<strong class="mc-ticket-number">#{model.id}</strong>'
            f'</span>'
            f'<span class="mc-ticket-open" aria-hidden="true">›</span>'
            f'</a>'
        )

    column_formatters = {
        Order.id: _id_ticket_formatter,
        Order.customer_name: _customer_formatter,
        Order.order_type: _order_type_formatter,
        Order.address_street: _address_formatter,
        Order.total: _money_formatter,
        Order.payment_status: _payment_formatter,
        Order.status: _status_formatter,
        Order.requested_date: _slot_formatter,
    }

    can_create = False


class OrderItemAdmin(ModelView, model=OrderItem):
    name = "Article commandé"
    name_plural = "Articles commandés"
    icon = "fa-solid fa-receipt"

    column_list = [
        OrderItem.order_id,
        OrderItem.dish_name,
        OrderItem.quantity,
        OrderItem.unit_price,
        OrderItem.removed_ingredients,
        OrderItem.selected_choices,
    ]

    column_labels = {
        OrderItem.order_id: "Commande",
        OrderItem.dish_name: "Plat",
        OrderItem.quantity: "Quantité",
        OrderItem.unit_price: "Prix unitaire",
        OrderItem.removed_ingredients: "Sans",
        OrderItem.selected_choices: "Personnalisation",
    }

    @staticmethod
    def _selected_choices_formatter(model, attribute, request):
        """Affiche la personnalisation de façon lisible, sans JSON technique."""
        raw = getattr(model, attribute, None)
        if not raw:
            return Markup('<span class="mc-empty-value">—</span>')

        try:
            if isinstance(raw, str):
                data = json.loads(raw)
            elif isinstance(raw, dict):
                data = raw
            else:
                data = dict(raw)
        except (TypeError, ValueError, json.JSONDecodeError):
            return Markup('<span class="mc-empty-value">—</span>')

        if not isinstance(data, dict) or not data:
            return Markup('<span class="mc-empty-value">—</span>')

        # IDs de plats éventuellement utilisés comme choix/substitutions.
        all_ids = set()
        for selection in data.values():
            if not isinstance(selection, dict):
                continue
            for dish_id in selection.get("dish_ids") or []:
                all_ids.add(dish_id)

        db = SessionLocal()
        try:
            names = {}
            if all_ids:
                rows = db.query(Dish.id, Dish.name_fr).filter(Dish.id.in_(all_ids)).all()
                names = {row[0]: row[1] for row in rows}
        finally:
            db.close()

        rendered_rows = []

        for label, selection in data.items():
            if not isinstance(selection, dict):
                continue

            dish_ids = selection.get("dish_ids") or []
            options = selection.get("options") or []
            alternative = selection.get("alternative")
            sub_removed = selection.get("sub_removed") or []
            sub_choices = selection.get("sub_choices") or {}

            values = []

            if dish_ids:
                counts = {}
                for dish_id in dish_ids:
                    counts[dish_id] = counts.get(dish_id, 0) + 1
                for dish_id, count in counts.items():
                    dish_name = names.get(dish_id, f"#{dish_id}")
                    values.append(f"{dish_name} ×{count}" if count > 1 else dish_name)

            if options:
                values.extend(str(option) for option in options if option)

            if alternative:
                if isinstance(alternative, dict):
                    alt_name = alternative.get("name") or alternative.get("label")
                    if alt_name:
                        values.append(str(alt_name))
                elif isinstance(alternative, (str, int, float)):
                    values.append(str(alternative))

            # Déduplique tout en conservant l'ordre.
            seen = set()
            clean_values = []
            for value in values:
                value = str(value).strip()
                if value and value not in seen:
                    seen.add(value)
                    clean_values.append(value)

            extras = []
            if sub_removed:
                clean_removed = [str(v).strip() for v in sub_removed if str(v).strip()]
                if clean_removed:
                    extras.append("Sans : " + ", ".join(clean_removed))

            if isinstance(sub_choices, dict):
                for sub_label, sub_values in sub_choices.items():
                    if not sub_values:
                        continue
                    if not isinstance(sub_values, (list, tuple, set)):
                        sub_values = [sub_values]
                    clean_sub = [str(v).strip() for v in sub_values if str(v).strip()]
                    if clean_sub:
                        extras.append(f"{sub_label} : {', '.join(clean_sub)}")

            # Ne montre jamais les champs techniques vides/null.
            if not clean_values and not extras:
                continue

            main_value = ", ".join(clean_values) if clean_values else "—"
            extras_html = ""
            if extras:
                extras_html = (
                    '<div class="mc-personalization-extra">'
                    + " · ".join(escape(item) for item in extras)
                    + "</div>"
                )

            rendered_rows.append(
                '<div class="mc-personalization-row">'
                f'<span class="mc-personalization-label">{escape(str(label))}</span>'
                '<div class="mc-personalization-content">'
                f'<span class="mc-personalization-value">{escape(main_value)}</span>'
                f'{extras_html}'
                '</div>'
                '</div>'
            )

        if not rendered_rows:
            return Markup('<span class="mc-empty-value">—</span>')

        return Markup(
            '<div class="mc-personalization-summary">'
            + "".join(rendered_rows)
            + "</div>"
        )

    @staticmethod
    def _removed_ingredients_formatter(model, attribute, request):
        raw = getattr(model, attribute, None)
        if not raw:
            return Markup('<span class="mc-empty-value">—</span>')
        try:
            data = json.loads(raw) if isinstance(raw, str) else raw
        except (TypeError, ValueError, json.JSONDecodeError):
            data = raw

        if isinstance(data, (list, tuple, set)):
            values = [str(value).strip() for value in data if str(value).strip()]
        elif data:
            values = [str(data).strip()]
        else:
            values = []

        if not values:
            return Markup('<span class="mc-empty-value">—</span>')

        return Markup(
            '<div class="mc-without-list">'
            + ''.join(
                f'<span class="mc-without-chip">{escape(value)}</span>'
                for value in values
            )
            + '</div>'
        )

    column_formatters = {
        OrderItem.order_id: lambda model, attr: (
            f"Commande #{getattr(model, attr)}"
        ),
        OrderItem.quantity: lambda model, attr: (
            f"× {getattr(model, attr)}"
        ),
        OrderItem.unit_price: lambda model, attr: (
            f"{getattr(model, attr):.2f} €".replace(".", ",")
        ),
        OrderItem.removed_ingredients: _removed_ingredients_formatter,
        OrderItem.selected_choices: _selected_choices_formatter,
    }

    # SQLAdmin utilise un formatter séparé sur la page "Voir".
    # Sans ceci, Personnalisation retombait sur le JSON brut.
    column_formatters_detail = column_formatters
    column_details_list = column_list

    column_searchable_list = [
        OrderItem.dish_name,
    ]

    column_sortable_list = [
        OrderItem.order_id,
        OrderItem.dish_name,
        OrderItem.quantity,
        OrderItem.unit_price,
    ]

    column_default_sort = ("order_id", True)

    can_create = False
    can_edit = False


class TableReservationAdmin(ModelView, model=TableReservation):
    name = "Réservation table"
    name_plural = "Réservations tables"
    icon = "fa-solid fa-chair"

    column_list = [
        TableReservation.last_name,
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
    ]

    column_labels = {
        TableReservation.last_name: "Client",
        TableReservation.date: "Date",
        TableReservation.time: "Heure",
        TableReservation.guests: "Convives",
        TableReservation.status: "Statut",
    }

    column_formatters = {
        TableReservation.last_name: lambda model, attr: (
            f"👤 {getattr(model, attr).title()}"
        ),
        TableReservation.date: lambda model, attr: (
            getattr(model, attr).strftime("%d/%m/%Y")
            if hasattr(getattr(model, attr), "strftime")
            else str(getattr(model, attr))
        ),
        TableReservation.time: lambda model, attr: (
            f"🕒 {getattr(model, attr)}"
        ),
        TableReservation.guests: lambda model, attr: (
            f"👥 {getattr(model, attr)} personne"
            if getattr(model, attr) == 1
            else f"👥 {getattr(model, attr)} personnes"
        ),
        TableReservation.status: lambda model, attr: {
            "nouvelle": "🟡 Nouvelle",
            "confirmée": "🟢 Confirmée",
            "problème signalé": "🔴 Problème signalé",
            "annulée": "⚫ Annulée",
        }.get(
            str(getattr(model, attr)).lower(),
            str(getattr(model, attr)).capitalize(),
        ),
    }

    column_searchable_list = [
        TableReservation.last_name,
        TableReservation.phone,
        TableReservation.email,
    ]

    column_sortable_list = [
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
        TableReservation.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        TableReservation.id,
        TableReservation.first_name,
        TableReservation.last_name,
        TableReservation.phone,
        TableReservation.email,
        TableReservation.date,
        TableReservation.time,
        TableReservation.guests,
        TableReservation.status,
        TableReservation.table_ids,
        TableReservation.note,
        TableReservation.created_at,
    ]

    can_create = False

    @action(
        name="confirm",
        label="✅ Confirmer (email + SMS)",
        confirmation_message=(
            "Confirmer la/les réservation(s) sélectionnée(s) "
            "et envoyer un email + SMS de confirmation ?"
        ),
    )
    async def confirm_reservation(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                reservation = db.get(TableReservation, int(pk))
                if not reservation:
                    continue
                reservation.status = "confirmée"
                db.commit()
                db.refresh(reservation)

                subject, body, sms_text = table_reservation_confirmed(reservation)
                send_email(reservation.email, subject, body, html=True)
                send_sms(reservation.phone, sms_text)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity),
            status_code=302,
        )

    @action(
        name="report-issue",
        label="🚨 Signaler un problème",
        add_in_detail=True,
        add_in_list=True,
    )
    async def report_issue(self, request: Request):
        pks = [pk for pk in request.query_params.get("pks", "").split(",") if pk]

        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity),
                status_code=302,
            )

        db = SessionLocal()
        try:
            reservation = db.get(TableReservation, int(pks[0]))

            if not reservation:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity),
                    status_code=302,
                )

            default_message = table_issue_message(reservation)

            title = (
                f"{reservation.first_name} "
                f"{reservation.last_name} — "
                f"{reservation.date} "
                f"{reservation.time} "
                f"({reservation.guests} pers.)"
            )
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/reservation-issue/table/{pks[0]}/send",
                cancel_url="/admin/table-reservation/list",
                heading="🚨 Signaler un problème",
                subtitle=title,
                default_message=default_message,
                show_sms=True,
            )
        )


class EventReservationAdmin(ModelView, model=EventReservation):
    name = "Réservation événement"
    name_plural = "Réservations événements"
    icon = "fa-solid fa-champagne-glasses"

    column_list = [
        EventReservation.event_type,
        EventReservation.last_name,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
    ]

    column_labels = {
        EventReservation.event_type: "Événement",
        EventReservation.last_name: "Client",
        EventReservation.date: "Date",
        EventReservation.time: "Heure",
        EventReservation.guests: "Convives",
        EventReservation.status: "Statut",
    }

    column_formatters = {
        EventReservation.event_type: lambda model, attr: {
            "anniversaire": "🎂 Anniversaire",
            "mariage": "💍 Mariage",
            "entreprise": "💼 Entreprise",
            "privé": "✨ Événement privé",
            "prive": "✨ Événement privé",
        }.get(
            str(getattr(model, attr) or "").lower(),
            f"✨ {str(getattr(model, attr) or 'Événement').title()}",
        ),

        EventReservation.last_name: lambda model, attr: (
            f"👤 {str(getattr(model, attr) or 'Client').title()}"
        ),

        EventReservation.date: lambda model, attr: (
            getattr(model, attr).strftime("%d/%m/%Y")
            if hasattr(getattr(model, attr), "strftime")
            else str(getattr(model, attr) or "—")
        ),

        EventReservation.time: lambda model, attr: (
            f"🕒 {getattr(model, attr) or '—'}"
        ),

        EventReservation.guests: lambda model, attr: (
            f"👥 {getattr(model, attr)} personne"
            if getattr(model, attr) == 1
            else f"👥 {getattr(model, attr)} personnes"
        ),

        EventReservation.status: lambda model, attr: {
            "nouvelle": "🟡 Nouvelle",
            "confirmée": "🟢 Confirmée",
            "confirmee": "🟢 Confirmée",
            "en attente": "🟠 En attente",
            "en_attente": "🟠 En attente",
            "problème signalé": "🔴 Problème signalé",
            "probleme signale": "🔴 Problème signalé",
            "annulée": "⚫ Annulée",
            "annulee": "⚫ Annulée",
        }.get(
            str(getattr(model, attr) or "").lower(),
            str(getattr(model, attr) or "Inconnu").capitalize(),
        ),
    }

    column_searchable_list = [
        EventReservation.event_type,
        EventReservation.last_name,
        EventReservation.phone,
        EventReservation.email,
    ]

    column_sortable_list = [
        EventReservation.event_type,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
        EventReservation.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        EventReservation.id,
        EventReservation.event_type,
        EventReservation.first_name,
        EventReservation.last_name,
        EventReservation.phone,
        EventReservation.email,
        EventReservation.date,
        EventReservation.time,
        EventReservation.guests,
        EventReservation.status,
        EventReservation.note,
        EventReservation.created_at,
    ]

    can_create = False

    @action(
        name="confirm",
        label="✅ Confirmer (email + SMS)",
        confirmation_message="Confirmer la/les réservation(s) sélectionnée(s) et envoyer un email + SMS de confirmation ?",
    )
    async def confirm_reservation(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                reservation = db.get(EventReservation, int(pk))
                if not reservation:
                    continue
                reservation.status = "confirmée"
                db.commit()
                db.refresh(reservation)

                subject, body, sms_text = event_reservation_confirmed(reservation)
                send_email(reservation.email, subject, body)
                send_sms(reservation.phone, sms_text)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity), status_code=302
        )

    @action(
        name="report-issue",
        label="🚨 Signaler un problème",
        add_in_detail=True,
        add_in_list=True,
    )
    async def report_issue(self, request: Request):
        pks = [p for p in request.query_params.get("pks", "").split(",") if p]
        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity), status_code=302
            )
        db = SessionLocal()
        try:
            reservation = db.get(EventReservation, int(pks[0]))
            if not reservation:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity), status_code=302
                )
            default_message = event_issue_message(reservation)
            title = (
                f"{reservation.event_type} — {reservation.first_name} {reservation.last_name} — "
                f"{reservation.date} {reservation.time} ({reservation.guests} pers.)"
            )
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/reservation-issue/event/{pks[0]}/send",
                cancel_url="/admin/event-reservation/list",
                heading="🚨 Signaler un problème",
                subtitle=title,
                default_message=default_message,
                show_sms=True,
            )
        )


class ContactMessageAdmin(ModelView, model=ContactMessage):
    name = "Message contact"
    name_plural = "Messages contact"
    icon = "fa-solid fa-envelope"

    column_list = [
        ContactMessage.name,
        ContactMessage.subject,
        ContactMessage.message,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.created_at,
    ]

    column_labels = {
        ContactMessage.name: "Contact",
        ContactMessage.subject: "Sujet",
        ContactMessage.message: "Message",
        ContactMessage.status: "Statut",
        ContactMessage.is_read: "Lecture",
        ContactMessage.created_at: "Reçu le",
    }

    column_searchable_list = [
        ContactMessage.name,
        ContactMessage.email,
        ContactMessage.subject,
        ContactMessage.message,
    ]

    column_sortable_list = [
        ContactMessage.name,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.created_at,
    ]

    column_default_sort = ("created_at", True)

    column_details_list = [
        ContactMessage.id,
        ContactMessage.name,
        ContactMessage.email,
        ContactMessage.phone,
        ContactMessage.subject,
        ContactMessage.message,
        ContactMessage.status,
        ContactMessage.is_read,
        ContactMessage.language,
        ContactMessage.created_at,
    ]

    @staticmethod
    def _contact_formatter(model, attribute, request):
        name = escape(model.name or "Contact")
        email = escape(model.email or "—")

        return Markup(
            f'<div style="min-width:170px">'
            f'<strong style="color:#163f21">👤 {name}</strong><br>'
            f'<span style="color:#7a8190;font-size:12px">{email}</span>'
            f'</div>'
        )

    @staticmethod
    def _subject_formatter(model, attribute, request):
        subject = escape(model.subject or "Sans objet")
        return Markup(f'<strong style="color:#2d3748">{subject}</strong>')

    @staticmethod
    def _message_formatter(model, attribute, request):
        message = str(model.message or "").strip()

        if not message:
            return Markup('<span style="color:#9aa0aa">Aucun message</span>')

        preview = message[:90]
        if len(message) > 90:
            preview += "…"

        return Markup(
            f'<div style="max-width:320px;color:#667085;'
            f'font-size:13px;line-height:1.45">'
            f'{escape(preview)}'
            f'</div>'
        )

    @staticmethod
    def _status_formatter(model, attribute, request):
        status = str(model.status or "nouveau").lower()

        styles = {
            "nouveau": ("Nouveau", "#eaf2ff", "#2457a6"),
            "lu": ("Lu", "#fff5df", "#9a6500"),
            "répondu": ("Répondu", "#e8f4ea", "#1f6b2d"),
            "repondu": ("Répondu", "#e8f4ea", "#1f6b2d"),
            "archivé": ("Archivé", "#eef1f5", "#566070"),
            "archive": ("Archivé", "#eef1f5", "#566070"),
        }

        label, background, color = styles.get(
            status,
            (status.replace("_", " ").title(), "#eef1f5", "#566070"),
        )

        return Markup(
            f'<span style="display:inline-block;padding:6px 10px;'
            f'border-radius:999px;background:{background};'
            f'color:{color};font-weight:700;font-size:12px;'
            f'white-space:nowrap">{escape(label)}</span>'
        )

    @staticmethod
    def _read_formatter(model, attribute, request):
        if model.is_read:
            return Markup('<span style="color:#1f6b2d;font-weight:700">✓ Lu</span>')

        return Markup('<span style="color:#c47d0e;font-weight:700">● Non lu</span>')

    @staticmethod
    def _date_formatter(model, attribute, request):
        value = model.created_at

        if not value:
            return "—"

        if hasattr(value, "strftime"):
            return value.strftime("%d/%m/%Y à %H:%M")

        return str(value)

    column_formatters = {
        ContactMessage.name: _contact_formatter,
        ContactMessage.subject: _subject_formatter,
        ContactMessage.message: _message_formatter,
        ContactMessage.status: _status_formatter,
        ContactMessage.is_read: _read_formatter,
        ContactMessage.created_at: _date_formatter,
    }

    can_create = False

    @action(
        name="acknowledge",
        label="✅ Accusé de réception (email)",
        confirmation_message="Envoyer un email « nous vous répondrons bientôt » au(x) contact(s) sélectionné(s) ?",
    )
    async def acknowledge_message(self, request: Request) -> RedirectResponse:
        pks = request.query_params.get("pks", "")
        db = SessionLocal()
        try:
            for pk in pks.split(","):
                if not pk:
                    continue
                message = db.get(ContactMessage, int(pk))
                if not message:
                    continue
                message.is_read = True
                db.commit()
                db.refresh(message)

                subject, body = contact_acknowledgement(message)
                send_email(message.email, subject, body)
        finally:
            db.close()

        return RedirectResponse(
            request.url_for("admin:list", identity=self.identity), status_code=302
        )

    @action(
        name="reply",
        label="✉️ Répondre",
        add_in_detail=True,
        add_in_list=True,
    )
    async def reply_to_message(self, request: Request):
        pks = [p for p in request.query_params.get("pks", "").split(",") if p]
        if len(pks) != 1:
            return RedirectResponse(
                request.url_for("admin:list", identity=self.identity), status_code=302
            )
        db = SessionLocal()
        try:
            message = db.get(ContactMessage, int(pks[0]))
            if not message:
                return RedirectResponse(
                    request.url_for("admin:list", identity=self.identity), status_code=302
                )
            default_message = contact_reply_default_message(message)
            title = f"{message.name} ({message.email})"
            original = message.message
        finally:
            db.close()

        return HTMLResponse(
            _issue_form_html(
                action_path=f"/contact-reply/{pks[0]}/send",
                cancel_url="/admin/contact-message/list",
                heading="✉️ Répondre au message",
                subtitle=title,
                default_message=default_message,
                show_sms=False,
                quoted=original,
            )
        )


def setup_admin(app):
    authentication_backend = AdminAuth(secret_key=os.getenv("SECRET_KEY", "change-me"))
    admin = Admin(
        app,
        engine,
        title="Miss Chawarma - Admin",
        authentication_backend=authentication_backend,
    )
    admin.add_view(CategoryAdmin)
    admin.add_view(DishAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(OrderItemAdmin)
    admin.add_view(TableReservationAdmin)
    admin.add_view(EventReservationAdmin)
    admin.add_view(ContactMessageAdmin)
    register_admin_dashboard_routes(app)

    from starlette.middleware.sessions import SessionMiddleware

    app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "change-me"))
    app.add_middleware(AdminBrandMiddleware)
    # Chargé après le thème principal afin que les règles compactes
    # gagnent la cascade CSS uniquement sur /admin/category/list.
    app.add_middleware(CategoryCompactCardsMiddleware)
    # Chargé encore après pour spécialiser la page Commandes
    # sans toucher aux autres écrans SQLAdmin.
    app.add_middleware(OrderUXMiddleware)

    @app.post("/reservation-issue/{kind}/{pk}/send")
    async def send_issue(kind: str, pk: int, request: Request):
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        form = await request.form()
        message = (form.get("message") or "").strip()
        send_email_flag = form.get("send_email") == "on"
        send_sms_flag = form.get("send_sms") == "on"

        Model = TableReservation if kind == "table" else EventReservation
        db = SessionLocal()
        try:
            reservation = db.get(Model, pk)
            if reservation and message:
                if send_email_flag:
                    send_email(
                        reservation.email, issue_email_subject(reservation.language), message
                    )
                if send_sms_flag:
                    send_sms(reservation.phone, message)
                reservation.status = "problème signalé"
                db.commit()
        finally:
            db.close()

        identity = "table-reservation" if kind == "table" else "event-reservation"
        return RedirectResponse(f"/admin/{identity}/list", status_code=302)

    @app.post("/contact-reply/{pk}/send")
    async def send_contact_reply(pk: int, request: Request):
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        form = await request.form()
        message_text = (form.get("message") or "").strip()
        send_email_flag = form.get("send_email") == "on"

        db = SessionLocal()
        try:
            contact_message = db.get(ContactMessage, pk)
            if contact_message and message_text:
                if send_email_flag:
                    send_email(
                        contact_message.email,
                        contact_reply_subject(contact_message.language),
                        message_text,
                    )
                contact_message.status = "répondu"
                contact_message.is_read = True
                db.commit()
        finally:
            db.close()

        return RedirectResponse("/admin/contact-message/list", status_code=302)

    @app.get("/order-ticket/{order_id}")
    async def order_ticket(order_id: int, request: Request):
        """Reçu premium Miss Chawarma affiché dans la popup des commandes."""
        if not request.session.get("authenticated"):
            return RedirectResponse("/admin/login", status_code=302)

        db = SessionLocal()
        try:
            order = db.get(Order, order_id)
            if not order:
                return HTMLResponse(
                    """
                    <!doctype html>
                    <html lang="fr">
                    <meta charset="utf-8">
                    <body style="font-family:Arial,sans-serif;padding:30px;color:#123f1d">
                      <h1>Commande introuvable</h1>
                    </body>
                    </html>
                    """,
                    status_code=404,
                )

            items = db.query(OrderItem).filter(OrderItem.order_id == order_id).all()

            all_dish_ids = set()
            for item in items:
                if item.selected_choices:
                    try:
                        data = json.loads(item.selected_choices)
                        for sel in data.values():
                            all_dish_ids.update(sel.get("dish_ids") or [])
                    except (TypeError, ValueError):
                        pass

            dish_names = {}
            if all_dish_ids:
                rows = (
                    db.query(Dish.id, Dish.name_fr)
                    .filter(Dish.id.in_(all_dish_ids))
                    .all()
                )
                dish_names = {row[0]: row[1] for row in rows}

            def format_choices(raw):
                if not raw:
                    return ""
                try:
                    data = json.loads(raw)
                except (TypeError, ValueError):
                    return ""

                lines = []
                for label, sel in data.items():
                    dish_ids = sel.get("dish_ids") or []
                    options = sel.get("options") or []

                    if dish_ids:
                        counts = {}
                        for did in dish_ids:
                            counts[did] = counts.get(did, 0) + 1

                        parts = []
                        for did, count in counts.items():
                            name = dish_names.get(did, f"#{did}")
                            parts.append(f"{name} ×{count}" if count > 1 else name)
                        value = ", ".join(parts)
                    elif options:
                        value = ", ".join(options)
                    else:
                        value = ""

                    if value:
                        lines.append(
                            f"<strong>{escape(label)}:</strong> {escape(value)}"
                        )

                    sub_removed = sel.get("sub_removed") or []
                    sub_choices = sel.get("sub_choices") or {}
                    extras = []

                    if sub_removed:
                        extras.append(f"sans {', '.join(sub_removed)}")

                    for sub_label, sub_vals in sub_choices.items():
                        if sub_vals:
                            extras.append(f"{sub_label}: {', '.join(sub_vals)}")

                    if extras:
                        lines.append(
                            f'<span class="sub">↳ {escape(" · ".join(extras))}</span>'
                        )

                return "<br>".join(lines)

            def money(value):
                amount = float(value or 0)
                return f"{amount:,.2f}".replace(",", " ").replace(".", ",") + " €"

            order_type = OrderAdmin._normalized_order_type(order.order_type)
            is_delivery = order_type == "livraison"

            reception_fr = "Livraison" if is_delivery else "À emporter"
            reception_en = "Delivery" if is_delivery else "Pickup"

            payment_status_key = str(order.payment_status or "en_attente").strip().lower()
            payment_status_map = {
                "paye": ("Payé", "Paid"),
                "payé": ("Payé", "Paid"),
                "en_attente": ("En attente", "Pending"),
                "echoue": ("Échoué", "Failed"),
                "échoué": ("Échoué", "Failed"),
            }
            payment_fr, payment_en = payment_status_map.get(
                payment_status_key,
                (
                    payment_status_key.replace("_", " ").title(),
                    payment_status_key.replace("_", " ").title(),
                ),
            )

            card_payment = str(order.payment_method or "").strip().lower() == "carte"
            method_fr = "Carte" if card_payment else "Sur place"
            method_en = "Card" if card_payment else "On site"
            payment_display_fr = f"{payment_fr} · {method_fr}"
            payment_display_en = f"{payment_en} · {method_en}"

            requested_date = escape(order.requested_date or "—")
            requested_time = escape(order.requested_time or "")
            slot_html = (
                f'<span class="slot-date">{requested_date}</span>'
                + (
                    f'<span class="slot-time">{requested_time}</span>'
                    if requested_time
                    else ""
                )
            )

            destination_parts = []
            if is_delivery:
                if order.address_street:
                    destination_parts.append(str(order.address_street))
                city_line = " ".join(
                    p
                    for p in [
                        str(order.postal_code or "").strip(),
                        str(order.city or "").strip(),
                    ]
                    if p
                )
                if city_line:
                    destination_parts.append(city_line)

            destination = (
                " · ".join(destination_parts)
                if destination_parts
                else ("Adresse non renseignée" if is_delivery else "Retrait au restaurant")
            )
            destination_en = (
                destination
                if is_delivery
                else "Pickup at restaurant"
            )

            items_html = ""
            for item in items:
                try:
                    removed_values = json.loads(item.removed_ingredients or "[]")
                    if not isinstance(removed_values, list):
                        removed_values = []
                except (TypeError, ValueError):
                    removed_values = []

                removed = ", ".join(str(value) for value in removed_values if value)
                choices_html = format_choices(item.selected_choices)

                extras = ""
                if removed:
                    extras += (
                        f'<div class="item-extra item-removed">'
                        f'<span data-fr="Sans" data-en="Without">Sans</span> : '
                        f'{escape(removed)}</div>'
                    )
                if choices_html:
                    extras += f'<div class="item-extra item-choices">{choices_html}</div>'

                items_html += f"""
                  <tr class="order-line">
                    <td class="article-cell">
                      <div class="article-name">{escape(item.dish_name)}</div>
                      {extras}
                    </td>
                    <td class="qty-cell">{int(item.quantity or 0)}</td>
                    <td class="price-cell">{money(item.unit_price)}</td>
                  </tr>
                """

            if not items_html:
                items_html = """
                  <tr>
                    <td colspan="3" class="empty-items"
                        data-fr="Aucun article dans cette commande."
                        data-en="No items in this order.">
                      Aucun article dans cette commande.
                    </td>
                  </tr>
                """

            subtotal_value = float(order.subtotal or 0)
            delivery_fee_value = float(order.delivery_fee or 0)
            breakdown_html = ""

            if delivery_fee_value > 0:
                breakdown_html = f"""
                  <div class="breakdown-row">
                    <span data-fr="Sous-total" data-en="Subtotal">Sous-total</span>
                    <strong>{money(subtotal_value)}</strong>
                  </div>
                  <div class="breakdown-row">
                    <span data-fr="Livraison" data-en="Delivery">Livraison</span>
                    <strong>{money(delivery_fee_value)}</strong>
                  </div>
                """

            note_html = ""
            if order.note:
                note_html = f"""
                  <div class="receipt-note">
                    <span class="note-icon">✎</span>
                    <div>
                      <strong data-fr="Note" data-en="Note">Note</strong>
                      <p>{escape(order.note)}</p>
                    </div>
                  </div>
                """

            html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Commande #{order.id} · Miss Chawarma</title>
<style>
  :root {{
    --green:#1f6b2d;
    --dark:#123f1d;
    --gold:#c47d0e;
    --gold2:#e4b83f;
    --cream:#f7f0e4;
    --paper:#fffdf8;
    --muted:#6f786f;
    --line:rgba(31,107,45,.14);
  }}

  * {{ box-sizing:border-box; }}

  html,body {{ min-height:100%; }}

  body {{
    margin:0;
    padding:22px 14px 28px;
    color:#253228;
    background:
      radial-gradient(circle at 90% 0,rgba(228,184,63,.13),transparent 220px),
      radial-gradient(circle at 5% 95%,rgba(31,107,45,.08),transparent 240px),
      #efeae1;
    font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
  }}

  .receipt {{
    position:relative;
    width:min(100%,520px);
    margin:0 auto;
    padding:34px 30px 28px;
    border:1px solid rgba(196,125,14,.22);
    background:
      linear-gradient(rgba(255,253,248,.97),rgba(255,253,248,.97)),
      repeating-linear-gradient(0deg,rgba(18,63,29,.012) 0 1px,transparent 1px 4px);
    box-shadow:0 22px 58px rgba(24,35,24,.16);
  }}

  /* Bord supérieur et inférieur façon ticket de caisse perforé. */
  .receipt::before,
  .receipt::after {{
    content:"";
    position:absolute;
    left:0;
    right:0;
    height:14px;
    z-index:2;
    pointer-events:none;
    background:
      radial-gradient(circle at 7px 7px,#efeae1 0 6px,transparent 6.4px)
      0 0/14px 14px repeat-x;
  }}

  .receipt::before {{ top:-7px; }}
  .receipt::after {{ bottom:-7px; }}

  .brand {{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;
    margin-bottom:7px;
  }}

  .brand-line {{
    width:58px;
    height:2px;
    border-radius:999px;
    background:linear-gradient(90deg,transparent,var(--gold));
  }}

  .brand-line:last-child {{
    background:linear-gradient(90deg,var(--gold),transparent);
  }}

  .brand img {{
    width:92px;
    height:72px;
    object-fit:contain;
    filter:drop-shadow(0 4px 8px rgba(18,63,29,.08));
  }}

  .receipt-label {{
    margin-top:7px;
    color:var(--gold);
    font-family:Georgia,"Times New Roman",serif;
    font-size:12px;
    font-weight:800;
    letter-spacing:.20em;
    text-align:center;
    text-transform:uppercase;
  }}

  .ticket-number {{
    width:max-content;
    min-width:86px;
    margin:16px auto 18px;
    padding:8px 17px 9px;
    border:1px solid rgba(196,125,14,.25);
    border-radius:10px;
    background:#fffaf0;
    color:var(--dark);
    font-family:Georgia,"Times New Roman",serif;
    font-size:30px;
    font-weight:800;
    line-height:1;
    text-align:center;
    box-shadow:0 5px 14px rgba(196,125,14,.07);
  }}

  .section-dash {{
    margin:0 0 17px;
    border-top:1px dashed rgba(109,98,69,.42);
  }}

  .info-grid {{
    display:grid;
    gap:10px;
    padding:0 4px 19px;
  }}

  .info-row {{
    display:grid;
    grid-template-columns:28px 116px minmax(0,1fr);
    align-items:center;
    gap:7px;
    font-size:12px;
  }}

  .info-icon {{
    width:25px;
    height:25px;
    display:grid;
    place-items:center;
    border-radius:8px;
    background:#edf5ea;
    color:var(--green);
    font-size:13px;
  }}

  .info-label {{
    color:#667068;
    font-size:11px;
    font-weight:700;
  }}

  .info-value {{
    min-width:0;
    color:#28322a;
    font-size:12px;
    font-weight:700;
    text-align:right;
    overflow-wrap:anywhere;
  }}

  .info-value.payment {{
    color:#a56e00;
  }}

  .slot-value {{
    display:flex;
    justify-content:flex-end;
    align-items:baseline;
    flex-wrap:wrap;
    gap:7px;
  }}

  .slot-date {{ color:#596271; }}
  .slot-time {{ color:var(--green); font-weight:900; }}

  .details-title {{
    margin:16px 0 11px;
    color:var(--gold);
    font-family:Georgia,"Times New Roman",serif;
    font-size:11px;
    font-weight:800;
    letter-spacing:.17em;
    text-align:center;
    text-transform:uppercase;
  }}

  .items-table {{
    width:100%;
    border-collapse:collapse;
    table-layout:fixed;
  }}

  .items-table th {{
    padding:7px 4px;
    border-bottom:1px solid rgba(31,107,45,.14);
    color:#4f594f;
    font-family:Georgia,"Times New Roman",serif;
    font-size:10px;
    text-align:left;
  }}

  .items-table th:nth-child(2),
  .items-table td:nth-child(2) {{
    width:48px;
    text-align:center;
  }}

  .items-table th:nth-child(3),
  .items-table td:nth-child(3) {{
    width:76px;
    text-align:right;
  }}

  .order-line td {{
    padding:9px 4px;
    border-bottom:1px dashed rgba(96,99,88,.22);
    vertical-align:top;
  }}

  .article-name {{
    color:#283229;
    font-family:Georgia,"Times New Roman",serif;
    font-size:12px;
    font-weight:700;
    line-height:1.3;
  }}

  .qty-cell,
  .price-cell {{
    color:#4c554e;
    font-size:11px;
    font-weight:700;
  }}

  .item-extra {{
    margin-top:4px;
    color:#767f76;
    font-size:9px;
    line-height:1.4;
  }}

  .item-removed {{ color:#aa5146; }}
  .item-choices strong {{ color:#566457; }}
  .item-choices .sub {{ color:#8a918a; }}

  .empty-items {{
    padding:20px 5px!important;
    color:#7b847d;
    text-align:center!important;
    font-size:11px;
  }}

  .breakdown {{
    margin-top:15px;
    padding-top:11px;
    border-top:1px dashed rgba(109,98,69,.42);
  }}

  .breakdown-row {{
    padding:4px 0;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:15px;
    color:#727a72;
    font-size:10px;
  }}

  .breakdown-row strong {{ color:#3e4840; }}

  .total-row {{
    margin-top:8px;
    padding-top:12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:18px;
    border-top:1px solid rgba(31,107,45,.16);
    color:var(--dark);
    font-family:Georgia,"Times New Roman",serif;
    font-size:16px;
    font-weight:900;
  }}

  .total-row strong {{
    color:var(--green);
    font-size:24px;
    white-space:nowrap;
  }}

  .receipt-note {{
    margin-top:16px;
    padding:11px 12px;
    display:flex;
    align-items:flex-start;
    gap:9px;
    border:1px solid rgba(196,125,14,.14);
    border-radius:11px;
    background:#fff8e7;
    color:#6f6550;
  }}

  .note-icon {{
    color:var(--gold);
    font-size:16px;
  }}

  .receipt-note strong {{
    color:#7d5b10;
    font-size:10px;
    text-transform:uppercase;
    letter-spacing:.08em;
  }}

  .receipt-note p {{
    margin:3px 0 0;
    font-size:10px;
    line-height:1.45;
  }}

  .thanks {{
    margin-top:19px;
    color:#bf830e;
    font-family:"Brush Script MT","Segoe Script",cursive;
    font-size:17px;
    text-align:center;
  }}

  .standalone-actions {{
    width:min(100%,520px);
    margin:16px auto 0;
  }}

  .print-btn {{
    width:100%;
    min-height:46px;
    border:0;
    border-radius:13px;
    background:linear-gradient(135deg,var(--green),#318b42);
    color:white;
    font-size:12px;
    font-weight:850;
    cursor:pointer;
    box-shadow:0 10px 24px rgba(31,107,45,.18);
  }}

  html.in-modal .standalone-actions {{
    display:none;
  }}

  @media(max-width:520px) {{
    body {{ padding:16px 8px 24px; }}
    .receipt {{ padding:29px 18px 24px; }}
    .brand-line {{ width:34px; }}
    .brand img {{ width:82px; height:64px; }}
    .info-row {{ grid-template-columns:26px 92px minmax(0,1fr); }}
    .info-label {{ font-size:9.5px; }}
    .info-value {{ font-size:10.5px; }}
    .items-table th:nth-child(2),
    .items-table td:nth-child(2) {{ width:38px; }}
    .items-table th:nth-child(3),
    .items-table td:nth-child(3) {{ width:66px; }}
    .total-row strong {{ font-size:21px; }}
  }}

  @media print {{
    body {{ padding:0; background:white; }}
    .receipt {{
      width:100%;
      max-width:none;
      border:0;
      box-shadow:none;
    }}
    .receipt::before,
    .receipt::after {{
      display:none;
    }}
    .standalone-actions {{
      display:none!important;
    }}
  }}
</style>
</head>
<body>
  <main class="receipt">
    <div class="brand">
      <span class="brand-line"></span>
      <img src="/images/logoMissChawarma.png" alt="Miss Chawarma"
           onerror="this.style.display='none'">
      <span class="brand-line"></span>
    </div>

    <div class="receipt-label"
         data-fr="Reçu de commande"
         data-en="Order receipt">
      Reçu de commande
    </div>

    <div class="ticket-number">#{order.id}</div>
    <div class="section-dash"></div>

    <section class="info-grid">
      <div class="info-row">
        <span class="info-icon">♙</span>
        <span class="info-label" data-fr="Client" data-en="Customer">Client</span>
        <span class="info-value">{escape(order.customer_name or "Client")}</span>
      </div>

      <div class="info-row">
        <span class="info-icon">☎</span>
        <span class="info-label" data-fr="Téléphone" data-en="Phone">Téléphone</span>
        <span class="info-value">{escape(order.customer_phone or "—")}</span>
      </div>

      <div class="info-row">
        <span class="info-icon">▣</span>
        <span class="info-label" data-fr="Mode de réception" data-en="Reception">Mode de réception</span>
        <span class="info-value"
              data-fr="{escape(reception_fr)}"
              data-en="{escape(reception_en)}">{escape(reception_fr)}</span>
      </div>

      <div class="info-row">
        <span class="info-icon">▤</span>
        <span class="info-label" data-fr="Paiement" data-en="Payment">Paiement</span>
        <span class="info-value payment"
              data-fr="{escape(payment_display_fr)}"
              data-en="{escape(payment_display_en)}">{escape(payment_display_fr)}</span>
      </div>

      <div class="info-row">
        <span class="info-icon">▦</span>
        <span class="info-label" data-fr="Date & heure" data-en="Date & time">Date & heure</span>
        <span class="info-value slot-value">{slot_html}</span>
      </div>

      <div class="info-row">
        <span class="info-icon">⌂</span>
        <span class="info-label" data-fr="Destination" data-en="Destination">Destination</span>
        <span class="info-value"
              data-fr="{escape(destination)}"
              data-en="{escape(destination_en)}">{escape(destination)}</span>
      </div>
    </section>

    <div class="section-dash"></div>

    <div class="details-title"
         data-fr="Détails de la commande"
         data-en="Order details">
      Détails de la commande
    </div>

    <table class="items-table">
      <thead>
        <tr>
          <th data-fr="Article" data-en="Item">Article</th>
          <th data-fr="Qté" data-en="Qty">Qté</th>
          <th data-fr="Prix" data-en="Price">Prix</th>
        </tr>
      </thead>
      <tbody>
        {items_html}
      </tbody>
    </table>

    <div class="breakdown">
      {breakdown_html}
      <div class="total-row">
        <span data-fr="TOTAL" data-en="TOTAL">TOTAL</span>
        <strong>{money(order.total)}</strong>
      </div>
    </div>

    {note_html}

    <div class="thanks"
         data-fr="Merci pour votre commande ! ♡"
         data-en="Thank you for your order! ♡">
      Merci pour votre commande ! ♡
    </div>
  </main>

  <div class="standalone-actions">
    <button class="print-btn" type="button" onclick="window.print()"
            data-fr="Imprimer le reçu" data-en="Print receipt">
      Imprimer le reçu
    </button>
  </div>

<script>
(function(){{
  if (window.self !== window.top) {{
    document.documentElement.classList.add('in-modal');
  }}

  var lang = localStorage.getItem('mc_admin_lang') || 'fr';
  document.documentElement.lang = lang;

  document.querySelectorAll('[data-fr][data-en]').forEach(function(el){{
    var value = el.getAttribute(lang === 'en' ? 'data-en' : 'data-fr');
    if (value != null) el.textContent = value;
  }});
}})();
</script>
</body>
</html>
"""
            return HTMLResponse(html)
        finally:
            db.close()


    return admin
