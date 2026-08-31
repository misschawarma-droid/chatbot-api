"""Thème premium Miss Chawarma pour SQLAdmin."""

MISS_CHAWARMA_ADMIN_CSS = r'''
<style id="miss-chawarma-admin-theme">
:root{
  --mc-green:#1f6b2d;--mc-green-2:#318b42;--mc-dark:#123f1d;--mc-dark-2:#092b12;
  --mc-gold:#c47d0e;--mc-gold-2:#e4b83f;--mc-cream:#f7f0e4;--mc-paper:#fffdf8;
  --mc-text:#243126;--mc-muted:#7a817b;--mc-border:rgba(31,107,45,.14);
  --mc-shadow:0 22px 60px rgba(18,63,29,.12);
  --tblr-primary:#1f6b2d!important;--tblr-primary-rgb:31,107,45!important;
  --tblr-link-color:#1f6b2d!important;--tblr-link-hover-color:#c47d0e!important;
  --tblr-navbar-border-color:transparent!important;
}
html,body,.page,.page-wrapper,.page-body{
  background:radial-gradient(circle at 91% 7%,rgba(196,125,14,.12),transparent 27rem),
             radial-gradient(circle at 8% 88%,rgba(31,107,45,.09),transparent 31rem),
             var(--mc-cream)!important;color:var(--mc-text)!important
}
body{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif!important}
.page-wrapper{margin-left:228px!important}.page-body{padding-top:96px!important}.container-xl{max-width:1420px!important}

/* TOPBAR */
.mc-topbar{position:fixed;top:0;left:228px;right:0;height:68px;z-index:1050;display:flex;align-items:center;
justify-content:space-between;padding:0 28px;background:rgba(255,253,248,.88);border-bottom:1px solid rgba(31,107,45,.10);
box-shadow:0 10px 35px rgba(18,63,29,.06);backdrop-filter:blur(14px)}
.mc-topbar-brand,.mc-topbar-actions{display:flex;align-items:center;gap:12px}.mc-topbar-actions{gap:10px}
.mc-topbar-orb{width:34px;height:34px;border-radius:12px;display:grid;place-items:center;overflow:hidden;background:transparent;
color:var(--mc-dark);font-family:Georgia,serif;font-weight:800;box-shadow:0 8px 20px rgba(196,125,14,.24);animation:mcPulse 3.4s ease-in-out infinite}
.mc-topbar-orb img{width:100%;height:100%;object-fit:cover;display:block}
.mc-topbar-title{color:var(--mc-dark);font-family:Georgia,serif;font-size:17px;font-weight:700}.mc-topbar-subtitle{color:var(--mc-muted);font-size:11px}
.mc-lang-switch{display:inline-flex;padding:3px;border:1px solid rgba(31,107,45,.16);border-radius:999px;background:white}
.mc-lang-switch button{border:0;padding:7px 13px;border-radius:999px;background:transparent;color:var(--mc-dark);font-size:11px;font-weight:800;cursor:pointer}
.mc-lang-switch button.mc-active{color:white;background:linear-gradient(135deg,var(--mc-green),var(--mc-green-2))}
.mc-topbar-link,.mc-topbar-logout{min-height:40px;display:inline-flex;align-items:center;gap:8px;padding:0 15px;border:1px solid rgba(31,107,45,.17);
border-radius:999px;background:white;color:var(--mc-dark)!important;font-size:12px;font-weight:750;text-decoration:none!important;transition:.2s}
.mc-topbar-link:hover,.mc-topbar-logout:hover{color:white!important;border-color:var(--mc-green);background:var(--mc-green);transform:translateY(-1px)}

/* SIDEBAR — design compact Miss Chawarma */
.navbar-vertical,
.navbar-expand-lg.navbar-vertical,
.navbar-vertical .container-fluid,
.navbar-vertical .navbar-collapse,
.navbar-vertical .navbar-menu,
.navbar-vertical .navbar-nav,
.navbar-vertical .dropdown-menu{
  background:linear-gradient(180deg,#0f4a2a 0%,#0b3d23 56%,#07341d 100%)!important;
  background-color:#0b3d23!important;
  border:0!important;
}

.navbar-vertical{
  position:fixed!important;
  inset:0 auto 0 0!important;
  width:228px!important;
  height:100vh!important;
  z-index:1040!important;
  display:flex!important;
  flex-direction:column!important;
  overflow:hidden!important;
  border-radius:0 0 0 0!important;
  box-shadow:12px 0 32px rgba(9,43,18,.16)!important;
}

/* enlève les séparateurs SQLAdmin natifs */
.navbar-vertical hr,
.navbar-vertical .navbar-brand+hr,
.navbar-vertical .navbar-collapse>hr,
.navbar-vertical::before,
.navbar-vertical .navbar-collapse::before,
.navbar-vertical .navbar-nav::before{
  display:none!important;
  content:none!important;
}

.navbar-vertical .container-fluid{
  position:relative!important;
  height:100%!important;
  display:flex!important;
  flex-direction:column!important;
  padding:0!important;
  overflow:hidden!important;
}

/* décoration végétale discrète en bas */
.navbar-vertical .container-fluid::after{
  content:"";
  position:absolute;
  left:-28px;
  bottom:64px;
  width:150px;
  height:210px;
  pointer-events:none;
  opacity:.26;
  background:
    radial-gradient(ellipse at 38% 84%,rgba(209,170,78,.9) 0 8px,transparent 9px),
    radial-gradient(ellipse at 55% 72%,rgba(209,170,78,.8) 0 11px,transparent 12px),
    radial-gradient(ellipse at 28% 60%,rgba(209,170,78,.65) 0 9px,transparent 10px),
    radial-gradient(ellipse at 64% 49%,rgba(209,170,78,.55) 0 10px,transparent 11px);
  transform:rotate(-20deg);
}

/* bloc logo */
.navbar-vertical .navbar-brand{
  min-height:165px!important;
  padding:22px 18px 16px!important;
  display:flex!important;
  flex-direction:column!important;
  align-items:center!important;
  justify-content:flex-start!important;
  color:#fffdf8!important;
  background:transparent!important;
  font-family:Georgia,"Times New Roman",serif!important;
  font-size:18px!important;
  font-weight:700!important;
  line-height:1.15!important;
  text-align:center!important;
  border:0!important;
}

.navbar-vertical .navbar-brand::before{
  content:"";
  width:70px!important;
  height:70px!important;
  margin:0 0 13px!important;
  display:block!important;
  flex:0 0 auto!important;
  border-radius:20px!important;
  background:url('/images/logoMissChawarma.png') center/cover no-repeat!important;
  box-shadow:0 8px 18px rgba(0,0,0,.16)!important;
  animation:none!important;
}

.navbar-vertical .navbar-brand::after{
  content:"ADMINISTRATION";
  display:block!important;
  margin-top:8px!important;
  color:#e6bd46!important;
  font-family:Inter,Arial,sans-serif!important;
  font-size:8px!important;
  font-weight:900!important;
  letter-spacing:.24em!important;
  line-height:1!important;
}

/* menu */
.navbar-vertical .navbar-collapse{
  flex:1 1 auto!important;
  min-height:0!important;
  padding:7px 12px 82px!important;
  display:flex!important;
  flex-direction:column!important;
  overflow:hidden!important;
}

.navbar-vertical .navbar-nav{
  flex:1 1 auto!important;
  min-height:0!important;
  width:100%!important;
  padding:0!important;
  margin:0!important;
  display:flex!important;
  flex-direction:column!important;
  gap:6px!important;
  overflow-y:auto!important;
  scrollbar-width:none!important;
}

.navbar-vertical .navbar-nav::-webkit-scrollbar{display:none!important}
.navbar-vertical .nav-item{margin:0!important;border:0!important;background:transparent!important}

.navbar-vertical .nav-link{
  min-height:43px!important;
  margin:0!important;
  padding:10px 11px!important;
  display:flex!important;
  align-items:center!important;
  gap:11px!important;
  border:0!important;
  border-radius:13px!important;
  color:rgba(255,255,255,.90)!important;
  background:transparent!important;
  font-size:12px!important;
  font-weight:700!important;
  line-height:1.2!important;
  text-decoration:none!important;
  transition:background .18s ease,transform .18s ease!important;
}

.navbar-vertical .nav-link:hover{
  color:#fff!important;
  background:rgba(255,255,255,.08)!important;
  transform:none!important;
}

.navbar-vertical .nav-item.active>.nav-link,
.navbar-vertical .nav-link.active,
.navbar-vertical .nav-link[aria-current="page"]{
  color:#fff!important;
  background:linear-gradient(135deg,rgba(107,173,103,.34),rgba(255,255,255,.10))!important;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.06)!important;
}

.navbar-vertical .nav-link-icon,
.navbar-vertical .nav-link i,
.navbar-vertical .nav-link svg{
  width:21px!important;
  height:21px!important;
  min-width:21px!important;
  color:#fff!important;
  fill:none!important;
  stroke:currentColor!important;
  background:transparent!important;
  opacity:1!important;
}

/* garde le logout natif caché, topbar inchangée */
.navbar-vertical .mt-auto,
.navbar-vertical a[href*="logout"].btn{
  display:none!important;
}

/* petit "compte" visuel en bas, sans modifier le HTML */
.navbar-vertical::after{
  content:"MC   Miss Chawarma";
  position:absolute;
  left:13px;
  right:13px;
  bottom:14px;
  height:48px;
  display:flex;
  align-items:center;
  padding:0 14px;
  border:1px solid rgba(255,255,255,.13);
  border-radius:14px;
  background:rgba(255,255,255,.035);
  color:rgba(255,255,255,.92);
  font-size:10px;
  font-weight:800;
  letter-spacing:.01em;
  pointer-events:none;
}

/* DASHBOARD */
.mc-dashboard{max-width:1260px;margin:0 auto;padding:4px 10px 55px;animation:mcPageIn .65s cubic-bezier(.2,.8,.2,1) both}
.mc-dashboard-hero{position:relative;overflow:hidden;min-height:285px;padding:44px 46px;display:flex;align-items:center;border:1px solid rgba(31,107,45,.13);
border-radius:30px;background:linear-gradient(118deg,rgba(255,253,248,.98),rgba(247,240,228,.96) 55%,rgba(238,224,186,.78));box-shadow:var(--mc-shadow)}
.mc-dashboard-hero::before,.mc-dashboard-hero::after{content:"";position:absolute;border-radius:50%;animation:mcBreathe 5.2s ease-in-out infinite}
.mc-dashboard-hero::before{width:390px;height:390px;right:-120px;top:-170px;background:radial-gradient(circle,rgba(196,125,14,.22),rgba(196,125,14,0) 68%)}
.mc-dashboard-hero::after{width:230px;height:230px;right:90px;bottom:-150px;background:radial-gradient(circle,rgba(31,107,45,.20),rgba(31,107,45,0) 68%);animation-direction:reverse}
.mc-hero-content{position:relative;z-index:2;max-width:720px}.mc-eyebrow{margin-bottom:13px;color:var(--mc-gold);font-size:11px;font-weight:850;letter-spacing:.20em;text-transform:uppercase}
.mc-dashboard h1{margin:0;color:var(--mc-dark);font-family:Georgia,serif;font-size:clamp(38px,5vw,66px);font-weight:500;line-height:1.02;letter-spacing:-.04em}.mc-dashboard h1 span{color:var(--mc-gold)}
.mc-hero-copy{max-width:650px;margin:19px 0 26px;color:#657067;font-size:15px;line-height:1.7}.mc-hero-actions{display:flex;flex-wrap:wrap;gap:12px}
.mc-hero-button{min-height:48px;padding:0 20px;display:inline-flex;align-items:center;gap:9px;border-radius:15px;color:white!important;
background:linear-gradient(135deg,var(--mc-green),var(--mc-green-2));font-size:13px;font-weight:800;text-decoration:none!important;box-shadow:0 13px 30px rgba(31,107,45,.22);transition:.2s}
.mc-hero-button:hover{color:white!important;transform:translateY(-3px);box-shadow:0 18px 35px rgba(31,107,45,.28)}
.mc-hero-button.mc-secondary{color:var(--mc-dark)!important;border:1px solid rgba(31,107,45,.16);background:rgba(255,255,255,.72);box-shadow:none}
.mc-stats-grid{margin-top:24px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.mc-stat-card{min-height:150px;padding:22px;border:1px solid rgba(31,107,45,.12);border-radius:22px;background:rgba(255,253,248,.92);
box-shadow:0 15px 40px rgba(18,63,29,.08);transition:.22s;animation:mcCardIn .65s ease both}.mc-stat-card:nth-child(2){animation-delay:.08s}.mc-stat-card:nth-child(3){animation-delay:.16s}.mc-stat-card:nth-child(4){animation-delay:.24s}
.mc-stat-card:hover{transform:translateY(-5px);box-shadow:0 22px 48px rgba(18,63,29,.13)}
.mc-stat-icon{width:42px;height:42px;display:grid;place-items:center;border-radius:14px;color:var(--mc-green);background:rgba(31,107,45,.09);font-size:18px}
.mc-stat-value{margin-top:17px;color:var(--mc-dark);font-family:Georgia,serif;font-size:34px;line-height:1}.mc-stat-label{margin-top:8px;color:var(--mc-muted);font-size:12px;font-weight:650}
.mc-dashboard-bottom{margin-top:24px;display:grid;grid-template-columns:1.25fr .75fr;gap:18px}.mc-panel{padding:25px;border:1px solid rgba(31,107,45,.12);border-radius:24px;background:rgba(255,253,248,.94);box-shadow:0 15px 40px rgba(18,63,29,.08)}
.mc-panel-title{color:var(--mc-dark);font-family:Georgia,serif;font-size:22px}.mc-panel-copy{margin-top:8px;color:var(--mc-muted);font-size:13px;line-height:1.6}
.mc-quick-grid{margin-top:18px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.mc-quick-link{min-height:70px;padding:15px;display:flex;align-items:center;gap:12px;border:1px solid rgba(31,107,45,.12);
border-radius:16px;color:var(--mc-dark)!important;background:white;font-size:13px;font-weight:750;text-decoration:none!important;transition:.2s}.mc-quick-link:hover{color:var(--mc-dark)!important;border-color:rgba(196,125,14,.35);background:#fffaf0;transform:translateY(-2px)}
.mc-clock{margin-top:20px;color:var(--mc-dark);font-family:Georgia,serif;font-size:38px}.mc-date{margin-top:5px;color:var(--mc-gold);font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}

/* Existing SQLAdmin */
.card{overflow:hidden!important;background:rgba(255,253,248,.97)!important;border:1px solid var(--mc-border)!important;border-radius:24px!important;box-shadow:var(--mc-shadow)!important;animation:mcPageIn .55s ease both}
.card-header{min-height:92px!important;padding:23px 28px!important;background:linear-gradient(100deg,rgba(255,253,248,.99),rgba(245,233,202,.54))!important;border-bottom:1px solid var(--mc-border)!important}
.card-title{color:var(--mc-dark)!important;font-family:Georgia,serif!important;font-size:29px!important;font-weight:500!important}.card-title::after{content:"";display:block;width:48px;height:3px;margin-top:10px;border-radius:999px;background:linear-gradient(90deg,var(--mc-gold),var(--mc-gold-2))}
.card-body{background:rgba(255,253,248,.96)!important}.card-footer{border-top:1px solid var(--mc-border)!important;background:rgba(247,240,228,.58)!important}
.btn{min-height:44px!important;border-radius:13px!important;font-weight:750!important;transition:.18s!important}.btn:hover{transform:translateY(-1px)}
.btn-primary{border-color:var(--mc-green)!important;background:linear-gradient(135deg,var(--mc-green),var(--mc-green-2))!important}.btn-secondary{border-color:rgba(196,125,14,.30)!important;background:#f7edcf!important;color:#795005!important}
.form-control,.form-select,.select2-selection,.ts-control{min-height:45px!important;border:1px solid rgba(31,107,45,.20)!important;border-radius:14px!important;background:white!important;color:var(--mc-text)!important;box-shadow:none!important}
.form-control:focus,.form-select:focus,.ts-control.focus{border-color:var(--mc-green)!important;box-shadow:0 0 0 4px rgba(31,107,45,.10)!important}
.table-responsive{background:var(--mc-paper)!important}.table{--tblr-table-border-color:rgba(31,107,45,.10)!important;color:var(--mc-text)!important}.table thead th{padding-top:17px!important;padding-bottom:17px!important;background:#f2eee4!important;color:var(--mc-dark)!important;font-size:11px!important;font-weight:850!important;letter-spacing:.075em!important;text-transform:uppercase!important}.table tbody td{padding-top:16px!important;padding-bottom:16px!important;vertical-align:middle!important}.table tbody tr:nth-child(even){background:rgba(247,240,228,.52)!important}.table tbody tr:hover{background:rgba(234,242,232,.92)!important;box-shadow:inset 4px 0 0 var(--mc-gold)!important}.table a{color:var(--mc-green)!important}.table td a[data-bs-target*="delete"],.table td a[href*="/delete"]{color:#c33d36!important}
.pagination .page-item.active .page-link{border-color:var(--mc-green)!important;color:white!important;background:var(--mc-green)!important}


/* =========================================================
   ORDER ITEM — PERSONNALISATION LISIBLE
   Remplace visuellement le JSON brut par des lignes propres.
========================================================= */
.mc-empty-value{color:#9aa0aa!important}
.mc-personalization-summary{
  min-width:220px;
  max-width:520px;
  display:grid;
  gap:8px;
}
.mc-personalization-row{
  padding:9px 11px;
  display:grid;
  grid-template-columns:minmax(86px,.7fr) minmax(0,1.6fr);
  gap:10px;
  align-items:start;
  border:1px solid rgba(31,107,45,.09);
  border-radius:12px;
  background:linear-gradient(145deg,#f7fbf5,#fffaf0);
}
.mc-personalization-label{
  color:#56705c;
  font-size:10px;
  font-weight:900;
  letter-spacing:.06em;
  text-transform:uppercase;
}
.mc-personalization-content{min-width:0}
.mc-personalization-value{
  display:block;
  color:#183f22;
  font-size:12px;
  font-weight:800;
  line-height:1.4;
  overflow-wrap:anywhere;
}
.mc-personalization-extra{
  margin-top:4px;
  color:#7a817b;
  font-size:10.5px;
  font-weight:650;
  line-height:1.4;
}
.mc-without-list{display:flex;flex-wrap:wrap;gap:6px}
.mc-without-chip{
  padding:5px 9px;
  border:1px solid rgba(196,125,14,.18);
  border-radius:999px;
  background:#fff3cf;
  color:#8c6200;
  font-size:10.5px;
  font-weight:800;
}
@media(max-width:575.98px){
  .mc-personalization-summary{min-width:0!important;max-width:100%!important;width:100%!important}
  .mc-personalization-row{grid-template-columns:1fr!important;gap:5px!important;padding:9px!important}
}


/* =========================================================
   SIDEBAR EXACTE — structure custom, proche de la référence
========================================================= */
.mc-sidebar-custom{
  height:100%;
  display:flex;
  flex-direction:column;
  background:linear-gradient(180deg,#0f4b2b 0%,#0c4326 56%,#07351e 100%);
  color:#fff;
  overflow:hidden;
}

.mc-sidebar-head{
  flex:0 0 auto;
  padding:22px 18px 16px;
  display:flex;
  flex-direction:column;
  align-items:center;
  text-align:center;
}

.mc-sidebar-logo{
  width:72px;
  height:72px;
  border-radius:20px;
  object-fit:cover;
  display:block;
  box-shadow:0 8px 20px rgba(0,0,0,.16);
}

.mc-sidebar-name{
  margin-top:12px;
  color:#fffdf8;
  font-family:Georgia,"Times New Roman",serif;
  font-size:18px;
  font-weight:700;
  line-height:1.1;
}

.mc-sidebar-role{
  margin-top:7px;
  color:#e4b83f;
  font-size:8px;
  font-weight:900;
  letter-spacing:.24em;
}

.mc-sidebar-menu{
  flex:1 1 auto;
  min-height:0;
  padding:10px 13px 92px;
  display:flex;
  flex-direction:column;
  gap:6px;
  overflow-y:auto;
  scrollbar-width:none;
}
.mc-sidebar-menu::-webkit-scrollbar{display:none}

.mc-sidebar-link{
  min-height:45px;
  padding:10px 12px;
  display:flex;
  align-items:center;
  gap:12px;
  border-radius:13px;
  color:rgba(255,255,255,.92)!important;
  text-decoration:none!important;
  font-size:12px;
  font-weight:750;
  transition:background .18s ease, transform .18s ease;
}

.mc-sidebar-link:hover{
  color:white!important;
  background:rgba(255,255,255,.08);
  transform:none;
}

.mc-sidebar-link.mc-active{
  color:white!important;
  background:linear-gradient(135deg,rgba(102,168,96,.38),rgba(255,255,255,.10));
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.06);
}

.mc-sidebar-icon{
  width:24px;
  min-width:24px;
  height:24px;
  display:grid;
  place-items:center;
  color:white;
}
.mc-sidebar-icon svg{
  width:21px!important;
  height:21px!important;
  stroke:currentColor!important;
  fill:none!important;
}

.mc-sidebar-leaves{
  position:absolute;
  left:-18px;
  bottom:58px;
  width:150px;
  height:190px;
  pointer-events:none;
  opacity:.34;
  background:
    radial-gradient(ellipse at 28% 78%,rgba(215,176,79,.95) 0 10px,transparent 11px),
    radial-gradient(ellipse at 46% 66%,rgba(215,176,79,.80) 0 13px,transparent 14px),
    radial-gradient(ellipse at 24% 53%,rgba(215,176,79,.66) 0 10px,transparent 11px),
    radial-gradient(ellipse at 58% 43%,rgba(215,176,79,.55) 0 12px,transparent 13px);
  transform:rotate(-22deg);
}

.mc-sidebar-account{
  position:absolute;
  left:13px;
  right:13px;
  bottom:13px;
  height:49px;
  padding:0 12px;
  display:flex;
  align-items:center;
  gap:9px;
  border:1px solid rgba(255,255,255,.14);
  border-radius:14px;
  background:rgba(255,255,255,.035);
  color:#fff;
}

.mc-sidebar-avatar{
  width:29px;
  height:29px;
  display:grid;
  place-items:center;
  border-radius:50%;
  background:rgba(103,171,105,.55);
  font-size:9px;
  font-weight:900;
}

.mc-sidebar-account-name{
  flex:1;
  font-size:10px;
  font-weight:800;
}

.mc-sidebar-chevron{
  font-size:14px;
  opacity:.9;
}

/* Une fois la structure custom injectée, on neutralise entièrement
   la structure Tabler/SQLAdmin native afin d'éviter le rail bleu,
   le deuxième hamburger et le grand titre. */
.navbar-vertical > .container-fluid{
  padding:0!important;
}
.navbar-vertical .navbar-toggler,
.navbar-vertical button.navbar-toggler,
.navbar-vertical [data-bs-toggle="collapse"]{
  display:none!important;
}

@media(min-width:992px){
  .navbar-vertical{
    width:228px!important;
  }
  .page-wrapper{margin-left:228px!important}
  .mc-topbar{left:228px!important}
}

@media(max-width:991.98px){
  .navbar-vertical{
    width:235px!important;
    max-width:235px!important;
    border-radius:0 0 24px 0!important;
  }
  .mc-sidebar-head{
    padding:18px 15px 13px;
  }
  .mc-sidebar-logo{
    width:64px;
    height:64px;
    border-radius:18px;
  }
  .mc-sidebar-name{
    margin-top:10px;
    font-size:16px;
  }
  .mc-sidebar-role{
    font-size:7px;
  }
  .mc-sidebar-menu{
    padding:7px 11px 82px;
    gap:5px;
  }
  .mc-sidebar-link{
    min-height:42px;
    padding:9px 10px;
    gap:10px;
    font-size:11px;
  }
  .mc-sidebar-icon{
    width:22px;
    min-width:22px;
  }
}

/* =========================================================
   ARTICLES COMMANDÉS — cartes mobiles plus claires et plus
   compactes, dans le même esprit que les tickets commandes.
========================================================= */
@media(max-width:575.98px){
  .card.mc-order-item-card-mode .mc-mobile-cards{
    display:flex!important;
    flex-direction:column!important;
    gap:12px!important;
    padding:10px 8px 18px!important;
  }

  .card.mc-order-item-card-mode .mc-order-group{
    margin:0!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:24px!important;
    background:linear-gradient(180deg,#fffefb 0%,#fcfaf4 100%)!important;
    box-shadow:0 10px 22px rgba(18,63,29,.055)!important;
    overflow:hidden!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-header{
    padding:14px 16px!important;
    background:linear-gradient(90deg,#f1f7ef 0%,#fff9ed 100%)!important;
    border-bottom:1px solid rgba(31,107,45,.08)!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-title{
    color:#194627!important;
    font-size:17px!important;
    font-weight:900!important;
    line-height:1.2!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-count{
    padding:8px 12px!important;
    border-radius:999px!important;
    background:#fff!important;
    border:1px solid rgba(31,107,45,.10)!important;
    color:#68746b!important;
    font-size:11px!important;
    font-weight:850!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-items{
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:12px!important;
    padding:12px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card{
    min-height:0!important;
    height:auto!important;
    border-radius:22px!important;
    overflow:hidden!important;
    background:#fffdf9!important;
    border:1px solid rgba(31,107,45,.09)!important;
    box-shadow:0 6px 18px rgba(18,63,29,.045)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card::before{
    width:5px!important;
    opacity:1!important;
    background:linear-gradient(180deg,#2f7a25 0%,#d6a400 100%)!important;
    border-radius:0 6px 6px 0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-summary{
    min-height:0!important;
    height:auto!important;
    padding:16px 16px 14px 18px!important;
    display:block!important;
    background:transparent!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-main{
    width:100%!important;
    min-height:0!important;
    height:auto!important;
    display:block!important;
    text-align:left!important;
    padding:0 58px 0 0!important;
    border:0!important;
    background:transparent!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-title{
    margin:0 0 12px!important;
    color:#214b29!important;
    font-size:17px!important;
    font-weight:900!important;
    line-height:1.28!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-subtitle,
  .card.mc-order-item-card-mode .mc-mobile-card-quick{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-chevron{
    top:16px!important;
    right:16px!important;
    width:46px!important;
    height:46px!important;
    border-radius:14px!important;
    border:1px solid rgba(212,177,72,.42)!important;
    background:linear-gradient(180deg,#fff5db 0%,#f7e7b4 100%)!important;
    color:#936200!important;
    box-shadow:0 6px 16px rgba(212,177,72,.18)!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-inline-metrics{
    display:flex!important;
    align-items:center!important;
    gap:8px!important;
    flex-wrap:wrap!important;
    margin:0 0 8px!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-chip{
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    padding:7px 11px!important;
    border-radius:999px!important;
    border:1px solid rgba(31,107,45,.12)!important;
    background:#edf5eb!important;
    color:#2f6938!important;
    font-size:12px!important;
    font-weight:850!important;
    line-height:1!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-chip.mc-order-item-chip-price{
    background:#fff5dc!important;
    border-color:rgba(212,177,72,.45)!important;
    color:#a67300!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-note{
    margin-top:6px!important;
    color:#6e766e!important;
    font-size:11.5px!important;
    font-weight:650!important;
    line-height:1.42!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-note strong{
    color:#58655c!important;
    font-weight:900!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-details{
    padding:0 12px 12px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-grid{
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:10px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row{
    min-height:84px!important;
    padding:14px!important;
    border-radius:18px!important;
    border:1px solid rgba(31,107,45,.08)!important;
    background:linear-gradient(180deg,#fffefc 0%,#fbfaf5 100%)!important;
    box-shadow:none!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-label{
    padding:0!important;
    color:#7a847b!important;
    font-size:10px!important;
    font-weight:850!important;
    letter-spacing:.10em!important;
    line-height:1.2!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-value{
    color:#26372b!important;
    font-size:14px!important;
    font-weight:750!important;
    line-height:1.42!important;
    overflow-wrap:anywhere!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-order,
  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-note,
  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-options{
    grid-column:1 / -1!important;
    min-height:0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-qty .mc-mobile-detail-value,
  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-price .mc-mobile-detail-value{
    font-size:23px!important;
    font-weight:900!important;
    line-height:1.05!important;
    letter-spacing:-.02em!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row.mc-order-item-detail-price .mc-mobile-detail-value{
    color:#b07d00!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-actions{
    display:flex!important;
    justify-content:flex-start!important;
    gap:10px!important;
    padding-top:12px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-actions a,
  .card.mc-order-item-card-mode .mc-mobile-card-actions button{
    width:52px!important;
    height:52px!important;
    border-radius:16px!important;
  }

  .card.mc-dish-list-card-mode .mc-mobile-record-card{
    min-height:0!important;
  }

  .card.mc-dish-list-card-mode .mc-mobile-card-summary{
    min-height:172px!important;
  }
}

@media(min-width:431px) and (max-width:575.98px){
  .card.mc-order-item-card-mode .mc-order-group-items{
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
  }
}

@media(max-width:430px){
  .card.mc-order-item-card-mode .mc-mobile-card-grid{
    grid-template-columns:1fr!important;
  }
}

</style>
'''

ORDER_TICKET_MODAL_HTML = """
<style id="mc-order-ticket-modal-style">
  .order-ticket-overlay{
    display:none;
    position:fixed;
    inset:0;
    z-index:9999;
    padding:22px;
    align-items:center;
    justify-content:center;
    background:rgba(13,29,18,.58);
    backdrop-filter:blur(6px);
    -webkit-backdrop-filter:blur(6px);
  }

  .order-ticket-overlay.open{
    display:flex;
    animation:mcTicketOverlayIn .18s ease both;
  }

  .order-ticket-modal{
    position:relative;
    width:min(650px,96vw);
    height:min(900px,94vh);
    min-height:520px;
    padding:16px;
    display:flex;
    flex-direction:column;
    gap:12px;
    overflow:visible;
    border:1px solid rgba(255,255,255,.22);
    border-radius:24px;
    background:
      radial-gradient(circle at 96% 0,rgba(228,184,63,.17),transparent 210px),
      linear-gradient(145deg,#f5efe4,#ebe7df);
    box-shadow:
      0 36px 100px rgba(7,25,12,.42),
      inset 0 1px 0 rgba(255,255,255,.72);
    animation:mcTicketModalIn .26s cubic-bezier(.2,.8,.2,1) both;
  }

  .order-ticket-frame{
    position:relative;
    flex:1 1 auto;
    min-height:0;
    overflow:hidden;
    scrollbar-width:none;
    border:1px solid rgba(31,107,45,.12);
    border-radius:18px;
    background:#efeae1;
    box-shadow:0 10px 28px rgba(18,63,29,.10);
  }

  .order-ticket-modal iframe{
    width:100%;
    height:100%;
    display:block;
    border:0;
    background:#efeae1;
  }

  .order-ticket-loading{
    position:absolute;
    inset:0;
    z-index:2;
    display:grid;
    place-items:center;
    background:linear-gradient(145deg,#f7f0e4,#efe9dd);
    color:#647066;
    font-size:11px;
    font-weight:800;
    letter-spacing:.04em;
    transition:opacity .18s ease,visibility .18s ease;
  }

  .order-ticket-loading::before{
    content:"";
    width:28px;
    height:28px;
    margin-bottom:42px;
    position:absolute;
    border:3px solid rgba(31,107,45,.15);
    border-top-color:#1f6b2d;
    border-radius:50%;
    animation:mcTicketSpin .7s linear infinite;
  }

  .order-ticket-modal.mc-loaded .order-ticket-loading{
    opacity:0;
    visibility:hidden;
  }

  .order-ticket-close{display:none!important;
    position:absolute;
    top:-14px;
    right:-14px;
    width:44px;
    height:44px;
    z-index:5;
    display:grid;
    place-items:center;
    border:1px solid rgba(31,107,45,.12);
    border-radius:50%;
    background:#fffdf8;
    color:#123f1d;
    box-shadow:0 8px 22px rgba(9,43,18,.18);
    font-size:21px;
    font-weight:500;
    line-height:1;
    cursor:pointer;
    transition:transform .18s ease,background .18s ease,color .18s ease;
  }

  .order-ticket-close:hover{
    color:white;
    background:#1f6b2d;
    transform:rotate(8deg);
  }

  .order-ticket-toolbar{
    flex:0 0 auto;
    min-height:62px;
    padding:8px;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
    border:1px solid rgba(31,107,45,.09);
    border-radius:16px;
    background:rgba(255,253,248,.82);
    box-shadow:0 7px 20px rgba(18,63,29,.07);
  }

  .order-ticket-action{
    min-height:46px;
    padding:0 16px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:8px;
    border:1px solid rgba(31,107,45,.13);
    border-radius:12px;
    background:#fffdf8;
    color:#183f22;
    font-size:11px;
    font-weight:850;
    cursor:pointer;
    transition:transform .18s ease,box-shadow .18s ease,background .18s ease;
  }

  .order-ticket-action:hover{
    transform:translateY(-1px);
    box-shadow:0 7px 18px rgba(18,63,29,.09);
  }

  .order-ticket-action.mc-print{
    border-color:#1f6b2d;
    background:linear-gradient(135deg,#1f6b2d,#318b42);
    color:white;
  }

  @keyframes mcTicketOverlayIn{
    from{opacity:0}
    to{opacity:1}
  }

  @keyframes mcTicketModalIn{
    from{opacity:0;transform:translateY(14px) scale(.975)}
    to{opacity:1;transform:translateY(0) scale(1)}
  }

  @keyframes mcTicketSpin{
    to{transform:rotate(360deg)}
  }

  @media(max-width:575.98px){
    .order-ticket-overlay{
      padding:8px;
      align-items:stretch;
    }

    .order-ticket-modal{
      width:100%;
      height:calc(100dvh - 16px);
      min-height:0;
      padding:10px;
      gap:8px;
      border-radius:19px;
    }

    .order-ticket-frame{
      border-radius:14px;
    }

    .order-ticket-close{display:none!important;
      top:8px;
      right:8px;
      width:38px;
      height:38px;
      font-size:19px;
    }

    .order-ticket-toolbar{
      min-height:56px;
      padding:6px;
      gap:7px;
      border-radius:13px;
    }

    .order-ticket-action{
      min-height:43px;
      padding:0 10px;
      border-radius:10px;
      font-size:10px;
    }
  }
</style>

<div id="order-ticket-overlay"
     class="order-ticket-overlay"
     aria-hidden="true">
  <div id="order-ticket-modal"
       class="order-ticket-modal"
       role="dialog"
       aria-modal="true"
       aria-label="Reçu de commande">


    <div class="order-ticket-frame">
      <div class="order-ticket-loading" id="order-ticket-loading">
        Chargement du reçu…
      </div>
      <iframe id="order-ticket-iframe"
              title="Reçu de commande"
              scrolling="no"
              src=""></iframe>
    </div>

    <div class="order-ticket-toolbar">
      <button class="order-ticket-action"
              type="button"
              onclick="closeOrderTicket()"
              data-ticket-fr="Fermer"
              data-ticket-en="Close">
        ✕ <span>Fermer</span>
      </button>

      <button class="order-ticket-action mc-print"
              type="button"
              onclick="printOrderTicket()"
              data-ticket-fr="Imprimer"
              data-ticket-en="Print">
        ⎙ <span>Imprimer</span>
      </button>
    </div>
  </div>
</div>

<script>
(function(){
  var previousOverflow = "";

  function ticketLang(){
    return localStorage.getItem('mc_admin_lang') || 'fr';
  }

  function translateTicketModal(){
    var lang = ticketLang();

    document.querySelectorAll('[data-ticket-fr][data-ticket-en]').forEach(function(el){
      var text = el.getAttribute(lang === 'en' ? 'data-ticket-en' : 'data-ticket-fr');
      var span = el.querySelector('span');
      if (span) span.textContent = text;
    });

    var loading = document.getElementById('order-ticket-loading');
    if (loading) {
      loading.childNodes.forEach(function(node){
        if (node.nodeType === Node.TEXT_NODE) node.nodeValue = '';
      });
      loading.appendChild(
        document.createTextNode(lang === 'en' ? 'Loading receipt…' : 'Chargement du reçu…')
      );
    }
  }

  window.openOrderTicket = function(orderId){
    var overlay = document.getElementById('order-ticket-overlay');
    var modal = document.getElementById('order-ticket-modal');
    var iframe = document.getElementById('order-ticket-iframe');
    if (!overlay || !modal || !iframe || !orderId) return;

    previousOverflow = document.body.style.overflow || "";
    document.body.style.overflow = "hidden";

    modal.classList.remove('mc-loaded');
    iframe.src = '/order-ticket/' + encodeURIComponent(orderId);

    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden','false');
    translateTicketModal();
  };

  window.closeOrderTicket = function(){
    var overlay = document.getElementById('order-ticket-overlay');
    var modal = document.getElementById('order-ticket-modal');
    var iframe = document.getElementById('order-ticket-iframe');
    if (!overlay || !iframe) return;

    overlay.classList.remove('open');
    overlay.setAttribute('aria-hidden','true');

    document.body.style.overflow = previousOverflow;
    previousOverflow = "";

    setTimeout(function(){
      if (!overlay.classList.contains('open')) {
        iframe.src = '';
        if (modal) modal.classList.remove('mc-loaded');
      }
    }, 180);
  };

  window.printOrderTicket = function(){
    var iframe = document.getElementById('order-ticket-iframe');
    if (!iframe || !iframe.contentWindow) return;
    iframe.contentWindow.focus();
    iframe.contentWindow.print();
  };

  var iframe = document.getElementById('order-ticket-iframe');
  if (iframe) {
    iframe.addEventListener('load', function(){
      var modal = document.getElementById('order-ticket-modal');
      if (iframe.getAttribute('src') && modal) {
        modal.classList.add('mc-loaded');
      }
    });
  }

  /* Capture le clic AVANT le bouton générique des cartes mobiles :
     cliquer sur le ticket ouvre uniquement le reçu et n'ouvre pas
     l'accordéon de détails de la carte. */
  document.addEventListener('click', function(e){
    var trigger = e.target.closest && e.target.closest('.ticket-trigger');
    if (trigger) {
      e.preventDefault();
      e.stopPropagation();
      window.openOrderTicket(trigger.dataset.orderId);
      return;
    }

    if (e.target && e.target.id === 'order-ticket-overlay') {
      window.closeOrderTicket();
    }
  }, true);

  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') window.closeOrderTicket();
  });
})();
</script>
"""

MISS_CHAWARMA_ADMIN_SCRIPT = r'''
<style>
/* =========================================================
   CALENDRIER DES RÉSERVATIONS
   Design compact inspiré de la référence
   IMPORTANT : le reste du dashboard reste inchangé.
========================================================= */

.mc-calendar-panel{
  margin-top:26px;
  padding:18px 18px 20px;
  border:1px solid rgba(31,107,45,.10);
  border-radius:24px;
  background:rgba(255,254,250,.90);
  box-shadow:0 14px 38px rgba(18,63,29,.07);
  animation:mcCardIn .65s ease .12s both;
}

.mc-calendar-header{
  display:flex;
  align-items:flex-start;
  justify-content:space-between;
  gap:18px;
  margin-bottom:12px;
}

.mc-calendar-title{
  color:var(--mc-dark);
  font-family:Georgia,"Times New Roman",serif;
  font-size:24px;
  line-height:1.2;
}

.mc-calendar-title::after{
  content:"";
  display:block;
  width:42px;
  height:3px;
  margin-top:8px;
  border-radius:999px;
  background:linear-gradient(90deg,var(--mc-gold),var(--mc-gold-2));
}

.mc-calendar-subtitle{
  margin-top:8px;
  color:var(--mc-muted);
  font-size:12px;
  line-height:1.5;
}

.mc-calendar-controls{
  display:grid;
  grid-template-columns:48px minmax(160px,1fr) 48px;
  align-items:center;
  gap:8px;
  width:min(100%,520px);
  padding:6px 8px;
  border:1px solid rgba(31,107,45,.10);
  border-radius:18px;
  background:rgba(255,255,255,.88);
  box-shadow:0 6px 18px rgba(18,63,29,.04);
}

.mc-calendar-nav{
  width:42px;
  height:42px;
  display:grid;
  place-items:center;
  border:0;
  border-radius:12px;
  background:#eef5ec;
  color:var(--mc-dark);
  font-size:25px;
  line-height:1;
  cursor:pointer;
  transition:.2s ease;
}

.mc-calendar-nav:hover{
  color:var(--mc-dark);
  background:#e4efe2;
  transform:scale(1.03);
  box-shadow:none;
}

#mc-calendar-prev{justify-self:start}
#mc-calendar-next{justify-self:end}

.mc-calendar-month{
  min-width:0;
  color:var(--mc-dark);
  font-family:Georgia,"Times New Roman",serif;
  font-size:24px;
  font-weight:500;
  text-align:center;
  text-transform:capitalize;
}

.mc-calendar-weekdays,
.mc-calendar-grid{
  display:grid;
  grid-template-columns:repeat(7,minmax(0,1fr));
  gap:8px;
}

.mc-calendar-weekdays{
  margin-bottom:6px;
  padding:0 2px;
}

.mc-calendar-weekday{
  padding:8px 2px;
  color:#607165;
  font-size:9px;
  font-weight:850;
  letter-spacing:.12em;
  text-align:center;
  text-transform:uppercase;
}

.mc-calendar-grid{
  min-height:0;
}

.mc-calendar-day{
  position:relative;
  min-width:0;
  width:100%;
  min-height:78px;
  height:78px;
  padding:8px 9px;
  overflow:hidden;
  border:1px solid rgba(31,107,45,.10);
  border-radius:13px;
  background:rgba(255,255,255,.86);
  color:var(--mc-text);
  cursor:pointer;
  text-align:left;
  box-shadow:none;
  transition:border-color .18s ease,background .18s ease;
}

.mc-calendar-day::before{
  display:none;
}

.mc-calendar-day:hover:not(.mc-empty){
  border-color:rgba(31,107,45,.20);
  background:#fffdf7;
  box-shadow:none;
  transform:none;
}

.mc-calendar-day.mc-empty{
  border-color:transparent;
  background:transparent;
  cursor:default;
  box-shadow:none;
}

.mc-calendar-day.mc-today{
  border-color:rgba(196,125,14,.34);
  background:linear-gradient(145deg,#fffefa,#fff8e3);
  box-shadow:inset 0 0 0 1px rgba(196,125,14,.08);
}

.mc-calendar-day.mc-has-reservations{
  border-color:rgba(31,107,45,.15);
}

.mc-calendar-number{
  position:absolute;
  top:8px;
  left:9px;
  z-index:3;
  display:block;
  width:auto;
  height:auto;
  padding:0;
  border:0;
  border-radius:0;
  background:transparent;
  box-shadow:none;
  color:var(--mc-dark);
  font-size:12px;
  font-weight:850;
  line-height:1;
}

.mc-calendar-day.mc-today .mc-calendar-number{
  color:var(--mc-gold);
}

.mc-calendar-count{
  display:none;
}

.mc-calendar-dot{
  display:none;
}

.mc-calendar-loading,
.mc-calendar-error{
  grid-column:1/-1;
  min-height:250px;
  display:grid;
  place-items:center;
  border:1px dashed rgba(31,107,45,.18);
  border-radius:16px;
  color:var(--mc-muted);
  background:rgba(255,255,255,.55);
  text-align:center;
}

/* Couleurs par type */
.mc-calendar-day.mc-table-only{
  background:linear-gradient(145deg,#ffffff 0%,#edf6ec 100%);
  border-color:rgba(31,107,45,.15);
}

.mc-calendar-day.mc-event-only{
  background:linear-gradient(145deg,#ffffff 0%,#fff4d5 100%);
  border-color:rgba(196,125,14,.20);
}

.mc-calendar-day.mc-mixed{
  background:
    linear-gradient(135deg,#edf6ec 0%,#edf6ec 49%,#fff3d2 51%,#fff3d2 100%);
  border-color:rgba(145,123,55,.16);
}

.mc-calendar-day.mc-mixed .mc-calendar-number{
  background:transparent;
  box-shadow:none;
  border:0;
}

/* Petits badges comme dans la référence */
.mc-calendar-badges{
  position:absolute;
  left:9px;
  right:auto;
  bottom:8px;
  z-index:3;
  display:flex;
  align-items:center;
  gap:5px;
}

.mc-calendar-type-badge{
  width:20px;
  min-width:20px;
  height:20px;
  padding:0;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  border-radius:50%;
  color:white;
  font-size:0;
  font-weight:850;
  line-height:20px;
  box-shadow:none;
}

.mc-calendar-type-badge.mc-table{
  background:#2f843b;
}

.mc-calendar-type-badge.mc-event{
  background:#d39a00;
}

.mc-calendar-type-badge .mc-badge-icon{
  display:none;
}

.mc-calendar-type-badge .mc-badge-count{
  font-size:9px;
  line-height:1;
  font-weight:900;
}

/* Footer compact mais garde les mêmes chiffres/infos */
.mc-calendar-footer{
  margin-top:12px;
  padding:11px 14px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  border-top:1px solid rgba(31,107,45,.08);
  border-radius:14px;
  color:var(--mc-muted);
  background:rgba(255,255,255,.58);
  font-size:11px;
}

.mc-calendar-total{
  display:inline-flex;
  align-items:center;
  gap:6px;
  padding:7px 10px;
  border-radius:999px;
  background:#edf4eb;
  color:var(--mc-dark);
}

.mc-calendar-total strong{
  color:var(--mc-green);
  font-size:12px;
}

/* Tablette */
@media(max-width:991.98px){
  .mc-calendar-panel{
    padding:15px!important;
    border-radius:20px!important;
  }

  .mc-calendar-header{
    flex-direction:column!important;
    align-items:stretch!important;
    gap:12px!important;
  }

  .mc-calendar-controls{
    width:100%!important;
    grid-template-columns:46px 1fr 46px!important;
    margin-top:0!important;
  }

  .mc-calendar-weekdays,
  .mc-calendar-grid{
    gap:6px!important;
  }

  .mc-calendar-day{
    min-height:68px!important;
    height:68px!important;
    padding:7px!important;
    border-radius:11px!important;
  }

  .mc-calendar-number{
    top:7px!important;
    left:7px!important;
    font-size:11px!important;
    width:auto!important;
    height:auto!important;
    position:absolute!important;
  }

  .mc-calendar-badges{
    left:7px!important;
    right:auto!important;
    bottom:7px!important;
    gap:4px!important;
  }

  .mc-calendar-type-badge{
    width:19px!important;
    min-width:19px!important;
    height:19px!important;
    padding:0!important;
    font-size:0!important;
  }

  .mc-calendar-type-badge .mc-badge-count{
    font-size:8.5px!important;
  }

  .mc-calendar-footer{
    flex-direction:row!important;
    align-items:center!important;
    flex-wrap:wrap!important;
  }
}

/* Mobile */
@media(max-width:575.98px){
  .mc-calendar-panel{
    margin-top:18px!important;
    padding:10px 7px 12px!important;
    border-radius:17px!important;
    overflow:hidden!important;
  }

  .mc-calendar-header{
    margin-bottom:9px!important;
    gap:9px!important;
  }

  .mc-calendar-title{
    font-size:19px!important;
  }

  .mc-calendar-subtitle{
    margin-top:6px!important;
    font-size:10.5px!important;
  }

  .mc-calendar-legend{
    gap:5px!important;
    margin-top:8px!important;
  }

  .mc-calendar-legend-item{
    padding:5px 8px!important;
    gap:5px!important;
    font-size:9px!important;
  }

  .mc-calendar-controls{
    height:46px!important;
    grid-template-columns:36px 1fr 36px!important;
    padding:4px 5px!important;
    border-radius:13px!important;
  }

  .mc-calendar-nav{
    width:32px!important;
    height:32px!important;
    border-radius:9px!important;
    font-size:21px!important;
  }

  .mc-calendar-month{
    font-size:18px!important;
  }

  .mc-calendar-weekdays,
  .mc-calendar-grid{
    gap:4px!important;
  }

  .mc-calendar-weekdays{
    margin-bottom:4px!important;
  }

  .mc-calendar-weekday{
    padding:4px 0!important;
    font-size:7px!important;
    letter-spacing:.04em!important;
    white-space:nowrap!important;
  }

  .mc-calendar-day{
    min-height:50px!important;
    height:50px!important;
    padding:5px!important;
    border-radius:9px!important;
  }

  .mc-calendar-number{
    top:5px!important;
    left:5px!important;
    font-size:9px!important;
    width:auto!important;
    height:auto!important;
    line-height:1!important;
    position:absolute!important;
  }

  .mc-calendar-badges{
    left:5px!important;
    right:auto!important;
    bottom:5px!important;
    gap:3px!important;
    justify-content:flex-start!important;
  }

  .mc-calendar-type-badge{
    width:16px!important;
    min-width:16px!important;
    height:16px!important;
    padding:0!important;
    border-radius:50%!important;
    font-size:0!important;
    line-height:16px!important;
  }

  .mc-calendar-type-badge .mc-badge-count{
    font-size:7px!important;
  }

  .mc-calendar-footer{
    margin-top:9px!important;
    padding:8px!important;
    gap:6px!important;
    font-size:8.5px!important;
    flex-wrap:wrap!important;
    flex-direction:row!important;
    align-items:center!important;
  }

  .mc-calendar-total{
    padding:5px 7px!important;
    font-size:8.5px!important;
  }

  .mc-calendar-total strong{
    font-size:9px!important;
  }
}


/* =========================================================
   LÉGENDE DES COULEURS DU CALENDRIER
   Vert = réservations de tables
   Orange / Or = événements
========================================================= */
.mc-calendar-legend{
  margin-top:10px;
  display:flex;
  align-items:center;
  flex-wrap:wrap;
  gap:8px;
}

.mc-calendar-legend-item{
  min-height:30px;
  padding:6px 11px;
  display:inline-flex;
  align-items:center;
  gap:7px;
  border-radius:999px;
  font-size:10px;
  font-weight:850;
  white-space:nowrap;
}

.mc-calendar-legend-item.mc-table{
  color:#236d31;
  background:#eaf5e8;
  border:1px solid rgba(47,132,59,.14);
}

.mc-calendar-legend-item.mc-event{
  color:#956600;
  background:#fff1c8;
  border:1px solid rgba(211,154,0,.18);
}

.mc-calendar-legend-dot{
  width:9px;
  height:9px;
  display:block;
  flex:0 0 auto;
  border-radius:50%;
}

.mc-calendar-legend-item.mc-table .mc-calendar-legend-dot{
  background:#2f843b;
  box-shadow:0 0 0 3px rgba(47,132,59,.10);
}

.mc-calendar-legend-item.mc-event .mc-calendar-legend-dot{
  background:#d39a00;
  box-shadow:0 0 0 3px rgba(211,154,0,.11);
}

/* Modal des réservations d'une journée */

.mc-day-modal{
  position:fixed;
  inset:0;
  z-index:2200;
  display:none;
  align-items:center;
  justify-content:center;
  padding:24px;
  background:rgba(9,43,18,.54);
  backdrop-filter:blur(9px);
  -webkit-backdrop-filter:blur(9px);
  overflow:hidden;
}

.mc-day-modal.mc-open{
  display:flex;
  animation:mcFadeIn .2s ease both;
}

.mc-day-dialog{
  width:min(820px,100%);
  max-height:min(700px, calc(100vh - 48px));
  display:flex;
  flex-direction:column;
  overflow:hidden;
  border:1px solid rgba(31,107,45,.14);
  border-radius:28px;
  background:var(--mc-paper);
  box-shadow:0 38px 95px rgba(9,43,18,.35);
  animation:mcModalIn .28s cubic-bezier(.2,.8,.2,1) both;
}

.mc-day-dialog-header{
  flex:0 0 auto !important;
  padding:25px 27px;
  display:flex;
  align-items:flex-start;
  justify-content:space-between;
  gap:18px;
  background:linear-gradient(110deg,#fffdf8,rgba(245,233,202,.82));
  border-bottom:1px solid var(--mc-border);
}

.mc-day-dialog-eyebrow{
  color:var(--mc-gold);
  font-size:10px;
  font-weight:850;
  letter-spacing:.18em;
  text-transform:uppercase;
}

.mc-day-dialog-title{
  margin-top:8px;
  color:var(--mc-dark);
  font-family:Georgia,"Times New Roman",serif;
   font-size:22px;
  text-transform:capitalize;
}

.mc-day-close{
  width:42px;
  height:42px;
  display:grid;
  place-items:center;
  flex:0 0 auto;
  border:1px solid rgba(31,107,45,.14);
  border-radius:50%;
  background:white;
  color:var(--mc-dark);
  font-size:21px;
  cursor:pointer;
  transition:.2s ease;
}

.mc-day-close:hover{
  color:white;
  background:var(--mc-green);
  transform:rotate(8deg);
}

.mc-day-dialog-body{
  flex:1 1 auto !important;
  min-height:0 !important;
  overflow-y:scroll !important;
  overflow-x:hidden;
  overscroll-behavior:contain;
  padding:16px 20px 20px;
  scrollbar-width:thin;
  scrollbar-color:rgba(31,107,45,.48) transparent;
}
.mc-day-dialog-body::-webkit-scrollbar{
  width:8px;
}

.mc-day-dialog-body::-webkit-scrollbar-track{
  background:transparent;
}

.mc-day-dialog-body::-webkit-scrollbar-thumb{
  border-radius:999px;
  background:rgba(31,107,45,.42);
}

.mc-day-dialog-body::-webkit-scrollbar-thumb:hover{
  background:var(--mc-green);
}

.mc-day-empty{
  padding:48px 20px;
  color:var(--mc-muted);
  text-align:center;
}

.mc-reservation-list{
  display:grid;
  gap:13px;
}

.mc-reservation-card{
  padding:17px;
  display:grid;
  grid-template-columns:76px minmax(0,1fr) auto;
  align-items:center;
  gap:17px;
  border:1px solid rgba(31,107,45,.11);
  border-radius:18px;
  background:white;
  transition:.2s ease;
}

.mc-reservation-card:hover{
  border-color:rgba(196,125,14,.34);
  box-shadow:0 11px 25px rgba(18,63,29,.09);
  transform:translateX(4px);
}

.mc-reservation-time{
  color:var(--mc-green);
  font-family:Georgia,"Times New Roman",serif;
  font-size:23px;
  font-weight:700;
}

.mc-reservation-name{
  color:var(--mc-dark);
  font-size:14px;
  font-weight:800;
}

.mc-reservation-meta{
  margin-top:6px;
  display:flex;
  flex-wrap:wrap;
  gap:7px 13px;
  color:var(--mc-muted);
  font-size:11px;
}

.mc-reservation-status{
  padding:7px 11px;
  border-radius:999px;
  color:#805500;
  background:#fff1ca;
  font-size:10px;
  font-weight:850;
  white-space:nowrap;
}

.mc-reservation-details{
  margin-top:9px;
  display:inline-flex;
  color:var(--mc-green)!important;
  font-size:11px;
  font-weight:800;
  text-decoration:none!important;
}

@keyframes mcFadeIn{
  from{opacity:0}
  to{opacity:1}
}

@keyframes mcModalIn{
  from{opacity:0;transform:translateY(18px) scale(.97)}
  to{opacity:1;transform:translateY(0) scale(1)}
}

@media(max-width:760px){
  .mc-day-modal{padding:12px}
  .mc-day-dialog{max-height:calc(100vh - 24px);border-radius:22px}
  .mc-day-dialog-header{padding:19px 18px}
  .mc-day-dialog-title{font-size:22px}
  .mc-day-dialog-body{padding:15px 14px 19px}

  .mc-calendar-panel{padding:19px;border-radius:21px}
  .mc-calendar-header{flex-direction:column}
  .mc-calendar-controls{width:100%;justify-content:space-between}
  .mc-calendar-month{min-width:130px;font-size:17px}
  .mc-calendar-weekdays,.mc-calendar-grid{gap:5px}
  .mc-calendar-day{min-height:66px;padding:7px;border-radius:12px}
  .mc-calendar-number{width:24px;height:24px}
  .mc-calendar-count{right:5px;bottom:5px;min-width:24px;height:24px;padding:0 6px}
  .mc-calendar-dot{display:none}
  .mc-calendar-footer{align-items:flex-start;flex-direction:column}
  .mc-reservation-card{grid-template-columns:58px minmax(0,1fr)}
  .mc-reservation-status{grid-column:2;justify-self:start}
}

@keyframes mcPageIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
@keyframes mcCardIn{from{opacity:0;transform:translateY(20px) scale(.98)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes mcLogoFloat{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-5px) rotate(2deg)}}
@keyframes mcPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
@keyframes mcBreathe{0%,100%{transform:scale(1);opacity:.75}50%{transform:scale(1.12);opacity:1}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important}}
/* Les règles mobiles complètes (topbar, tiroir latéral, grilles, calendrier)
   sont regroupées plus bas dans le bloc "VERSION MOBILE" pour éviter les
   doublons/conflits avec les media queries ci-dessus. */

/* Recherche instantanée */
.card.mc-live-search-loading .table-responsive,
.card.mc-live-search-loading .card-footer {
  opacity: .46 !important;
  pointer-events: none !important;
  transition: opacity .18s ease !important;
}

.card.mc-live-search-loading {
  position: relative !important;
}

.card.mc-live-search-loading::after {
  content: "";
  position: absolute;
  right: 31px;
  top: 128px;
  width: 18px;
  height: 18px;
  z-index: 20;
  border: 2px solid rgba(31,107,45,.18);
  border-top-color: var(--mc-green);
  border-radius: 50%;
  animation: mcLiveSearchSpin .65s linear infinite;
}

@keyframes mcLiveSearchSpin {
  to { transform: rotate(360deg); }
}
/* Améliore la lisibilité des statuts */
.table tbody td span {
    font-family: Inter, Arial, sans-serif !important;
    letter-spacing: 0 !important;
    font-variant-ligatures: none !important;
}

/* Badges de statut */
.table tbody td span[style*="border-radius:999px"] {
    font-size: 12px !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    padding: 7px 12px !important;
    white-space: nowrap !important;
}

/* =========================================================
   VERSION MOBILE — menu hamburger + tiroir latéral + tactile
   (la version desktop ci-dessus n'est pas modifiée ; tout ce
   bloc ne s'active qu'en dessous des largeurs indiquées)
========================================================= */

/* Bouton hamburger : invisible sur desktop, affiché en media query */
.mc-nav-toggle{display:none;width:40px;height:40px;flex-shrink:0;align-items:center;justify-content:center;
  flex-direction:column;gap:4px;border:1px solid rgba(31,107,45,.18);border-radius:12px;background:white;cursor:pointer}
.mc-nav-toggle span{display:block;width:18px;height:2px;border-radius:2px;background:var(--mc-dark);transition:transform .22s ease,opacity .22s ease}
html.mc-nav-open .mc-nav-toggle span:nth-child(1){transform:translateY(6px) rotate(45deg)}
html.mc-nav-open .mc-nav-toggle span:nth-child(2){opacity:0}
html.mc-nav-open .mc-nav-toggle span:nth-child(3){transform:translateY(-6px) rotate(-45deg)}

/* Fond sombre derrière le menu ouvert */
.mc-nav-backdrop{display:none;position:fixed;inset:0;z-index:1039;background:rgba(9,43,18,.45);
  backdrop-filter:blur(2px);opacity:0;transition:opacity .25s ease}
html.mc-nav-open .mc-nav-backdrop{display:block;opacity:1}
html.mc-nav-open{overflow:hidden!important}

html.mc-nav-open,html.mc-nav-open body,html.mc-nav-open .page,html.mc-nav-open .page-wrapper{transform:none!important}

@media(max-width:991.98px){
  .mc-nav-toggle{display:inline-flex!important}
  .page-wrapper{margin-left:0!important}
  .mc-topbar{position:fixed!important;top:0!important;left:0!important;right:0!important;min-height:58px!important;height:auto!important;
    padding:9px 14px!important;z-index:2000!important;gap:8px!important;flex-wrap:nowrap!important}
  .mc-topbar-brand{display:none!important}
  .mc-topbar-actions{flex:1 1 auto!important;flex-wrap:nowrap!important;justify-content:flex-end!important;gap:8px!important;min-width:0!important}
  .mc-topbar-link{display:none!important}
  .mc-lang-switch{flex-shrink:0!important;padding:2px!important}
  .mc-lang-switch button{padding:6px 9px!important;font-size:10.5px!important}
  .mc-topbar-logout{flex-shrink:0!important;padding:0 12px!important;font-size:11.5px!important}
  .page-body{padding-top:74px!important}

  /* Le menu latéral devient un tiroir qui glisse par-dessus le contenu */
  .navbar-vertical{position:fixed!important;top:0!important;left:0!important;height:100vh!important;
    width:76vw!important;max-width:255px!important;transform:translateX(-100%)!important;
    transition:transform .28s cubic-bezier(.2,.8,.2,1)!important;z-index:1900!important;
    border-radius:0 0 26px 0!important;box-shadow:20px 0 54px rgba(9,43,18,.30)!important}
  html.mc-nav-open .navbar-vertical{transform:translateX(0)!important}
  .mc-nav-backdrop{z-index:1890!important}

  .mc-dashboard-bottom{grid-template-columns:1fr!important;gap:14px!important}
  .mc-dashboard-hero{min-height:auto!important;padding:24px 20px!important;border-radius:22px!important}
  .mc-dashboard h1{font-size:clamp(26px,8vw,38px)!important}
  .mc-hero-copy{font-size:13.5px!important}
  .mc-hero-actions{flex-direction:column!important;align-items:stretch!important}
  .mc-hero-actions .mc-hero-button{width:100%!important;justify-content:center!important}

  .card-header{flex-wrap:wrap!important;gap:10px!important;padding:16px 18px!important;min-height:auto!important}
  .card-header>*{width:100%!important}
  .card-title{font-size:21px!important}
  .card-body{padding:14px!important}
  .card-footer{flex-wrap:wrap!important;gap:10px!important}
  .card-footer .btn{flex:1 1 auto!important;min-width:130px!important}

  /* KPI et accès rapides : on garde toujours au moins 2 colonnes, jamais empilés en 1 */
  .mc-stats-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px!important}
  .mc-stat-card{min-height:auto!important;padding:14px!important;border-radius:17px!important}
  .mc-stat-icon{font-size:20px!important;margin-bottom:6px!important}
  .mc-stat-value{font-size:24px!important}
  .mc-stat-label{font-size:11px!important;line-height:1.3!important}
  .mc-quick-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px!important}
  .mc-quick-link{min-height:auto!important;padding:12px 10px!important;flex-direction:column!important;
    text-align:center!important;gap:6px!important;font-size:12px!important;line-height:1.25!important}
  .mc-quick-link span:first-child{font-size:20px!important}

  /* Calendrier : cellules plus lisibles, chiffre et badge bien séparés
     (tablette : on reste proche de la taille desktop, il y a la place) */
  .mc-calendar-panel{padding:16px!important;border-radius:19px!important}
  .mc-calendar-header{flex-direction:column!important;align-items:flex-start!important}
  .mc-calendar-legend{margin-top:8px!important}
  .mc-calendar-controls{width:100%!important;justify-content:space-between!important;margin-top:10px!important}
  .mc-calendar-weekdays,.mc-calendar-grid{gap:7px!important}
  .mc-calendar-weekday{font-size:10px!important;padding:6px 2px!important}
  .mc-calendar-day{min-height:88px!important;padding:10px!important;border-radius:15px!important}
  .mc-calendar-number{width:27px!important;height:27px!important;font-size:12.5px!important;z-index:3!important;position:relative!important}
  .mc-calendar-badges{right:7px!important;bottom:7px!important;gap:5px!important}
  .mc-calendar-type-badge{min-width:26px!important;height:25px!important;padding:0 7px!important;font-size:10px!important;gap:3px!important}
  .mc-calendar-count{right:7px!important;bottom:7px!important;min-width:25px!important;height:25px!important}
  .mc-calendar-footer{align-items:flex-start!important;flex-direction:column!important;gap:8px!important}

  /* Tableaux : on garde le scroll horizontal natif (fiable avec les filtres/actions
     SQLAdmin) mais on l'indique visuellement et on agrandit les zones tactiles */
  .table-responsive{-webkit-overflow-scrolling:touch!important;position:relative!important}
  .table-responsive::after{content:"";position:absolute;top:0;right:0;bottom:0;width:20px;pointer-events:none;
    background:linear-gradient(90deg,transparent,rgba(18,63,29,.08))}
  .table thead th,.table tbody td{padding:12px 10px!important;font-size:12.5px!important}
  .table a{min-height:38px!important;display:inline-flex!important;align-items:center!important}

  .modal-dialog{margin:10px!important;max-width:calc(100vw - 20px)!important}
  .order-ticket-modal{width:94vw!important;height:88vh!important}

  /* Empêche le zoom automatique iOS sur les champs de formulaire */
  .form-control,.form-select,.ts-control{font-size:16px!important}
}

@media(max-width:575.98px){
  .mc-dashboard{padding:2px 4px 40px!important}
  .card-header{padding:14px!important}
  .card-body{padding:12px!important}
  .mc-dashboard h1{font-size:25px!important}
  .mc-stat-value{font-size:21px!important}
  .mc-quick-link{font-size:11.5px!important}

  /* =========================================================
     CALENDRIER MOBILE COMPACT ET RESPONSIVE
     - 7 colonnes toujours visibles
     - cellules plus petites
     - badges réduits au nombre uniquement
  ========================================================= */
  .mc-calendar-panel{
    margin-top:18px!important;
    padding:14px 10px 16px!important;
    border-radius:18px!important;
    overflow:hidden!important;
  }

  .mc-calendar-header{
    margin-bottom:14px!important;
    gap:10px!important;
  }

  .mc-calendar-title{
    font-size:21px!important;
  }

  .mc-calendar-subtitle{
    margin-top:7px!important;
    font-size:11.5px!important;
    line-height:1.45!important;
  }

  .mc-calendar-legend{
    gap:6px!important;
    margin-top:10px!important;
  }

  .mc-calendar-legend-item{
    padding:6px 9px!important;
    gap:5px!important;
    font-size:10px!important;
  }

  .mc-calendar-legend-dot{
    width:7px!important;
    height:7px!important;
  }

  .mc-calendar-controls{
    width:100%!important;
    height:48px!important;
    margin-top:5px!important;
    padding:4px!important;
    border-radius:14px!important;
  }

  .mc-calendar-nav{
    width:40px!important;
    height:40px!important;
    border-radius:11px!important;
    font-size:23px!important;
    flex-shrink:0!important;
  }

  .mc-calendar-month{
    min-width:0!important;
    flex:1!important;
    font-size:17px!important;
    font-weight:600!important;
  }

  .mc-calendar-weekdays,
  .mc-calendar-grid{
    width:100%!important;
    display:grid!important;
    grid-template-columns:repeat(7,minmax(0,1fr))!important;
    gap:4px!important;
  }

  .mc-calendar-weekdays{
    margin-bottom:5px!important;
  }

  .mc-calendar-weekday{
    padding:5px 0!important;
    font-size:8px!important;
    letter-spacing:.04em!important;
    white-space:nowrap!important;
  }

  .mc-calendar-grid{
    min-height:0!important;
  }

  .mc-calendar-day{
    position:relative!important;
    min-width:0!important;
    width:100%!important;
    min-height:52px!important;
    height:52px!important;
    padding:5px!important;
    border-radius:10px!important;
    overflow:hidden!important;
  }

  .mc-calendar-day:hover:not(.mc-empty){
    transform:none!important;
  }

  .mc-calendar-number{
    position:relative!important;
    z-index:3!important;
    width:20px!important;
    height:20px!important;
    padding:0!important;
    font-size:10px!important;
    line-height:20px!important;
    border-radius:7px!important;
  }

  .mc-calendar-badges{
    position:absolute!important;
    z-index:4!important;
    left:4px!important;
    right:4px!important;
    bottom:4px!important;
    display:flex!important;
    justify-content:flex-end!important;
    align-items:center!important;
    gap:2px!important;
  }

  .mc-calendar-type-badge{
    min-width:17px!important;
    width:auto!important;
    height:17px!important;
    padding:0 4px!important;
    gap:0!important;
    border-radius:999px!important;
    font-size:0!important;
    line-height:17px!important;
    box-shadow:none!important;
  }

  .mc-calendar-type-badge .mc-badge-count{
    font-size:8px!important;
    line-height:1!important;
    font-weight:900!important;
  }

  .mc-calendar-type-badge .mc-badge-icon{
    display:none!important;
  }

  .mc-calendar-count{
    right:4px!important;
    bottom:4px!important;
    min-width:17px!important;
    height:17px!important;
    padding:0 4px!important;
    font-size:8px!important;
  }

  .mc-calendar-dot{
    display:none!important;
  }

  .mc-calendar-day.mc-today{
    box-shadow:inset 0 0 0 1px rgba(196,125,14,.25)!important;
  }

  .mc-calendar-day.mc-mixed .mc-calendar-number{
    background:rgba(255,255,255,.94)!important;
    box-shadow:none!important;
  }

  .mc-calendar-footer{
    margin-top:12px!important;
    padding-top:11px!important;
    gap:7px!important;
    font-size:10px!important;
  }

  .mc-calendar-total{
    padding:7px 9px!important;
    font-size:9.5px!important;
  }

  .mc-calendar-total strong{
    font-size:10px!important;
  }

  /* Modal de réservations optimisé téléphone */
  .mc-day-modal{
    padding:8px!important;
  }

  .mc-day-dialog{
    width:100%!important;
    max-height:calc(100vh - 16px)!important;
    border-radius:18px!important;
  }

  .mc-day-dialog-header{
    padding:16px!important;
  }

  .mc-day-dialog-title{
    font-size:19px!important;
  }

  .mc-day-close{
    width:38px!important;
    height:38px!important;
  }

  .mc-day-dialog-body{
    padding:12px!important;
  }

  .mc-reservation-card{
    grid-template-columns:1fr!important;
    gap:8px!important;
    padding:13px!important;
    border-radius:14px!important;
  }

  .mc-reservation-time{
    font-size:19px!important;
  }

  .mc-reservation-status{
    grid-column:auto!important;
    justify-self:start!important;
  }

  .mc-day-summary{
    gap:6px!important;
  }

  .mc-day-summary-badge{
    padding:7px 9px!important;
    font-size:10px!important;
  }
}

@media(max-width:359.98px){
  /* Écrans très étroits uniquement : on passe l'intitulé "Déconnexion" en icône seule */
  .mc-logout-text{display:none!important}
  .mc-topbar-logout{padding:0 11px!important}
}


/* =========================================================
   SIDEBAR MOBILE — même design que la référence
========================================================= */
@media(max-width:991.98px){
  .navbar-vertical .navbar-brand{
    min-height:148px!important;
    padding:18px 14px 13px!important;
    font-size:17px!important;
  }

  .navbar-vertical .navbar-brand::before{
    width:64px!important;
    height:64px!important;
    margin-bottom:11px!important;
    border-radius:18px!important;
  }

  .navbar-vertical .navbar-brand::after{
    margin-top:7px!important;
    font-size:7.5px!important;
  }

  .navbar-vertical .navbar-collapse{
    padding:6px 11px 78px!important;
  }

  .navbar-vertical .navbar-nav{
    gap:5px!important;
  }

  .navbar-vertical .nav-link{
    min-height:42px!important;
    padding:9px 10px!important;
    border-radius:12px!important;
    gap:10px!important;
    font-size:11.5px!important;
  }

  .navbar-vertical .nav-link-icon,
  .navbar-vertical .nav-link i,
  .navbar-vertical .nav-link svg{
    width:20px!important;
    height:20px!important;
    min-width:20px!important;
  }

  .navbar-vertical::after{
    left:11px!important;
    right:11px!important;
    bottom:12px!important;
    height:46px!important;
    padding:0 12px!important;
    border-radius:13px!important;
    font-size:9.5px!important;
  }

  .navbar-vertical .container-fluid::after{
    bottom:58px!important;
    opacity:.20!important;
  }
}


/* =========================================================
   MOBILE SIDEBAR — collapsed icon rail + expanded full menu
   Closed: a slim green rail stays visible.
   Open: the full sidebar expands.
========================================================= */
@media(max-width:991.98px){

  /* Sidebar starts BELOW the fixed topbar so the logo is no longer cut */
  .navbar-vertical{
    top:74px!important;
    bottom:0!important;
    left:0!important;
    height:calc(100vh - 74px)!important;

    width:66px!important;
    max-width:none!important;

    transform:none!important;
    transition:width .26s cubic-bezier(.2,.8,.2,1)!important;

    border-radius:0 0 22px 0!important;
    overflow:hidden!important;
    z-index:1900!important;
  }

  html.mc-nav-open .navbar-vertical{
    width:235px!important;
    transform:none!important;
  }

  /* Keep the page visible beside the small rail */
  .page-wrapper{
    margin-left:66px!important;
    transition:margin-left .26s cubic-bezier(.2,.8,.2,1)!important;
  }

  html.mc-nav-open .page-wrapper{
    margin-left:66px!important;
  }

  /* backdrop only when menu is really expanded */
  .mc-nav-backdrop{
    left:66px!important;
  }

  /* -------- CLOSED STATE -------- */

  .mc-sidebar-head{
    min-height:78px!important;
    padding:10px 8px!important;
  }

  .mc-sidebar-logo{
    width:44px!important;
    height:44px!important;
    margin:0 auto!important;
    border-radius:14px!important;
  }

  .mc-sidebar-name,
  .mc-sidebar-role{
    display:none!important;
  }

  .mc-sidebar-menu{
    padding:7px 7px 72px!important;
    gap:5px!important;
    align-items:stretch!important;
  }

  .mc-sidebar-link{
    min-height:44px!important;
    width:100%!important;
    padding:0!important;
    justify-content:center!important;
    gap:0!important;
    border-radius:12px!important;
  }

  .mc-sidebar-link > span:not(.mc-sidebar-icon){
    display:none!important;
  }

  .mc-sidebar-icon{
    width:24px!important;
    min-width:24px!important;
    height:24px!important;
    font-size:18px!important;
  }

  .mc-sidebar-leaves{
    display:none!important;
  }

  .mc-sidebar-account{
    left:8px!important;
    right:8px!important;
    bottom:10px!important;
    height:44px!important;
    padding:0!important;
    justify-content:center!important;
    border-radius:13px!important;
  }

  .mc-sidebar-avatar{
    width:29px!important;
    height:29px!important;
    flex:0 0 auto!important;
  }

  .mc-sidebar-account-name,
  .mc-sidebar-chevron{
    display:none!important;
  }

  /* -------- OPEN STATE -------- */

  html.mc-nav-open .mc-sidebar-head{
    min-height:148px!important;
    padding:18px 15px 13px!important;
  }

  html.mc-nav-open .mc-sidebar-logo{
    width:64px!important;
    height:64px!important;
    border-radius:18px!important;
  }

  html.mc-nav-open .mc-sidebar-name{
    display:block!important;
    margin-top:10px!important;
    font-size:16px!important;
  }

  html.mc-nav-open .mc-sidebar-role{
    display:block!important;
    margin-top:7px!important;
    font-size:7px!important;
  }

  html.mc-nav-open .mc-sidebar-menu{
    padding:7px 11px 82px!important;
    gap:5px!important;
  }

  html.mc-nav-open .mc-sidebar-link{
    min-height:42px!important;
    padding:9px 10px!important;
    justify-content:flex-start!important;
    gap:10px!important;
    font-size:11px!important;
  }

  html.mc-nav-open .mc-sidebar-link > span:not(.mc-sidebar-icon){
    display:inline!important;
  }

  html.mc-nav-open .mc-sidebar-leaves{
    display:block!important;
  }

  html.mc-nav-open .mc-sidebar-account{
    left:11px!important;
    right:11px!important;
    bottom:12px!important;
    height:46px!important;
    padding:0 12px!important;
    justify-content:flex-start!important;
  }

  html.mc-nav-open .mc-sidebar-account-name,
  html.mc-nav-open .mc-sidebar-chevron{
    display:inline!important;
  }

  html.mc-nav-open .mc-sidebar-account-name{
    flex:1!important;
  }

  /* The topbar hamburger remains the controller */
  .mc-nav-toggle{
    display:inline-flex!important;
  }
}

/* Very narrow screens: slightly slimmer rail */
@media(max-width:420px){
  .navbar-vertical{
    width:58px!important;
  }

  .page-wrapper{
    margin-left:58px!important;
  }

  .mc-nav-backdrop{
    left:58px!important;
  }

  html.mc-nav-open .navbar-vertical{
    width:min(82vw,235px)!important;
  }

  .mc-sidebar-menu{
    padding-left:5px!important;
    padding-right:5px!important;
  }

  .mc-sidebar-logo{
    width:40px!important;
    height:40px!important;
  }
}


/* =========================================================
   FINAL SIDEBAR POLISH
   Clean mobile rail + elegant expanded drawer.
   Overrides previous sidebar mobile rules only.
========================================================= */
@media(max-width:991.98px){

  /* ---------- GLOBAL DRAWER ---------- */
  .navbar-vertical{
    top:74px!important;
    bottom:0!important;
    left:0!important;
    height:calc(100vh - 74px)!important;

    width:64px!important;
    max-width:none!important;

    transform:none!important;
    transition:width .26s cubic-bezier(.2,.8,.2,1)!important;

    overflow:hidden!important;
    border-radius:0 0 24px 0!important;
    box-shadow:10px 0 30px rgba(9,43,18,.16)!important;
    background:linear-gradient(180deg,#124f2d 0%,#0d4326 58%,#08371f 100%)!important;
  }

  html.mc-nav-open .navbar-vertical{
    width:248px!important;
    transform:none!important;
    box-shadow:22px 0 54px rgba(9,43,18,.28)!important;
  }

  .page-wrapper{
    margin-left:64px!important;
    transition:margin-left .26s cubic-bezier(.2,.8,.2,1)!important;
  }

  html.mc-nav-open .page-wrapper{
    margin-left:64px!important;
  }

  .mc-nav-backdrop{
    left:64px!important;
    background:rgba(9,43,18,.38)!important;
    backdrop-filter:blur(2px)!important;
  }

  /* ---------- CLOSED RAIL ---------- */
  .mc-sidebar-custom{
    position:relative!important;
    height:100%!important;
    display:flex!important;
    flex-direction:column!important;
    overflow:hidden!important;
    background:transparent!important;
  }

  .mc-sidebar-head{
    min-height:88px!important;
    padding:14px 8px 10px!important;
    display:flex!important;
    align-items:center!important;
    justify-content:flex-start!important;
  }

  .mc-sidebar-logo{
    width:44px!important;
    height:44px!important;
    margin:0 auto!important;
    border-radius:14px!important;
    object-fit:cover!important;
    box-shadow:0 7px 16px rgba(0,0,0,.18)!important;
  }

  .mc-sidebar-name,
  .mc-sidebar-role{
    display:none!important;
  }

  .mc-sidebar-menu{
    flex:1 1 auto!important;
    min-height:0!important;
    padding:8px 7px 74px!important;
    gap:6px!important;
    overflow-y:auto!important;
  }

  .mc-sidebar-link{
    min-height:46px!important;
    width:100%!important;
    padding:0!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    gap:0!important;
    border-radius:13px!important;
    color:rgba(255,255,255,.92)!important;
    background:transparent!important;
  }

  .mc-sidebar-link:hover{
    background:rgba(255,255,255,.08)!important;
  }

  .mc-sidebar-link.mc-active{
    background:linear-gradient(135deg,rgba(112,183,108,.42),rgba(255,255,255,.10))!important;
    box-shadow:inset 0 0 0 1px rgba(255,255,255,.06)!important;
  }

  .mc-sidebar-link > span:not(.mc-sidebar-icon){
    display:none!important;
  }

  .mc-sidebar-icon{
    width:24px!important;
    min-width:24px!important;
    height:24px!important;
    display:grid!important;
    place-items:center!important;
    font-size:18px!important;
    line-height:1!important;
  }

  /* Remove the ugly fake decorative blobs in mobile */
  .mc-sidebar-leaves,
  .navbar-vertical .container-fluid::after{
    display:none!important;
  }

  /* Compact profile chip in rail */
  .mc-sidebar-account{
    left:9px!important;
    right:9px!important;
    bottom:11px!important;
    height:44px!important;
    padding:0!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    gap:0!important;
    overflow:hidden!important;
    border:1px solid rgba(255,255,255,.13)!important;
    border-radius:14px!important;
    background:rgba(255,255,255,.045)!important;
    box-shadow:none!important;
  }

  .mc-sidebar-avatar{
    width:30px!important;
    height:30px!important;
    min-width:30px!important;
    display:grid!important;
    place-items:center!important;
    border-radius:50%!important;
    background:rgba(111,179,108,.58)!important;
    color:white!important;
    font-size:9px!important;
    font-weight:900!important;
  }

  .mc-sidebar-account-name,
  .mc-sidebar-chevron{
    display:none!important;
  }

  /* Remove pseudo-account from previous CSS to avoid duplicated text */
  .navbar-vertical::after{
    display:none!important;
    content:none!important;
  }

  /* ---------- OPEN DRAWER ---------- */
  html.mc-nav-open .mc-sidebar-head{
    min-height:156px!important;
    padding:20px 16px 15px!important;
  }

  html.mc-nav-open .mc-sidebar-logo{
    width:68px!important;
    height:68px!important;
    margin:0 auto!important;
    border-radius:19px!important;
  }

  html.mc-nav-open .mc-sidebar-name{
    display:block!important;
    margin-top:12px!important;
    color:#fffdf8!important;
    font-family:Georgia,"Times New Roman",serif!important;
    font-size:18px!important;
    font-weight:700!important;
    line-height:1.1!important;
    text-align:center!important;
    white-space:nowrap!important;
  }

  html.mc-nav-open .mc-sidebar-role{
    display:block!important;
    margin-top:8px!important;
    color:#e6bd46!important;
    font-size:7.5px!important;
    font-weight:900!important;
    letter-spacing:.22em!important;
    text-align:center!important;
    white-space:nowrap!important;
  }

  html.mc-nav-open .mc-sidebar-menu{
    padding:8px 13px 78px!important;
    gap:5px!important;
  }

  html.mc-nav-open .mc-sidebar-link{
    min-height:44px!important;
    padding:10px 12px!important;
    justify-content:flex-start!important;
    gap:12px!important;
    border-radius:13px!important;
    font-size:11.5px!important;
    font-weight:750!important;
  }

  html.mc-nav-open .mc-sidebar-link > span:not(.mc-sidebar-icon){
    display:inline!important;
    min-width:0!important;
    overflow:hidden!important;
    text-overflow:ellipsis!important;
    white-space:nowrap!important;
  }

  html.mc-nav-open .mc-sidebar-icon{
    width:22px!important;
    min-width:22px!important;
    height:22px!important;
    font-size:17px!important;
  }

  html.mc-nav-open .mc-sidebar-account{
    left:13px!important;
    right:13px!important;
    bottom:13px!important;
    height:48px!important;
    padding:0 12px!important;
    justify-content:flex-start!important;
    gap:9px!important;
  }

  html.mc-nav-open .mc-sidebar-avatar{
    width:30px!important;
    height:30px!important;
    min-width:30px!important;
  }

  html.mc-nav-open .mc-sidebar-account-name{
    display:block!important;
    flex:1 1 auto!important;
    min-width:0!important;
    overflow:hidden!important;
    text-overflow:ellipsis!important;
    white-space:nowrap!important;
    color:white!important;
    font-size:10px!important;
    font-weight:800!important;
  }

  html.mc-nav-open .mc-sidebar-chevron{
    display:block!important;
    flex:0 0 auto!important;
    color:rgba(255,255,255,.9)!important;
    font-size:13px!important;
  }
}

/* Smaller phones */
@media(max-width:420px){
  .navbar-vertical{
    width:56px!important;
  }

  .page-wrapper{
    margin-left:56px!important;
  }

  .mc-nav-backdrop{
    left:56px!important;
  }

  html.mc-nav-open .navbar-vertical{
    width:min(82vw,242px)!important;
  }

  .mc-sidebar-head{
    min-height:82px!important;
    padding-left:6px!important;
    padding-right:6px!important;
  }

  .mc-sidebar-logo{
    width:40px!important;
    height:40px!important;
  }

  .mc-sidebar-menu{
    padding-left:5px!important;
    padding-right:5px!important;
  }

  .mc-sidebar-account{
    left:7px!important;
    right:7px!important;
  }
}


/* =========================================================
   FIX GAP BETWEEN TOPBAR AND MOBILE SIDEBAR
   Sidebar sits flush directly under the topbar.
========================================================= */
@media(max-width:991.98px){

  :root{
    --mc-mobile-topbar-h:58px;
  }

  .mc-topbar{
    min-height:var(--mc-mobile-topbar-h)!important;
    height:var(--mc-mobile-topbar-h)!important;
    padding-top:0!important;
    padding-bottom:0!important;
  }

  .navbar-vertical{
    top:var(--mc-mobile-topbar-h)!important;
    height:calc(100vh - var(--mc-mobile-topbar-h))!important;
    bottom:auto!important;
    margin-top:0!important;
  }

  .page-body{
    padding-top:var(--mc-mobile-topbar-h)!important;
  }

  .mc-nav-backdrop{
    top:var(--mc-mobile-topbar-h)!important;
    bottom:0!important;
    height:calc(100vh - var(--mc-mobile-topbar-h))!important;
  }

  .mc-sidebar-custom,
  .mc-sidebar-head{
    margin-top:0!important;
  }
}


/* =========================================================
   TABLES SQLADMIN -> CARTES SUR MOBILE UNIQUEMENT
   Desktop/tablette restent inchangés.
========================================================= */

.mc-mobile-cards{
  display:none;
}

@media(max-width:575.98px){

  /* On cache seulement le tableau natif sur téléphone */
  .card.mc-mobile-card-mode .table-responsive{
    display:none!important;
  }

  .card.mc-mobile-card-mode .mc-mobile-cards{
    display:grid!important;
    gap:10px!important;
    padding:12px!important;
    background:transparent!important;
  }

  .mc-mobile-record-card{
    overflow:hidden;
    border:1px solid rgba(31,107,45,.12);
    border-radius:16px;
    background:rgba(255,253,248,.98);
    box-shadow:0 8px 22px rgba(18,63,29,.07);
    transition:border-color .18s ease, box-shadow .18s ease;
  }

  .mc-mobile-record-card.mc-open{
    border-color:rgba(196,125,14,.28);
    box-shadow:0 12px 26px rgba(18,63,29,.10);
  }

  .mc-mobile-card-summary{
    width:100%;
    min-height:76px;
    padding:13px 14px;
    display:flex;
    align-items:center;
    gap:12px;
    border:0;
    background:transparent;
    color:var(--mc-text);
    text-align:left;
    cursor:pointer;
  }

  .mc-mobile-card-main{
    min-width:0;
    flex:1 1 auto;
  }

  .mc-mobile-card-title{
    overflow:hidden;
    color:var(--mc-dark);
    font-size:14px;
    font-weight:850;
    line-height:1.25;
    text-overflow:ellipsis;
    white-space:nowrap;
  }

  .mc-mobile-card-subtitle{
    margin-top:4px;
    overflow:hidden;
    color:var(--mc-muted);
    font-size:11px;
    line-height:1.3;
    text-overflow:ellipsis;
    white-space:nowrap;
  }

  .mc-mobile-card-chevron{
    width:28px;
    height:28px;
    flex:0 0 auto;
    display:grid;
    place-items:center;
    border-radius:50%;
    color:var(--mc-dark);
    background:#edf4eb;
    font-size:17px;
    font-weight:800;
    transition:transform .18s ease, background .18s ease;
  }

  .mc-mobile-record-card.mc-open .mc-mobile-card-chevron{
    background:#fff0c7;
  }

  .mc-mobile-card-details{
    display:none;
    padding:0 14px 14px;
    border-top:1px solid rgba(31,107,45,.08);
  }

  .mc-mobile-record-card.mc-open .mc-mobile-card-details{
    display:block;
  }

  .mc-mobile-card-grid{
    padding-top:10px;
    display:grid;
    gap:0;
  }

  .mc-mobile-detail-row{
    padding:9px 0;
    display:grid;
    grid-template-columns:112px minmax(0,1fr);
    gap:10px;
    align-items:start;
    border-bottom:1px solid rgba(31,107,45,.07);
  }

  .mc-mobile-detail-row:last-child{
    border-bottom:0;
  }

  .mc-mobile-detail-label{
    color:#728077;
    font-size:9px;
    font-weight:850;
    letter-spacing:.07em;
    text-transform:uppercase;
  }

  .mc-mobile-detail-value{
    min-width:0;
    overflow-wrap:anywhere;
    color:var(--mc-text);
    font-size:12px;
    line-height:1.4;
  }

  .mc-mobile-detail-value a{
    min-height:auto!important;
    display:inline!important;
  }

  /* Actions du tableau conservées dans une zone dédiée */
  .mc-mobile-card-actions{
    margin-top:10px;
    padding-top:10px;
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:8px;
    border-top:1px solid rgba(31,107,45,.09);
  }

  .mc-mobile-card-actions a,
  .mc-mobile-card-actions button{
    min-width:36px;
    min-height:36px!important;
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    border-radius:10px!important;
  }

  /* Toolbar plus compacte au-dessus des cartes */
  .card.mc-mobile-card-mode .card-body{
    padding:10px!important;
  }

  .card.mc-mobile-card-mode .card-body form{
    gap:8px!important;
  }
}


/* =========================================================
   MOBILE CARDS — FINAL ELEGANT VERSION
   Selection is synced with the hidden SQLAdmin checkboxes so
   the existing "Actions" bulk menu keeps working.
========================================================= */
@media(max-width:575.98px){

  .card.mc-mobile-card-mode .mc-mobile-cards{
    gap:12px!important;
    padding:14px 12px 18px!important;
  }

  .mc-mobile-selectbar{
    min-height:46px;
    padding:9px 12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    border:1px solid rgba(31,107,45,.10);
    border-radius:14px;
    background:rgba(255,253,248,.86);
    box-shadow:0 6px 16px rgba(18,63,29,.04);
  }

  .mc-mobile-selectbar-left{
    display:flex;
    align-items:center;
    gap:9px;
    color:var(--mc-dark);
    font-size:11px;
    font-weight:800;
  }

  .mc-mobile-selected-count{
    padding:5px 8px;
    border-radius:999px;
    background:#edf4eb;
    color:var(--mc-green);
    font-size:9px;
    font-weight:900;
    white-space:nowrap;
  }

  .mc-mobile-select,
  .mc-mobile-select-all{
    width:18px!important;
    height:18px!important;
    min-height:18px!important;
    margin:0!important;
    accent-color:var(--mc-green);
    cursor:pointer;
  }

  .mc-mobile-record-card{
    position:relative;
    overflow:hidden;
    border:1px solid rgba(31,107,45,.11)!important;
    border-radius:19px!important;
    background:
      linear-gradient(145deg,rgba(255,255,255,.97),rgba(255,252,245,.96))!important;
    box-shadow:0 9px 24px rgba(18,63,29,.065)!important;
  }

  .mc-mobile-record-card::before{
    content:"";
    position:absolute;
    left:0;
    top:0;
    bottom:0;
    width:3px;
    opacity:0;
    background:linear-gradient(180deg,var(--mc-green),var(--mc-gold));
    transition:opacity .18s ease;
  }

  .mc-mobile-record-card.mc-open::before,
  .mc-mobile-record-card.mc-selected::before{
    opacity:1;
  }

  .mc-mobile-record-card.mc-selected{
    border-color:rgba(31,107,45,.28)!important;
    box-shadow:0 12px 28px rgba(18,63,29,.11)!important;
  }

  .mc-mobile-card-summary{
    min-height:82px!important;
    padding:14px 14px 14px 13px!important;
    gap:11px!important;
  }

  .mc-mobile-card-select-wrap{
    width:26px;
    min-width:26px;
    height:26px;
    display:grid;
    place-items:center;
    border-radius:9px;
    background:#f5f7f2;
  }

  .mc-mobile-card-title{
    color:#174623!important;
    font-size:14px!important;
    font-weight:850!important;
  }

  .mc-mobile-card-title > *{
    max-width:100%;
  }

  .mc-mobile-card-subtitle{
    margin-top:5px!important;
    color:#7b8490!important;
    font-size:11px!important;
    font-weight:650!important;
  }

  .mc-mobile-card-chevron{
    width:31px!important;
    height:31px!important;
    border:1px solid rgba(31,107,45,.08);
    background:#eef5ec!important;
    color:#174623!important;
    font-family:Arial,sans-serif!important;
    font-size:16px!important;
  }

  .mc-mobile-record-card.mc-open .mc-mobile-card-chevron{
    color:#805500!important;
    background:#fff0c7!important;
    border-color:rgba(196,125,14,.12)!important;
  }

  .mc-mobile-card-details{
    padding:0 15px 15px!important;
    background:linear-gradient(180deg,rgba(247,240,228,.18),rgba(255,255,255,0));
  }

  .mc-mobile-card-grid{
    padding-top:5px!important;
  }

  .mc-mobile-detail-row{
    padding:11px 0!important;
    grid-template-columns:102px minmax(0,1fr)!important;
    gap:13px!important;
    border-bottom:1px solid rgba(31,107,45,.075)!important;
  }

  .mc-mobile-detail-label{
    padding-top:2px;
    color:#78847b!important;
    font-size:8.5px!important;
    font-weight:900!important;
    letter-spacing:.09em!important;
  }

  .mc-mobile-detail-value{
    color:#253228!important;
    font-size:12px!important;
    line-height:1.45!important;
    font-weight:500!important;
  }

  /* Action icons inside expanded card */
  .mc-mobile-card-actions{
    margin-top:5px!important;
    padding-top:13px!important;
    gap:9px!important;
  }

  .mc-mobile-card-actions a,
  .mc-mobile-card-actions button{
    width:38px!important;
    min-width:38px!important;
    height:38px!important;
    min-height:38px!important;
    padding:0!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:11px!important;
    background:white!important;
    box-shadow:0 5px 12px rgba(18,63,29,.055)!important;
    text-decoration:none!important;
  }

  .mc-mobile-card-actions a:hover,
  .mc-mobile-card-actions button:hover{
    transform:none!important;
    background:#f8fbf7!important;
  }

  /* View stays green */
  .mc-mobile-card-actions a[href*="/view"]{
    color:var(--mc-green)!important;
  }

  /* Edit is warm gold/green */
  .mc-mobile-card-actions a[href*="/edit"]{
    color:#a96f00!important;
  }

  /* DELETE / TRASH — RED */
  .mc-mobile-card-actions a[href*="/delete"],
  .mc-mobile-card-actions a[data-bs-target*="delete"],
  .mc-mobile-card-actions button[data-bs-target*="delete"],
  .mc-mobile-card-actions .text-danger{
    color:#c63f35!important;
    border-color:rgba(198,63,53,.16)!important;
    background:#fff8f7!important;
  }

  .mc-mobile-card-actions a[href*="/delete"] svg,
  .mc-mobile-card-actions a[data-bs-target*="delete"] svg,
  .mc-mobile-card-actions button[data-bs-target*="delete"] svg{
    color:#c63f35!important;
    stroke:#c63f35!important;
  }

  /* Keep top Actions menu accessible and visually separate */
  .card.mc-mobile-card-mode .card-body{
    border-bottom:1px solid rgba(31,107,45,.08);
  }
}


/* =========================================================
   MOBILE UX V2 — cartes + recherche plus premium
   Uniquement téléphone. Desktop/tablette restent inchangés.
========================================================= */
@media(max-width:575.98px){

  /* ---------- CARD SHELL ---------- */
  .card.mc-mobile-card-mode{
    border-radius:22px!important;
    overflow:hidden!important;
    background:
      linear-gradient(180deg,rgba(255,253,248,.98),rgba(250,247,238,.98))!important;
  }

  .card.mc-mobile-card-mode .card-header{
    padding:16px 16px 13px!important;
    gap:8px!important;
    background:
      radial-gradient(circle at 95% 0,rgba(228,184,63,.17),transparent 120px),
      linear-gradient(120deg,#fffdf8,#fbf4e5)!important;
  }

  .card.mc-mobile-card-mode .card-title{
    font-size:23px!important;
    line-height:1.1!important;
  }

  .card.mc-mobile-card-mode .card-title::after{
    width:38px!important;
    margin-top:8px!important;
  }

  /* ---------- TOOLBAR / SEARCH EXPERIENCE ---------- */
  .card.mc-mobile-card-mode .card-body{
    padding:12px!important;
    background:rgba(255,253,248,.92)!important;
  }

  .card.mc-mobile-card-mode .card-body form{
    display:grid!important;
    grid-template-columns:1fr auto!important;
    gap:8px!important;
    align-items:center!important;
  }

  /* Search input becomes the main object */
  .card.mc-mobile-card-mode input[name="search"]{
    grid-column:1 / -1!important;
    width:100%!important;
    min-height:50px!important;
    padding:0 44px 0 43px!important;
    border:1px solid rgba(31,107,45,.15)!important;
    border-radius:16px!important;
    background:
      linear-gradient(180deg,#fff,#fffdf8)!important;
    box-shadow:
      0 7px 18px rgba(18,63,29,.055),
      inset 0 0 0 1px rgba(255,255,255,.7)!important;
    color:#1e3825!important;
    font-size:15px!important;
  }

  .card.mc-mobile-card-mode input[name="search"]:focus{
    border-color:rgba(31,107,45,.42)!important;
    box-shadow:
      0 0 0 4px rgba(31,107,45,.085),
      0 9px 20px rgba(18,63,29,.07)!important;
  }

  /* Search form pseudo icon */
  .card.mc-mobile-card-mode .card-body form{
    position:relative!important;
  }

  .card.mc-mobile-card-mode .card-body form::before{
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

  /* Native buttons in the toolbar become secondary compact controls */
  .card.mc-mobile-card-mode .card-body form .btn{
    min-height:42px!important;
    padding:0 13px!important;
    border-radius:13px!important;
    font-size:11px!important;
    box-shadow:none!important;
  }

  /* Hide redundant Search submit button: typing is already instant */
  .card.mc-mobile-card-mode .card-body form button[type="submit"],
  .card.mc-mobile-card-mode .card-body form input[type="submit"]{
    display:none!important;
  }

  /* Clear button / X */
  .card.mc-mobile-card-mode .card-body form a[href*="search="],
  .card.mc-mobile-card-mode .card-body form .btn-close,
  .card.mc-mobile-card-mode .card-body form [aria-label="Clear"]{
    position:absolute!important;
    right:8px!important;
    top:8px!important;
    width:34px!important;
    min-width:34px!important;
    height:34px!important;
    min-height:34px!important;
    padding:0!important;
    display:grid!important;
    place-items:center!important;
    border:0!important;
    border-radius:10px!important;
    background:#f2f5ef!important;
    color:#728077!important;
  }

  /* Actions / Export: softer pills */
  .card.mc-mobile-card-mode .dropdown .btn,
  .card.mc-mobile-card-mode .btn-group .btn{
    min-height:42px!important;
    padding:0 14px!important;
    border-radius:13px!important;
    background:#f5f7f3!important;
    border:1px solid rgba(31,107,45,.09)!important;
    color:#243126!important;
    font-size:11px!important;
    font-weight:800!important;
  }

  /* ---------- SELECTION BAR ---------- */
  .mc-mobile-selectbar{
    min-height:44px!important;
    margin:0 0 2px!important;
    padding:8px 11px!important;
    border-radius:13px!important;
    border:1px solid rgba(31,107,45,.09)!important;
    background:
      linear-gradient(90deg,#f7faf5,#fffaf0)!important;
    box-shadow:none!important;
  }

  .mc-mobile-selectbar-left{
    font-size:10.5px!important;
  }

  .mc-mobile-selected-count{
    padding:5px 8px!important;
    background:white!important;
    border:1px solid rgba(31,107,45,.09)!important;
    color:#2f793d!important;
    font-size:8.5px!important;
  }

  /* ---------- LIST CARDS ---------- */
  .card.mc-mobile-card-mode .mc-mobile-cards{
    gap:10px!important;
    padding:12px!important;
  }

  .mc-mobile-record-card{
    border-radius:17px!important;
    border:1px solid rgba(31,107,45,.10)!important;
    background:
      linear-gradient(145deg,#fffefb,#fbf9f2)!important;
    box-shadow:0 7px 18px rgba(18,63,29,.055)!important;
  }

  .mc-mobile-record-card::before{
    width:3px!important;
    background:linear-gradient(180deg,#2f843b,#d39a00)!important;
  }

  .mc-mobile-record-card.mc-selected{
    background:
      linear-gradient(145deg,#f5fbf4,#fffaf0)!important;
  }

  .mc-mobile-card-summary{
    min-height:76px!important;
    padding:12px 12px 12px 11px!important;
    gap:9px!important;
  }

  .mc-mobile-card-select-wrap{
    width:25px!important;
    min-width:25px!important;
    height:25px!important;
    border-radius:8px!important;
    background:#f1f5ef!important;
  }

  .mc-mobile-select,
  .mc-mobile-select-all{
    width:17px!important;
    height:17px!important;
    min-height:17px!important;
  }

  .mc-mobile-card-title{
    font-size:13.5px!important;
    line-height:1.25!important;
  }

  .mc-mobile-card-subtitle{
    margin-top:4px!important;
    font-size:10.5px!important;
    font-weight:600!important;
    color:#7d8690!important;
  }

  .mc-mobile-card-chevron{
    width:30px!important;
    height:30px!important;
    border-radius:10px!important;
    background:#edf4eb!important;
    font-size:15px!important;
  }

  .mc-mobile-record-card.mc-open .mc-mobile-card-chevron{
    background:#fff0c7!important;
  }

  /* ---------- EXPANDED CONTENT ---------- */
  .mc-mobile-card-details{
    padding:0 12px 13px!important;
    border-top:1px solid rgba(31,107,45,.07)!important;
    background:
      linear-gradient(180deg,rgba(245,240,228,.22),rgba(255,255,255,0))!important;
  }

  .mc-mobile-card-grid{
    padding-top:5px!important;
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:7px!important;
  }

  .mc-mobile-detail-row{
    min-height:auto!important;
    padding:9px 10px!important;
    display:grid!important;
    grid-template-columns:88px minmax(0,1fr)!important;
    gap:10px!important;
    align-items:center!important;
    border:1px solid rgba(31,107,45,.065)!important;
    border-radius:11px!important;
    background:rgba(255,255,255,.76)!important;
  }

  .mc-mobile-detail-label{
    padding:0!important;
    color:#79847b!important;
    font-size:7.8px!important;
    letter-spacing:.08em!important;
  }

  .mc-mobile-detail-value{
    color:#26362a!important;
    font-size:11.5px!important;
    line-height:1.4!important;
  }

  /* Message field gets a readable note treatment */
  .mc-mobile-detail-row:has(.mc-mobile-detail-label){
    transition:background .18s ease!important;
  }

  .mc-mobile-card-actions{
    margin-top:9px!important;
    padding-top:10px!important;
    gap:7px!important;
    border-top:0!important;
  }

  .mc-mobile-card-actions a,
  .mc-mobile-card-actions button{
    width:36px!important;
    min-width:36px!important;
    height:36px!important;
    min-height:36px!important;
    border-radius:10px!important;
    box-shadow:none!important;
  }

  .mc-mobile-card-actions a[href*="/delete"],
  .mc-mobile-card-actions a[data-bs-target*="delete"],
  .mc-mobile-card-actions button[data-bs-target*="delete"],
  .mc-mobile-card-actions .text-danger{
    color:#c63f35!important;
    background:#fff3f1!important;
    border-color:rgba(198,63,53,.14)!important;
  }

  /* ---------- DETAIL / VIEW PAGES ---------- */
  /* Since list-card conversion is now restricted to /list, native view pages
     get a clean "information sheet" treatment instead of many accordions. */
  body .card:not(.mc-mobile-card-mode) .table-responsive{
    border-radius:15px!important;
  }

  body .card:not(.mc-mobile-card-mode) .table tbody tr{
    background:transparent!important;
  }

  body .card:not(.mc-mobile-card-mode) .table tbody td{
    padding:12px 10px!important;
  }
}


/* =========================================================
   FILTRES ÉVÉNEMENTS — MOBILE
   Type d'événement + statut, générés depuis les données visibles.
========================================================= */
@media(max-width:575.98px){
  .mc-event-filters{
    margin:0 0 2px;
    padding:11px;
    display:grid;
    gap:9px;
    border:1px solid rgba(31,107,45,.10);
    border-radius:15px;
    background:linear-gradient(135deg,#f8fbf6,#fff9ed);
  }

  .mc-event-filter-head{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
  }

  .mc-event-filter-title{
    display:flex;
    align-items:center;
    gap:7px;
    color:var(--mc-dark);
    font-size:11px;
    font-weight:850;
  }

  .mc-event-filter-title::before{
    content:"⚲";
    width:25px;
    height:25px;
    display:grid;
    place-items:center;
    border-radius:8px;
    background:#edf4eb;
    color:var(--mc-green);
    font-size:14px;
  }

  .mc-event-filter-reset{
    min-height:30px!important;
    padding:0 9px!important;
    border:1px solid rgba(196,125,14,.16)!important;
    border-radius:9px!important;
    background:#fff8e8!important;
    color:#936200!important;
    font-size:8.5px!important;
    font-weight:850!important;
  }

  .mc-event-filter-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
  }

  .mc-event-filter-field{
    display:grid;
    gap:5px;
  }

  .mc-event-filter-label{
    color:#77827a;
    font-size:7.5px;
    font-weight:900;
    letter-spacing:.08em;
    text-transform:uppercase;
  }

  .mc-event-filter-select{
    width:100%;
    min-height:38px!important;
    padding:0 28px 0 10px!important;
    border:1px solid rgba(31,107,45,.13)!important;
    border-radius:11px!important;
    background:#fff!important;
    color:#24402a!important;
    font-size:10px!important;
    font-weight:700!important;
    box-shadow:none!important;
  }

  .mc-event-filter-result{
    color:#738078;
    font-size:8.5px;
    font-weight:700;
  }

  .mc-mobile-record-card.mc-event-filter-hidden{
    display:none!important;
  }

  .mc-event-no-results{
    padding:24px 14px;
    border:1px dashed rgba(31,107,45,.16);
    border-radius:14px;
    background:rgba(255,255,255,.62);
    color:#78827b;
    text-align:center;
    font-size:11px;
  }
}


/* =========================================================
   FILTRE PLATS PAR CATÉGORIE — MOBILE
========================================================= */
@media(max-width:575.98px){
  .mc-dish-filters{
    margin:0 0 2px;
    padding:11px;
    display:grid;
    gap:9px;
    border:1px solid rgba(31,107,45,.10);
    border-radius:15px;
    background:linear-gradient(135deg,#f8fbf6,#fff9ed);
  }

  .mc-dish-filter-head{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
  }

  .mc-dish-filter-title{
    display:flex;
    align-items:center;
    gap:7px;
    color:var(--mc-dark);
    font-size:11px;
    font-weight:850;
  }

  .mc-dish-filter-title::before{
    content:"☷";
    width:25px;
    height:25px;
    display:grid;
    place-items:center;
    border-radius:8px;
    background:#edf4eb;
    color:var(--mc-green);
    font-size:14px;
  }

  .mc-dish-filter-reset{
    min-height:30px!important;
    padding:0 9px!important;
    border:1px solid rgba(196,125,14,.16)!important;
    border-radius:9px!important;
    background:#fff8e8!important;
    color:#936200!important;
    font-size:8.5px!important;
    font-weight:850!important;
  }

  .mc-dish-filter-field{
    display:grid;
    gap:5px;
  }

  .mc-dish-filter-label{
    color:#77827a;
    font-size:7.5px;
    font-weight:900;
    letter-spacing:.08em;
    text-transform:uppercase;
  }

  .mc-dish-filter-select{
    width:100%;
    min-height:40px!important;
    padding:0 34px 0 11px!important;
    border:1px solid rgba(31,107,45,.13)!important;
    border-radius:11px!important;
    background:#fff!important;
    color:#24402a!important;
    font-size:10.5px!important;
    font-weight:700!important;
    box-shadow:none!important;
  }

  .mc-dish-filter-result{
    color:#738078;
    font-size:8.5px;
    font-weight:700;
  }

  .mc-mobile-record-card.mc-dish-filter-hidden{
    display:none!important;
  }

  .mc-dish-no-results{
    padding:24px 14px;
    border:1px dashed rgba(31,107,45,.16);
    border-radius:14px;
    background:rgba(255,255,255,.62);
    color:#78827b;
    text-align:center;
    font-size:11px;
  }
}


/* =========================================================
   FILTRE PLATS PAR CATÉGORIE — DESKTOP
========================================================= */
@media(min-width:576px){
  .mc-dish-desktop-filters{
    margin:18px 22px 16px;
    padding:16px 18px;
    display:flex;
    align-items:end;
    gap:14px;
    border:1px solid rgba(31,107,45,.10);
    border-radius:18px;
    background:linear-gradient(135deg,#f8fbf6,#fff9ed);
    box-shadow:0 8px 20px rgba(18,63,29,.05);
  }

  .mc-dish-desktop-filter-main{
    flex:1 1 auto;
    display:grid;
    gap:7px;
    min-width:220px;
  }

  .mc-dish-desktop-filter-label{
    color:#6f7c73;
    font-size:9px;
    font-weight:900;
    letter-spacing:.09em;
    text-transform:uppercase;
  }

  .mc-dish-desktop-filter-select{
    width:100%;
    min-height:44px!important;
    padding:0 38px 0 13px!important;
    border:1px solid rgba(31,107,45,.18)!important;
    border-radius:13px!important;
    background:#fff!important;
    color:#24402a!important;
    font-size:12px!important;
    font-weight:750!important;
    box-shadow:none!important;
  }

  .mc-dish-desktop-filter-select:focus{
    border-color:var(--mc-green)!important;
    box-shadow:0 0 0 4px rgba(31,107,45,.08)!important;
  }

  .mc-dish-desktop-filter-reset{
    min-height:44px!important;
    padding:0 16px!important;
    border:1px solid rgba(196,125,14,.20)!important;
    border-radius:13px!important;
    background:#fff8e8!important;
    color:#8c5d00!important;
    font-size:11px!important;
    font-weight:850!important;
    white-space:nowrap;
  }

  .mc-dish-desktop-filter-result{
    min-width:145px;
    padding-bottom:12px;
    color:#6f7c73;
    font-size:10px;
    font-weight:750;
    text-align:right;
    white-space:nowrap;
  }

  .mc-dish-desktop-empty{
    margin:0 22px 20px;
    padding:28px 18px;
    border:1px dashed rgba(31,107,45,.16);
    border-radius:16px;
    background:rgba(255,255,255,.66);
    color:#78827b;
    text-align:center;
    font-size:12px;
  }
}


/* =========================================================
   FIX — NEVER SHOW DESKTOP + MOBILE DISH FILTERS TOGETHER
========================================================= */

/* Mobile: hide desktop filter completely */
@media(max-width:575.98px){
  .mc-dish-desktop-filters,
  .mc-dish-desktop-empty{
    display:none!important;
  }
}

/* Desktop: hide the mobile dish filter completely */
@media(min-width:576px){
  .mc-dish-filters,
  .mc-dish-no-results{
    display:none!important;
  }

  /* Desktop must keep the real SQLAdmin table visible */
  .card.mc-mobile-card-mode .table-responsive{
    display:block!important;
  }

  .card.mc-mobile-card-mode .mc-mobile-cards{
    display:none!important;
  }
}


/* =========================================================
   MOBILE CARDS — 2 COLONNES RECTANGULAIRES
   Même organisation visuelle que la version desktop :
   nom + catégorie + prix + disponibilité directement visibles.
========================================================= */
@media(max-width:575.98px){
  .card.mc-mobile-card-mode .mc-mobile-cards{
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:10px!important;
    padding:12px 10px 18px!important;
    align-items:start!important;
  }

  .mc-mobile-selectbar,.mc-event-filters,.mc-dish-filters,
  .mc-event-no-results,.mc-dish-no-results{
    grid-column:1 / -1!important;
  }

  /* La sélection multiple ne sert qu'à une seule action ("Supprimer"),
     déjà accessible individuellement sur chaque carte (bouton ⌄ puis
     icône corbeille) : on masque la barre "Tout sélectionner" et les
     cases à cocher sur mobile pour simplifier l'interface. */
  .mc-mobile-selectbar,
  .mc-mobile-card-select-wrap{
    display:none!important;
  }

  .mc-mobile-record-card{
    min-width:0!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.11)!important;
    border-radius:15px!important;
    background:linear-gradient(145deg,#fffefb,#fbf9f2)!important;
    box-shadow:0 7px 18px rgba(18,63,29,.055)!important;
  }

  .mc-mobile-record-card::before{
    width:3px!important;
    opacity:0!important;
    background:linear-gradient(180deg,var(--mc-green),var(--mc-gold))!important;
  }
  .mc-mobile-record-card.mc-selected::before,
  .mc-mobile-record-card.mc-open::before{opacity:1!important}

  /* Vraie vignette photo du plat (colonne "Photo" détectée dans le tableau
     natif), affichée en cercle centré au sommet de la carte. */
  .mc-mobile-card-photo-wrap{
    width:64px!important;
    height:64px!important;
    margin:14px auto 0!important;
    overflow:hidden!important;
    border-radius:50%!important;
    background:#eef4ec!important;
    border:2px solid #fffdf8!important;
    box-shadow:0 3px 10px rgba(18,63,29,.14)!important;
  }
  .mc-mobile-card-photo{
    width:100%!important;
    height:100%!important;
    object-fit:cover!important;
    display:block!important;
  }
  .mc-mobile-card-photo-placeholder{
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    font-size:22px!important;
    color:#a9b6ad!important;
  }
  .mc-mobile-record-card.mc-open .mc-mobile-card-photo-wrap{
    width:72px!important;
    height:72px!important;
  }

  .mc-mobile-card-summary{
    position:relative!important;
    min-height:154px!important;
    padding:13px 12px 12px!important;
    display:block!important;
    background:transparent!important;
  }


  .mc-mobile-card-select-wrap{
    display:none!important;
  }
  .mc-mobile-select{width:14px!important;height:14px!important;min-height:14px!important}

  .mc-mobile-card-main{
    width:100%!important;
    min-width:0!important;
    padding:28px 0 34px!important;
    display:block!important;
    border:0!important;
    background:transparent!important;
    text-align:left!important;
  }

  .mc-mobile-card-title{
    color:#174623!important;
    font-size:12.5px!important;
    font-weight:900!important;
    line-height:1.22!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .mc-mobile-card-subtitle{
    margin-top:5px!important;
    color:#7b8490!important;
    font-size:9px!important;
    font-weight:650!important;
    line-height:1.25!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .mc-mobile-card-quick{
    margin-top:10px!important;
    display:grid!important;
    gap:6px!important;
  }
  .mc-mobile-card-category{
    width:max-content!important;
    max-width:100%!important;
    padding:4px 7px!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.09)!important;
    border-radius:999px!important;
    background:#edf4eb!important;
    color:#2c6b36!important;
    font-size:8px!important;
    font-weight:850!important;
    line-height:1!important;
    text-overflow:ellipsis!important;
    white-space:nowrap!important;
  }
  .mc-mobile-card-price{
    color:#174623!important;
    font-size:13px!important;
    font-weight:900!important;
    line-height:1!important;
  }
  .mc-mobile-card-availability{
    min-width:0!important;
    display:flex!important;
    align-items:center!important;
    gap:5px!important;
    color:#667269!important;
    font-size:8.5px!important;
    font-weight:800!important;
    line-height:1.2!important;
  }
  .mc-mobile-card-availability-dot{
    width:8px!important;
    height:8px!important;
    min-width:8px!important;
    display:block!important;
    border-radius:50%!important;
  }
  .mc-mobile-card-availability-dot.mc-state-green{background:#43b96b!important}
  .mc-mobile-card-availability-dot.mc-state-red{background:#d94b45!important}
  .mc-mobile-card-availability-dot.mc-state-yellow{background:#e2b635!important}
  .mc-mobile-card-availability-dot.mc-state-neutral{background:#a9b0aa!important}

  .mc-mobile-state-dot{
    position:absolute!important;
    top:9px!important;
    right:9px!important;
    width:16px!important;
    height:16px!important;
    display:block!important;
    border:2px solid #fffdf8!important;
    border-radius:50%!important;
    box-shadow:0 0 0 1px rgba(18,63,29,.10),0 2px 7px rgba(18,63,29,.22)!important;
    z-index:8!important;
    cursor:pointer!important;
  }
  .mc-mobile-state-dot.mc-state-green{background:#43b96b!important}
  .mc-mobile-state-dot.mc-state-red{background:#d94b45!important}
  .mc-mobile-state-dot.mc-state-yellow{background:#e2b635!important}
  .mc-mobile-state-dot.mc-state-neutral{background:#a9b0aa!important}

  /* Bulle d'info au survol/appui, affiche le statut en toutes lettres
     (ex: "Disponible") au lieu de compter uniquement sur la couleur. */
  .mc-mobile-state-dot::after{
    content:attr(data-tooltip)!important;
    position:absolute!important;
    top:calc(100% + 8px)!important;
    right:0!important;
    padding:5px 9px!important;
    border-radius:8px!important;
    background:#123f1d!important;
    color:#fffdf8!important;
    font-size:10px!important;
    font-weight:800!important;
    white-space:nowrap!important;
    opacity:0!important;
    pointer-events:none!important;
    transform:translateY(-4px)!important;
    transition:opacity .15s ease,transform .15s ease!important;
    box-shadow:0 8px 18px rgba(9,43,18,.28)!important;
    z-index:20!important;
  }
  .mc-mobile-state-dot:hover::after,
  .mc-mobile-state-dot:focus-visible::after{
    opacity:1!important;
    transform:translateY(0)!important;
  }

  .mc-mobile-card-chevron{
    position:absolute!important;
    right:9px!important;
    bottom:9px!important;
    width:27px!important;
    min-width:27px!important;
    height:27px!important;
    min-height:27px!important;
    display:grid!important;
    place-items:center!important;
    border-radius:9px!important;
    background:#edf4eb!important;
    color:#174623!important;
    font-size:13px!important;
  }

  /* Bulle d'info au survol : le bouton est en bas de carte, donc la
     bulle s'ouvre vers le haut pour rester visible. */
  .mc-mobile-card-chevron::after{
    content:attr(data-tooltip)!important;
    position:absolute!important;
    bottom:calc(100% + 8px)!important;
    right:0!important;
    padding:5px 9px!important;
    border-radius:8px!important;
    background:#123f1d!important;
    color:#fffdf8!important;
    font-size:10px!important;
    font-weight:800!important;
    white-space:nowrap!important;
    opacity:0!important;
    pointer-events:none!important;
    transform:translateY(4px)!important;
    transition:opacity .15s ease,transform .15s ease!important;
    box-shadow:0 8px 18px rgba(9,43,18,.28)!important;
    z-index:20!important;
  }
  .mc-mobile-card-chevron:hover::after,
  .mc-mobile-card-chevron:focus-visible::after{
    opacity:1!important;
    transform:translateY(0)!important;
  }

  .mc-mobile-record-card.mc-open{grid-column:1 / -1!important}
  .mc-mobile-record-card.mc-open .mc-mobile-card-summary{min-height:120px!important}
  .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:7px!important;
  }
  .mc-mobile-record-card.mc-open .mc-mobile-detail-row{
    grid-template-columns:76px minmax(0,1fr)!important;
    min-height:52px!important;
    padding:8px!important;
  }
}
@media(max-width:380px){
  .card.mc-mobile-card-mode .mc-mobile-cards{gap:7px!important;padding-left:7px!important;padding-right:7px!important}
  .mc-mobile-card-summary{min-height:148px!important;padding-left:9px!important;padding-right:9px!important}
  .mc-mobile-card-title{font-size:11.5px!important}
  .mc-mobile-card-subtitle{font-size:8.4px!important}
  .mc-mobile-card-price{font-size:12px!important}
  .mc-mobile-card-availability{font-size:8px!important}
}

/* =========================================================
   DESKTOP SIDEBAR ACCOUNT — remove duplicated bottom-left text
   Keep only the MC avatar and chevron on desktop.
========================================================= */
@media(min-width:992px){
  .mc-sidebar-account{
    left:16px!important;
    right:16px!important;
    bottom:14px!important;
    height:48px!important;
    padding:0 12px!important;
    justify-content:space-between!important;
    gap:8px!important;
  }

  .mc-sidebar-account-name{
    display:none!important;
  }

  .mc-sidebar-avatar{
    width:30px!important;
    height:30px!important;
    min-width:30px!important;
    flex:0 0 auto!important;
  }

  .mc-sidebar-chevron{
    display:block!important;
    margin-left:auto!important;
    flex:0 0 auto!important;
  }

  /* Extra safety: disable the old pseudo-account if any previous rule still exists */
  .navbar-vertical::after{
    display:none!important;
    content:none!important;
  }
}


/* =========================================================
   REGROUPEMENT DES ARTICLES COMMANDÉS PAR COMMANDE — MOBILE
   Évite d'afficher N cartes identiques "Commande #X" séparées
   pour une même commande : on les regroupe visuellement sous
   un seul en-tête, tout en gardant 2 colonnes par groupe.
========================================================= */
@media(max-width:575.98px){
  .mc-order-group{
    grid-column:1 / -1!important;
    margin-bottom:2px;
    overflow:hidden;
    border:1px solid rgba(31,107,45,.11);
    border-radius:16px;
    background:rgba(255,253,248,.92);
    box-shadow:0 7px 18px rgba(18,63,29,.05);
  }

  .mc-order-group-header{
    padding:10px 13px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
    background:linear-gradient(90deg,#eef6ec,#fff9ec);
    border-bottom:1px solid rgba(31,107,45,.08);
  }

  .mc-order-group-title{
    color:#174623;
    font-size:13px;
    font-weight:900;
  }

  .mc-order-group-count{
    padding:3px 9px;
    border-radius:999px;
    background:#fff;
    border:1px solid rgba(31,107,45,.12);
    color:#5f6b62;
    font-size:9px;
    font-weight:850;
    white-space:nowrap;
  }

  .mc-order-group-items{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:8px;
    padding:10px;
  }

  .mc-order-group-items .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }
}


/* =========================================================
   COMMANDES — FIX TOTAL + CRÉNEAU
   - garde les deux blocs côte à côte
   - empêche le montant de dépasser
   - laisse plus de largeur au total sur petits écrans
========================================================= */
@media(max-width:991.98px){
  .mc-mobile-record-card .mc-order-metric-card{
    min-height:108px!important;
    padding:14px 15px!important;
    align-items:flex-start!important;
    border:1px solid rgba(31,107,45,.08)!important;
    border-radius:18px!important;
    background:linear-gradient(180deg,#fffefb,#fcfaf4)!important;
    box-shadow:0 4px 14px rgba(18,63,29,.04)!important;
  }

  .mc-mobile-record-card .mc-order-metric-total{
    min-width:132px!important;
    grid-template-columns:1fr!important;
  }

  .mc-mobile-record-card .mc-order-metric-total .mc-mobile-detail-label{
    padding:0!important;
    font-size:10px!important;
    letter-spacing:.10em!important;
    line-height:1.1!important;
  }

  .mc-mobile-record-card .mc-order-metric-total .mc-mobile-detail-value{
    display:block!important;
    width:100%!important;
    min-width:0!important;
    max-width:100%!important;
    overflow:hidden!important;
    white-space:nowrap!important;
    text-overflow:clip!important;
    color:#b47d00!important;
    font-size:clamp(17px,2.8vw,22px)!important;
    font-weight:900!important;
    line-height:1.02!important;
    letter-spacing:-.03em!important;
  }

  .mc-mobile-record-card .mc-order-metric-total .mc-mobile-detail-value *{
    display:inline!important;
    font-size:inherit!important;
    font-weight:inherit!important;
    line-height:inherit!important;
    letter-spacing:inherit!important;
    white-space:inherit!important;
  }

  .mc-mobile-record-card .mc-order-metric-slot{
    min-width:0!important;
    grid-template-columns:1fr!important;
  }

  .mc-mobile-record-card .mc-order-metric-slot .mc-mobile-detail-label{
    padding:0!important;
    line-height:1.1!important;
  }

  .mc-mobile-record-card .mc-order-metric-slot .mc-mobile-detail-value{
    min-width:0!important;
    white-space:normal!important;
    overflow-wrap:anywhere!important;
    line-height:1.28!important;
  }
}

@media(max-width:575.98px){
  /* Sur les commandes ouvertes : Total + Créneau restent alignés. */
  .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    grid-template-columns:minmax(126px,.82fr) minmax(0,1.18fr)!important;
    gap:10px!important;
  }

  .mc-mobile-record-card .mc-order-metric-total{
    min-width:126px!important;
    padding:13px 12px!important;
  }

  .mc-mobile-record-card .mc-order-metric-total .mc-mobile-detail-value{
    font-size:clamp(15px,4.2vw,19px)!important;
  }
}

@media(max-width:380px){
  .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    grid-template-columns:minmax(116px,.82fr) minmax(0,1.18fr)!important;
    gap:8px!important;
  }

  .mc-mobile-record-card .mc-order-metric-total{
    min-width:116px!important;
    padding-left:10px!important;
    padding-right:10px!important;
  }

  .mc-mobile-record-card .mc-order-metric-total .mc-mobile-detail-value{
    font-size:15px!important;
  }
}


/* =========================================================
   ARTICLES COMMANDÉS — FINAL OVERRIDE
   Placé en dernier pour gagner sur toutes les anciennes règles
   génériques de cartes mobiles.
========================================================= */
@media(max-width:575.98px){
  .card.mc-order-item-card-mode .mc-mobile-cards{
    display:flex!important;
    flex-direction:column!important;
    gap:16px!important;
    padding:14px 10px 20px!important;
  }

  .card.mc-order-item-card-mode .mc-order-group{
    width:100%!important;
    margin:0!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:22px!important;
    background:linear-gradient(180deg,#fffefb 0%,#fbfaf5 100%)!important;
    box-shadow:0 10px 26px rgba(18,63,29,.055)!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-header{
    min-height:72px!important;
    padding:14px 16px!important;
    display:flex!important;
    align-items:center!important;
    justify-content:space-between!important;
    gap:12px!important;
    border-bottom:1px solid rgba(31,107,45,.08)!important;
    background:
      radial-gradient(circle at 94% 0,rgba(228,184,63,.12),transparent 90px),
      linear-gradient(90deg,#eef6ec,#fffaf0)!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-heading{
    display:flex!important;
    align-items:baseline!important;
    gap:8px!important;
    min-width:0!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-kicker{
    color:#8b690d!important;
    font-size:8px!important;
    font-weight:900!important;
    letter-spacing:.16em!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-title{
    color:#174623!important;
    font-family:Georgia,"Times New Roman",serif!important;
    font-size:25px!important;
    font-weight:700!important;
    line-height:1!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-count{
    flex:0 0 auto!important;
    padding:7px 11px!important;
    border:1px solid rgba(31,107,45,.12)!important;
    border-radius:999px!important;
    background:#fff!important;
    color:#677269!important;
    font-size:10px!important;
    font-weight:900!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-items{
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:10px!important;
    padding:11px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card{
    position:relative!important;
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:18px!important;
    background:#fffdf9!important;
    box-shadow:0 5px 14px rgba(18,63,29,.045)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card::before{
    content:""!important;
    position:absolute!important;
    left:0!important;
    top:0!important;
    bottom:0!important;
    width:4px!important;
    opacity:1!important;
    background:linear-gradient(180deg,#2d742d 0%,#d1a112 100%)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-summary{
    position:relative!important;
    min-height:0!important;
    height:auto!important;
    padding:15px 58px 15px 17px!important;
    display:block!important;
    background:transparent!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-main{
    width:100%!important;
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    padding:0!important;
    display:block!important;
    border:0!important;
    background:transparent!important;
    text-align:left!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-title{
    margin:0!important;
    color:#174623!important;
    font-size:16px!important;
    font-weight:900!important;
    line-height:1.25!important;
    white-space:normal!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-subtitle,
  .card.mc-order-item-card-mode .mc-mobile-card-quick,
  .card.mc-order-item-card-mode .mc-mobile-state-dot{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview{
    margin-top:11px!important;
    display:grid!important;
    gap:7px!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chips{
    display:flex!important;
    align-items:center!important;
    flex-wrap:wrap!important;
    gap:7px!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chip{
    min-height:29px!important;
    padding:0 10px!important;
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    border-radius:999px!important;
    border:1px solid rgba(31,107,45,.12)!important;
    background:#edf5eb!important;
    color:#2d6a36!important;
    font-size:11px!important;
    font-weight:900!important;
    line-height:1!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chip.mc-price{
    border-color:rgba(204,155,11,.25)!important;
    background:#fff3cf!important;
    color:#9c6d00!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-note{
    color:#717a73!important;
    font-size:10.5px!important;
    font-weight:650!important;
    line-height:1.38!important;
    white-space:normal!important;
    overflow-wrap:anywhere!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-note strong{
    color:#4d5e51!important;
    font-weight:900!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-chevron{
    position:absolute!important;
    top:50%!important;
    right:14px!important;
    bottom:auto!important;
    transform:translateY(-50%)!important;
    width:37px!important;
    min-width:37px!important;
    height:37px!important;
    min-height:37px!important;
    display:grid!important;
    place-items:center!important;
    border:1px solid rgba(31,107,45,.12)!important;
    border-radius:50%!important;
    background:#f1f7ef!important;
    color:#23672e!important;
    font-family:Georgia,serif!important;
    font-size:27px!important;
    font-weight:900!important;
    line-height:1!important;
    box-shadow:0 4px 11px rgba(18,63,29,.06)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-chevron::after{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-chevron{
    transform:translateY(-50%) rotate(90deg)!important;
    background:#fff1c9!important;
    color:#8d6200!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-details{
    padding:0 12px 12px!important;
    border-top:1px dashed rgba(177,143,53,.30)!important;
    background:linear-gradient(180deg,rgba(247,240,228,.30),rgba(255,255,255,0))!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-grid,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    padding-top:11px!important;
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:9px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-detail-row{
    min-width:0!important;
    min-height:76px!important;
    padding:11px!important;
    display:flex!important;
    flex-direction:column!important;
    align-items:flex-start!important;
    justify-content:center!important;
    gap:7px!important;
    border:1px solid rgba(31,107,45,.075)!important;
    border-radius:14px!important;
    background:rgba(255,255,255,.82)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-label{
    width:100%!important;
    padding:0!important;
    color:#7b847d!important;
    font-size:8px!important;
    font-weight:900!important;
    letter-spacing:.10em!important;
    line-height:1.2!important;
    white-space:normal!important;
    word-break:normal!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-value{
    width:100%!important;
    min-width:0!important;
    color:#26352a!important;
    font-size:12px!important;
    font-weight:700!important;
    line-height:1.38!important;
    white-space:normal!important;
    word-break:normal!important;
    overflow-wrap:anywhere!important;
  }

  /* Redondants : le groupe et le titre donnent déjà commande + plat. */
  .card.mc-order-item-card-mode .mc-order-item-detail-order,
  .card.mc-order-item-card-mode .mc-order-item-detail-dish{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-qty .mc-mobile-detail-value,
  .card.mc-order-item-card-mode .mc-order-item-detail-price .mc-mobile-detail-value{
    font-size:19px!important;
    font-weight:900!important;
    line-height:1.05!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-price .mc-mobile-detail-value{
    color:#ad7900!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-note,
  .card.mc-order-item-card-mode .mc-order-item-detail-options{
    grid-column:1 / -1!important;
    min-height:0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-actions{
    margin-top:10px!important;
    padding-top:0!important;
    display:flex!important;
    gap:8px!important;
    border-top:0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-actions a,
  .card.mc-order-item-card-mode .mc-mobile-card-actions button{
    width:40px!important;
    min-width:40px!important;
    height:40px!important;
    min-height:40px!important;
    border-radius:12px!important;
  }
}

@media(min-width:470px) and (max-width:575.98px){
  .card.mc-order-item-card-mode .mc-order-group-items{
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }
}

@media(max-width:390px){
  .card.mc-order-item-card-mode .mc-mobile-card-grid,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    grid-template-columns:1fr!important;
  }
}



/* =========================================================
   ARTICLES COMMANDÉS — CLEAN UX FINAL
   This block intentionally comes LAST and affects only
   /admin/order-item/list via .mc-order-item-card-mode.
========================================================= */
@media(max-width:575.98px){
  .card.mc-order-item-card-mode .mc-mobile-cards{
    display:flex!important;
    flex-direction:column!important;
    gap:18px!important;
    padding:14px 10px 22px!important;
  }

  .card.mc-order-item-card-mode .mc-order-group{
    width:100%!important;
    margin:0!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.11)!important;
    border-radius:22px!important;
    background:#fffdf9!important;
    box-shadow:0 10px 28px rgba(18,63,29,.065)!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-header{
    min-height:68px!important;
    padding:13px 16px!important;
    display:flex!important;
    align-items:center!important;
    justify-content:space-between!important;
    gap:12px!important;
    border-bottom:1px solid rgba(31,107,45,.085)!important;
    background:
      radial-gradient(circle at 100% 0,rgba(228,184,63,.14),transparent 110px),
      linear-gradient(100deg,#eef6ec 0%,#fffaf0 100%)!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-heading{
    min-width:0!important;
    display:flex!important;
    align-items:center!important;
    gap:9px!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-kicker{
    color:#917006!important;
    font-size:8px!important;
    font-weight:950!important;
    letter-spacing:.17em!important;
    text-transform:uppercase!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-title{
    color:#174623!important;
    font-family:Georgia,"Times New Roman",serif!important;
    font-size:25px!important;
    font-weight:700!important;
    line-height:1!important;
    letter-spacing:-.02em!important;
  }

  .card.mc-order-item-card-mode .mc-order-group-count{
    flex:0 0 auto!important;
    min-width:68px!important;
    padding:7px 10px!important;
    border:1px solid rgba(31,107,45,.12)!important;
    border-radius:999px!important;
    background:rgba(255,255,255,.9)!important;
    color:#68736b!important;
    font-size:9.5px!important;
    font-weight:900!important;
    text-align:center!important;
  }

  /* One article = full width. Multiple articles = tidy 2-col grid. */
  .card.mc-order-item-card-mode .mc-order-group-items{
    width:100%!important;
    padding:12px!important;
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:10px!important;
    align-items:start!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card{
    width:100%!important;
    min-width:0!important;
    min-height:0!important;
    height:auto!important;
    align-self:start!important;
    overflow:hidden!important;
    border:1px solid rgba(31,107,45,.10)!important;
    border-radius:17px!important;
    background:linear-gradient(145deg,#fffefb,#fbfaf5)!important;
    box-shadow:0 5px 14px rgba(18,63,29,.045)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card::before{
    width:4px!important;
    opacity:1!important;
    background:linear-gradient(180deg,#2f7b32 0%,#d6a50e 100%)!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-summary{
    min-height:0!important;
    height:auto!important;
    padding:15px 54px 15px 18px!important;
    display:block!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-main{
    width:100%!important;
    min-height:0!important;
    height:auto!important;
    padding:0!important;
    display:block!important;
    text-align:left!important;
    background:transparent!important;
    border:0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-title{
    margin:0!important;
    color:#174623!important;
    font-size:16px!important;
    font-weight:900!important;
    line-height:1.25!important;
    white-space:normal!important;
    display:block!important;
    overflow:visible!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-subtitle,
  .card.mc-order-item-card-mode .mc-mobile-card-quick,
  .card.mc-order-item-card-mode .mc-mobile-state-dot,
  .card.mc-order-item-card-mode .mc-order-item-inline-metrics,
  .card.mc-order-item-card-mode .mc-order-item-note{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview{
    margin-top:11px!important;
    display:grid!important;
    gap:7px!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chips{
    display:flex!important;
    align-items:center!important;
    flex-wrap:wrap!important;
    gap:7px!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chip{
    min-height:29px!important;
    padding:0 10px!important;
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    border:1px solid rgba(31,107,45,.13)!important;
    border-radius:999px!important;
    background:#edf5eb!important;
    color:#2f6b38!important;
    font-size:10.5px!important;
    font-weight:900!important;
    line-height:1!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-chip.mc-price{
    border-color:rgba(204,155,11,.27)!important;
    background:#fff3cf!important;
    color:#9b6c00!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-note{
    max-width:100%!important;
    color:#6f7971!important;
    font-size:10.5px!important;
    font-weight:650!important;
    line-height:1.38!important;
    white-space:normal!important;
    overflow-wrap:anywhere!important;
    display:-webkit-box!important;
    -webkit-box-orient:vertical!important;
    -webkit-line-clamp:2!important;
    overflow:hidden!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-preview-note strong{
    color:#4b5e50!important;
    font-weight:900!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-chevron{
    position:absolute!important;
    top:50%!important;
    right:13px!important;
    bottom:auto!important;
    transform:translateY(-50%)!important;
    width:36px!important;
    min-width:36px!important;
    height:36px!important;
    min-height:36px!important;
    display:grid!important;
    place-items:center!important;
    border:1px solid rgba(31,107,45,.12)!important;
    border-radius:50%!important;
    background:#f0f6ee!important;
    color:#287034!important;
    font-family:Georgia,serif!important;
    font-size:25px!important;
    font-weight:900!important;
    line-height:1!important;
    box-shadow:none!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-chevron{
    transform:translateY(-50%) rotate(90deg)!important;
    background:#fff0c8!important;
    color:#8d6200!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-details{
    padding:0 12px 12px!important;
    border-top:1px dashed rgba(177,143,53,.28)!important;
    background:linear-gradient(180deg,rgba(247,240,228,.26),rgba(255,255,255,0))!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-card-grid,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    padding-top:10px!important;
    display:grid!important;
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
    gap:8px!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-row,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-detail-row{
    min-width:0!important;
    min-height:68px!important;
    padding:10px!important;
    display:flex!important;
    flex-direction:column!important;
    align-items:flex-start!important;
    justify-content:center!important;
    gap:6px!important;
    border:1px solid rgba(31,107,45,.075)!important;
    border-radius:12px!important;
    background:rgba(255,255,255,.82)!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-order,
  .card.mc-order-item-card-mode .mc-order-item-detail-dish{
    display:none!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-note,
  .card.mc-order-item-card-mode .mc-order-item-detail-options{
    grid-column:1 / -1!important;
    min-height:0!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-label{
    color:#7b847d!important;
    font-size:7.5px!important;
    font-weight:900!important;
    letter-spacing:.09em!important;
    line-height:1.2!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-detail-value{
    width:100%!important;
    min-width:0!important;
    color:#26352a!important;
    font-size:11.5px!important;
    font-weight:700!important;
    line-height:1.35!important;
    overflow-wrap:anywhere!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-qty .mc-mobile-detail-value,
  .card.mc-order-item-card-mode .mc-order-item-detail-price .mc-mobile-detail-value{
    font-size:17px!important;
    font-weight:900!important;
  }

  .card.mc-order-item-card-mode .mc-order-item-detail-price .mc-mobile-detail-value{
    color:#a87300!important;
  }
}

@media(min-width:470px) and (max-width:575.98px){
  .card.mc-order-item-card-mode .mc-order-group-items{
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
  }

  /* A single article uses the whole row. */
  .card.mc-order-item-card-mode .mc-order-group-items > .mc-mobile-record-card:only-child{
    grid-column:1 / -1!important;
  }

  /* With an odd number of articles, the last one fills the empty row. */
  .card.mc-order-item-card-mode .mc-order-group-items > .mc-mobile-record-card:last-child:nth-child(odd){
    grid-column:1 / -1!important;
  }

  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open{
    grid-column:1 / -1!important;
  }
}

@media(max-width:390px){
  .card.mc-order-item-card-mode .mc-mobile-card-grid,
  .card.mc-order-item-card-mode .mc-mobile-record-card.mc-open .mc-mobile-card-grid{
    grid-template-columns:1fr!important;
  }
}

</style>

<script id="miss-chawarma-admin-script">
(function(){

  /* =========================================================
     TRADUCTION FR/EN
     — Le changement de langue recharge la page (simple, sans
       MutationObserver, aucun risque de conflit avec le calendrier
       ou le modal). mcApplyLanguage() est appelé UNE fois après
       chaque construction de contenu dynamique, jamais en boucle.
  ========================================================= */

  var MC_DICT = {
    "ADMINISTRATION": "ADMINISTRATION",
    "Catégories": "Categories",
    "Plats": "Dishes",
    "Commandes": "Orders",
    "Articles commandés": "Ordered items",
    "Réservations tables": "Table bookings",
    "Réservations événements": "Event bookings",
    "Messages contact": "Contact messages",
    "Déconnexion": "Logout",
    "Espace de gestion du restaurant": "Restaurant management space",

    "Actions": "Actions",
    "Export": "Export",
    "Search": "Search",
    "Save": "Save",
    "Cancel": "Cancel",
    "Delete": "Delete",
    "Edit": "Edit",
    "View": "View",
    "Yes": "Yes",
    "No": "No",
    "Show": "Show",
    "Page": "Page",
    "prev": "prev",
    "next": "next",
    "No data available in table": "No data available",
    "Details": "Details",

    "NOM DE LA CATÉGORIE": "CATEGORY NAME",
    "ORDRE D'AFFICHAGE": "DISPLAY ORDER",

    "PLAT": "DISH",
    "Plat": "Dish",
    "CATÉGORIE": "CATEGORY",
    "Catégorie": "Category",
    "PRIX": "PRICE",
    "Prix": "Price",
    "DISPONIBILITÉ": "AVAILABILITY",
    "Disponibilité": "Availability",
    "Disponible": "Available",
    "Indisponible": "Unavailable",

    "N°": "No.",
    "CLIENT": "CUSTOMER",
    "Client": "Customer",
    "RÉCEPTION": "METHOD",
    "DESTINATION": "DESTINATION",
    "TOTAL": "TOTAL",
    "PAIEMENT": "PAYMENT",
    "ÉTAT": "STATUS",
    "CRÉNEAU": "TIME SLOT",

    "COMMANDE": "ORDER",
    "Commande": "Order",
    "QUANTITÉ": "QUANTITY",
    "Quantité": "Quantity",
    "PRIX UNITAIRE": "UNIT PRICE",
    "Prix unitaire": "Unit price",

    "DATE": "DATE",
    "Date": "Date",
    "HEURE": "TIME",
    "Heure": "Time",
    "CONVIVES": "GUESTS",
    "Convives": "Guests",
    "STATUT": "STATUS",
    "Statut": "Status",
    "ÉVÉNEMENT": "EVENT",
    "Événement": "Event",

    "CONTACT": "CONTACT",
    "SUJET": "SUBJECT",
    "Sujet": "Subject",
    "MESSAGE": "MESSAGE",
    "Message": "Message",
    "LECTURE": "READ STATUS",
    "Lecture": "Read status",
    "REÇU LE": "RECEIVED ON",
    "Reçu le": "Received on",

    "En attente": "Pending",
    "Nouvelle": "New",
    "Confirmée": "Confirmed",
    "confirmée": "confirmed",
    "En préparation": "In progress",
    "Prête": "Ready",
    "Livrée": "Delivered",
    "Annulée": "Cancelled",
    "annulée": "cancelled",
    "Payé": "Paid",
    "Échoué": "Failed",
    "Problème signalé": "Issue reported",
    "problème signalé": "issue reported",
    "Livraison": "Delivery",
    "À emporter": "Pickup",
    "Retrait au restaurant": "Pickup at restaurant",
    "Carte": "Card",
    "Sur place": "On site",
    "Nouveau": "New",
    "Lu": "Read",
    "Non lu": "Unread",
    "Répondu": "Replied",
    "Archivé": "Archived",
    "Anniversaire": "Birthday",
    "Mariage": "Wedding",
    "Entreprise": "Corporate",
    "Événement privé": "Private event",

    "✅ Confirmer (email + SMS)": "✅ Confirm (email + SMS)",
    "🚨 Signaler un problème": "🚨 Report an issue",
    "✅ Accusé de réception (email)": "✅ Acknowledge (email)",
    "✉️ Répondre": "✉️ Reply",

    "Bienvenue dans votre espace": "Welcome to your space",
    "Pilotez les commandes, les réservations et les messages depuis un espace pensé pour votre équipe. Les informations importantes sont accessibles en un seul regard.":
      "Manage orders, bookings and messages from a space built for your team. Everything important, at a glance.",
    "Voir les commandes": "View orders",
    "Toutes les réservations": "All bookings",
    "Commandes enregistrées": "Orders recorded",
    "Réservations de tables": "Table bookings",
    "Événements privés": "Private events",
    "Messages non lus": "Unread messages",
    "Calendrier des réservations": "Bookings calendar",
    "Cliquez sur une journée pour afficher ses réservations de tables et ses événements.":
      "Click a day to see its table bookings and events.",
    "Tables": "Tables",
    "Événements": "Events",
    "Vert = Réservations de tables": "Green = Table bookings",
    "Orange = Événements": "Orange = Events",
    "Cliquez sur un jour contenant un badge vert.": "Click a day with a green badge.",
    "Accès rapides": "Quick access",
    "Les actions les plus utilisées par votre équipe.": "The actions your team uses most.",
    "Gérer les commandes": "Manage orders",
    "Modifier les plats": "Edit dishes",
    "Voir les réservations": "View bookings",
    "Lire les messages": "Read messages",
    "Aujourd'hui": "Today",
    "Une belle journée commence avec une équipe bien organisée.":
      "A great day starts with a well-organized team.",
    "Réservations de la journée": "Bookings for the day",
    "Aucune réservation pour cette journée.": "No bookings for this day.",
    "Impossible de charger les réservations.": "Unable to load bookings.",
    "Impossible de charger cette journée.": "Unable to load this day.",
    "Chargement du calendrier…": "Loading calendar…",
    "Calendrier indisponible": "Calendar unavailable",
    "Impossible de charger le calendrier.": "Unable to load calendar.",
    "Voir la fiche complète →": "View full record →",
    "Réservations de tables ": "Table bookings ",
    "Événements privés ": "Private events ",
    "convive(s)": "guest(s)",
    "participant(s)": "attendee(s)",
    "table(s)": "table(s)",
    "événement(s)": "event(s)",
    "réservation(s)": "booking(s)",
    "Bonjour,": "Hello,",
    "Chargement des réservations…": "Loading bookings…",
    "Mois précédent": "Previous month",
    "Mois suivant": "Next month",
    "Fermer": "Close",
    "Aucune réservation": "No booking",
    "Nom de la catégorie": "Category name",
    "Ordre d'affichage": "Display order",
    "Position": "Position",
    "Créer": "Create",
    "Ajouter": "Add",
    "Mettre à jour": "Update",
    "Retour": "Back",
    "nouvelle": "new",
    "en attente": "pending",
    "en préparation": "in progress",
    "prête": "ready",
    "livrée": "delivered",
    "payé": "paid",
    "échoué": "failed",
    "répondu": "replied",
    "archivé": "archived",
    "événement": "event",
    "réservation": "booking"
  };

  var MC_MONTHS_EN = ["January","February","March","April","May","June",
    "July","August","September","October","November","December"];
  var MC_WEEKDAYS_EN = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];

  /* Traduction bidirectionnelle : le HTML SQLAdmin peut être mixte. */
  var MC_DICT_FR = {
    "Categories":"Catégories","Dishes":"Plats","Dish":"Plat","Orders":"Commandes","Order":"Commande",
    "Ordered items":"Articles commandés","Table bookings":"Réservations tables","Event bookings":"Réservations événements",
    "Contact messages":"Messages contact","Logout":"Déconnexion","Restaurant management space":"Espace de gestion du restaurant",
    "Hello,":"Bonjour,","Welcome to your space":"Bienvenue dans votre espace",
    "Manage orders, bookings and messages from a space built for your team. Everything important, at a glance.":"Pilotez les commandes, les réservations et les messages depuis un espace pensé pour votre équipe. Les informations importantes sont accessibles en un seul regard.",
    "View orders":"Voir les commandes","All bookings":"Toutes les réservations","Orders recorded":"Commandes enregistrées",
    "Private events":"Événements privés","Unread messages":"Messages non lus","Bookings calendar":"Calendrier des réservations",
    "Click a day to see its table bookings and events.":"Cliquez sur une journée pour afficher ses réservations de tables et ses événements.",
    "Events":"Événements","Quick access":"Accès rapides","The actions your team uses most.":"Les actions les plus utilisées par votre équipe.",
    "Manage orders":"Gérer les commandes","Edit dishes":"Modifier les plats","View bookings":"Voir les réservations","Read messages":"Lire les messages",
    "Today":"Aujourd'hui","A great day starts with a well-organized team.":"Une belle journée commence avec une équipe bien organisée.",
    "Bookings for the day":"Réservations de la journée","No bookings for this day.":"Aucune réservation pour cette journée.",
    "Unable to load bookings.":"Impossible de charger les réservations.","Unable to load this day.":"Impossible de charger cette journée.",
    "Loading calendar…":"Chargement du calendrier…","Loading bookings…":"Chargement des réservations…","Calendar unavailable":"Calendrier indisponible",
    "Unable to load calendar.":"Impossible de charger le calendrier.","View full record →":"Voir la fiche complète →",
    "Previous month":"Mois précédent","Next month":"Mois suivant","Close":"Fermer","Save":"Enregistrer",
    "Cancel":"Annuler","Delete":"Supprimer","Edit":"Modifier","View":"Voir","Create":"Créer","Update":"Mettre à jour","Add":"Ajouter","Back":"Retour",
    "Yes":"Oui","No":"Non","Show":"Afficher","Page":"Page","Details":"Détails","Category":"Catégorie","Category name":"Nom de la catégorie",
    "Display order":"Ordre d'affichage","Price":"Prix","Availability":"Disponibilité","Available":"Disponible","Unavailable":"Indisponible",
    "Customer":"Client","Method":"Réception","Payment":"Paiement","Status":"Statut","Time slot":"Créneau","Quantity":"Quantité","Unit price":"Prix unitaire",
    "Time":"Heure","Guests":"Convives","Event":"Événement","Subject":"Sujet","Read status":"Lecture","Received on":"Reçu le",
    "Pending":"En attente","New":"Nouveau","Confirmed":"Confirmée","confirmed":"confirmée","In progress":"En préparation","Ready":"Prête",
    "Delivered":"Livrée","Cancelled":"Annulée","cancelled":"annulée","Paid":"Payé","Failed":"Échoué","Issue reported":"Problème signalé",
    "issue reported":"problème signalé","Delivery":"Livraison","Pickup":"À emporter","Pickup at restaurant":"Retrait au restaurant",
    "Card":"Carte","On site":"Sur place","Read":"Lu","Unread":"Non lu","Replied":"Répondu","Archived":"Archivé",
    "Birthday":"Anniversaire","Wedding":"Mariage","Corporate":"Entreprise","Private event":"Événement privé",
    "guest(s)":"convive(s)","attendee(s)":"participant(s)","event(s)":"événement(s)","booking(s)":"réservation(s)"
  };
  var MC_MONTHS_FR=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"];
  var mcOriginals = new WeakMap();
  function mcCurrentLang(){return localStorage.getItem('mc_admin_lang')||'fr';}
  function mcApplyDictionary(value, dictionary) {
    var result = value;
    var keys = Object.keys(dictionary).sort(function (a, b) {
      return b.length - a.length;
    });
    keys.forEach(function (key) {
      if (!key || dictionary[key] === key) return;
      var escaped = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      // (^|[^\p{L}]) et ($|[^\p{L}]) : n'accepte le remplacement que si le mot
      // est entouré de limites (début/fin de chaîne ou caractère non-lettre),
      // pour ne jamais toucher un mot plus long qui contiendrait la clé
      // (ex: "No" ne doit pas matcher dans "Nouvelle").
      var pattern = new RegExp("(^|[^\\p{L}])(" + escaped + ")($|[^\\p{L}])", "gu");
      result = result.replace(pattern, function (match, before, matched, after) {
        return before + dictionary[key] + after;
      });
    });
    return result;
  }
  function mcTranslateText(text){
    var trimmed=text.trim();if(!trimmed)return text;
    var translated=trimmed;
    if(mcCurrentLang()==='en'){
      var showingFr=translated.match(/^Affichage de (\d+) à (\d+) sur (\d+) éléments?$/i);
      if(showingFr)translated='Showing '+showingFr[1]+' to '+showingFr[2]+' of '+showingFr[3]+' items';
      translated=mcApplyDictionary(translated,MC_DICT).replace(/^Commande #(\d+)$/i,'Order #$1');
    }else{
      var showingEn=translated.match(/^Showing (\d+) to (\d+) of (\d+) items?$/i);
      if(showingEn)translated='Affichage de '+showingEn[1]+' à '+showingEn[2]+' sur '+showingEn[3]+' éléments';
      translated=mcApplyDictionary(translated,MC_DICT_FR).replace(/^Order #(\d+)$/i,'Commande #$1');
      translated=translated.replace(/^prev$/i,'précédent').replace(/^next$/i,'suivant');
    }
    return text.replace(trimmed,translated);
  }
  function mcWalk(node){
    if (node.nodeType === Node.TEXT_NODE) {
      if (!mcOriginals.has(node)) mcOriginals.set(node, node.nodeValue);
      var original = mcOriginals.get(node);
      node.nodeValue = mcTranslateText(original);
      return;
    }
    if (node.nodeType !== Node.ELEMENT_NODE) return;
    var tag = node.tagName;
    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'TEXTAREA') return;

    if (node.hasAttribute && node.hasAttribute('placeholder')) mcApplyAttr(node,'placeholder');
    if (node.hasAttribute && node.hasAttribute('title')) mcApplyAttr(node,'title');
    if (node.hasAttribute && node.hasAttribute('aria-label')) mcApplyAttr(node,'aria-label');

    for (var i = 0; i < node.childNodes.length; i++) {
      mcWalk(node.childNodes[i]);
    }
  }

  function mcApplyAttr(el, attr){
    if (!mcOriginals.has(el)) mcOriginals.set(el, {});
    var store = mcOriginals.get(el);
    if (store[attr] === undefined) store[attr] = el.getAttribute(attr);
    el.setAttribute(attr, mcTranslateText(store[attr]));
  }

  function mcApplyLanguage(root){
    mcWalk(root || document.body);
  }

  function mcFormatMonthLabel(date){
    if (mcCurrentLang() === 'en') {
      return MC_MONTHS_EN[date.getMonth()] + ' ' + date.getFullYear();
    }
    return MC_MONTHS_FR[date.getMonth()] + ' ' + date.getFullYear();
  }

  function mcFormatDayTitle(dateKey){
    var parsed = new Date(dateKey + 'T12:00:00');
    if (mcCurrentLang() === 'en') {
      return parsed.toLocaleDateString('en-US', {
        weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
      });
    }
    return parsed.toLocaleDateString('fr-FR', {
      weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
    });
  }

  function mcTranslateWeekdays(){
    document.querySelectorAll('.mc-calendar-weekday').forEach(function(el, idx){
      if (!mcOriginals.has(el)) mcOriginals.set(el, {text: el.textContent});
      var store = mcOriginals.get(el);
      el.textContent = mcCurrentLang() === 'en' ? MC_WEEKDAYS_EN[idx] : store.text;
    });
  }


  /* =========================================================
     SIDEBAR CUSTOM — reconstruit uniquement l'affichage,
     en conservant les vraies URLs SQLAdmin existantes.
  ========================================================= */
  function mcBuildCustomSidebar(){
    var nav = document.querySelector('.navbar-vertical');
    if(!nav || nav.dataset.mcSidebarBuilt === '1') return;

    var existingLinks = Array.prototype.slice.call(
      nav.querySelectorAll('a.nav-link, .navbar-nav a[href]')
    );

    function findHref(tokens, fallback){
      for(var i=0;i<existingLinks.length;i++){
        var a=existingLinks[i];
        var hay=((a.textContent||'')+' '+(a.getAttribute('href')||'')).toLowerCase();
        for(var j=0;j<tokens.length;j++){
          if(hay.indexOf(tokens[j])!==-1) return a.getAttribute('href')||fallback;
        }
      }
      return fallback;
    }

    var items = [
      {label:'Tableau de bord', href:'/admin', tokens:['tableau','dashboard'], icon:'⌂'},
      {label:'Catégories', href:findHref(['category','catégorie','categories'],'/admin/category/list'), tokens:['category','catégorie','categories'], icon:'☷'},
      {label:'Plats', href:findHref(['dish','plat','dishes'],'/admin/dish/list'), tokens:['dish','plat','dishes'], icon:'♨'},
      {label:'Commandes', href:findHref(['order','commande','orders'],'/admin/order/list'), tokens:['order','commande','orders'], icon:'🛍'},
      {label:'Articles commandés', href:findHref(['order-item','ordered item','articles commandés'],'/admin/order-item/list'), tokens:['order-item','ordered item','articles commandés'], icon:'▤'},
      {label:'Réservations', href:findHref(['table-reservation','réservations tables','table bookings'],'/admin/table-reservation/list'), icon:'▣'},
      {label:'Événements', href:findHref(['event-reservation','réservations événements','event bookings'],'/admin/event-reservation/list'), icon:'☆'},
      {label:'Messages', href:findHref(['contact-message','messages contact','contact messages'],'/admin/contact-message/list'), icon:'✉'}
    ];

    /* Réutilise les URL SQLAdmin existantes quand elles sont disponibles. */
    items.forEach(function(item){
      if(item.tokens){
        var found=findHref(item.tokens,item.href);
        if(found) item.href=found;
      }
    });

    var path=location.pathname.replace(/\/+$/,'')||'/';
    function isActive(item){
      if(item.label==='Tableau de bord') return path==='/admin';
      if(!item.href || item.href==='#') return false;
      var clean=item.href.split('?')[0].replace(/\/+$/,'');
      return clean && path.indexOf(clean.replace(/\/list$/,''))===0;
    }

    var menuHtml=items.map(function(item){
      return '<a class="mc-sidebar-link'+(isActive(item)?' mc-active':'')+'" href="'+item.href+'">'+
        '<span class="mc-sidebar-icon">'+item.icon+'</span>'+
        '<span>'+item.label+'</span>'+
      '</a>';
    }).join('');

    nav.innerHTML=
      '<div class="mc-sidebar-custom">'+
        '<div class="mc-sidebar-head">'+
          '<img class="mc-sidebar-logo" src="/images/logoMissChawarma.png" alt="Miss Chawarma">'+
          '<div class="mc-sidebar-name">Miss Chawarma</div>'+
          '<div class="mc-sidebar-role">ADMINISTRATION</div>'+
        '</div>'+
        '<nav class="mc-sidebar-menu">'+menuHtml+'</nav>'+
        '<div class="mc-sidebar-leaves"></div>'+
        '<div class="mc-sidebar-account">'+
          '<span class="mc-sidebar-avatar">MC</span>'+
          '<span class="mc-sidebar-account-name">Miss Chawarma</span>'+
          '<span class="mc-sidebar-chevron">⌄</span>'+
        '</div>'+
      '</div>';

    nav.dataset.mcSidebarBuilt='1';
  }

  /* =========================================================
     TOPBAR
  ========================================================= */

  function createTopbar(){
    if(document.querySelector('.mc-topbar'))return;
    var path = location.pathname.replace(/\/+$/,'');
    if (path === '/admin/login') return; 
    var oldLogout=document.querySelector('.navbar-vertical a[href*="logout"]');
    var logoutHref=oldLogout?oldLogout.getAttribute('href'):'/admin/logout';
    var bar=document.createElement('header');bar.className='mc-topbar';
    bar.innerHTML='<button type="button" class="mc-nav-toggle" id="mcNavToggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>'+
    '<div class="mc-topbar-brand"><div class="mc-topbar-orb"><img src="/images/logoMissChawarma.png" alt="Logo"></div><div><div class="mc-topbar-title">Maison Miss Chawarma</div><div class="mc-topbar-subtitle">Espace de gestion du restaurant</div></div></div>'+ 
    '<div class="mc-topbar-actions"><a class="mc-topbar-link" href="/admin/order/list">🛍 Commandes</a><div class="mc-lang-switch"><button type="button" data-lang="fr">FR</button><button type="button" data-lang="en">EN</button></div><a class="mc-topbar-logout" href="'+logoutHref+'">↗<span class="mc-logout-text"> Déconnexion</span></a></div>';
    document.body.insertBefore(bar,document.body.firstChild);
    if(!document.getElementById('mcNavBackdrop')){
      var backdrop=document.createElement('div');
      backdrop.className='mc-nav-backdrop';backdrop.id='mcNavBackdrop';
      document.body.appendChild(backdrop);
    }
    var current=mcCurrentLang();
    bar.querySelectorAll('[data-lang]').forEach(function(b){
      b.classList.toggle('mc-active',b.dataset.lang===current);
      b.addEventListener('click',function(){
        if (b.dataset.lang === mcCurrentLang()) return;
        localStorage.setItem('mc_admin_lang', b.dataset.lang);
        location.reload();
      });
    });
    mcApplyLanguage(bar);
  }

  /* =========================================================
     MENU MOBILE — ouverture/fermeture du tiroir latéral
  ========================================================= */
  function initMobileNav(){
    var toggle=document.getElementById('mcNavToggle');
    var backdrop=document.getElementById('mcNavBackdrop');
    var nav=document.querySelector('.navbar-vertical');
    if(!toggle||!nav||toggle.dataset.mcBound)return;
    toggle.dataset.mcBound='1';

    function isOpen(){return document.documentElement.classList.contains('mc-nav-open');}
    function closeNav(){
      document.documentElement.classList.remove('mc-nav-open');
      toggle.setAttribute('aria-expanded','false');
    }
    function openNav(){
      document.documentElement.classList.add('mc-nav-open');
      toggle.setAttribute('aria-expanded','true');
    }
    toggle.addEventListener('click',function(e){
      e.stopPropagation();
      isOpen()?closeNav():openNav();
    });
    if(backdrop)backdrop.addEventListener('click',closeNav);
    nav.addEventListener('click',function(e){
      if(e.target.closest('a.nav-link')&&window.innerWidth<=991.98)closeNav();
    });
    document.addEventListener('keydown',function(e){if(e.key==='Escape')closeNav();});
    window.addEventListener('resize',function(){if(window.innerWidth>991.98)closeNav();});
  }

  function dashboardMarkup(){
    return '<main class="mc-dashboard"><section class="mc-dashboard-hero"><div class="mc-hero-content"><div class="mc-eyebrow">Bienvenue dans votre espace</div><h1>Bonjour, <span>Miss Chawarma</span></h1><p class="mc-hero-copy">Pilotez les commandes, les réservations et les messages depuis un espace pensé pour votre équipe. Les informations importantes sont accessibles en un seul regard.</p><div class="mc-hero-actions"><a class="mc-hero-button" href="/admin/order/list">🛍 Voir les commandes</a><a class="mc-hero-button mc-secondary" href="/admin/table-reservation/list">🍽 Toutes les réservations</a></div></div></section>'+
    '<section class="mc-stats-grid"><article class="mc-stat-card"><div class="mc-stat-icon">🛍</div><div class="mc-stat-value" data-stat="orders">—</div><div class="mc-stat-label">Commandes enregistrées</div></article><article class="mc-stat-card"><div class="mc-stat-icon">🍽</div><div class="mc-stat-value" data-stat="tables">—</div><div class="mc-stat-label">Réservations de tables</div></article><article class="mc-stat-card"><div class="mc-stat-icon">🥂</div><div class="mc-stat-value" data-stat="events">—</div><div class="mc-stat-label">Événements privés</div></article><article class="mc-stat-card"><div class="mc-stat-icon">✉</div><div class="mc-stat-value" data-stat="messages">—</div><div class="mc-stat-label">Messages non lus</div></article></section>'+
    '<section class="mc-calendar-panel"><div class="mc-calendar-header"><div><div class="mc-calendar-title">Calendrier des réservations</div><div class="mc-calendar-subtitle">Cliquez sur une journée pour afficher ses réservations de tables et ses événements.</div><div class="mc-calendar-legend"><span class="mc-calendar-legend-item mc-table"><span class="mc-calendar-legend-dot"></span>Tables</span><span class="mc-calendar-legend-item mc-event"><span class="mc-calendar-legend-dot"></span>Événements</span></div></div><div class="mc-calendar-controls"><button class="mc-calendar-nav" id="mc-calendar-prev" type="button" aria-label="Mois précédent">‹</button><div class="mc-calendar-month" id="mc-calendar-month"></div><button class="mc-calendar-nav" id="mc-calendar-next" type="button" aria-label="Mois suivant">›</button></div></div><div class="mc-calendar-weekdays"><div class="mc-calendar-weekday">Lun</div><div class="mc-calendar-weekday">Mar</div><div class="mc-calendar-weekday">Mer</div><div class="mc-calendar-weekday">Jeu</div><div class="mc-calendar-weekday">Ven</div><div class="mc-calendar-weekday">Sam</div><div class="mc-calendar-weekday">Dim</div></div><div class="mc-calendar-grid" id="mc-calendar-grid"><div class="mc-calendar-loading">Chargement du calendrier…</div></div><div class="mc-calendar-footer"><span>Cliquez sur un jour contenant un badge vert.</span><span class="mc-calendar-total">Tables : <strong id="mc-calendar-table-total">0</strong>&nbsp;&nbsp;·&nbsp;&nbsp;Événements : <strong id="mc-calendar-event-total">0</strong></span></div></section>'+
    '<section class="mc-dashboard-bottom"><div class="mc-panel"><div class="mc-panel-title">Accès rapides</div><div class="mc-panel-copy">Les actions les plus utilisées par votre équipe.</div><div class="mc-quick-grid"><a class="mc-quick-link" href="/admin/order/list"><span>🛍</span><span>Gérer les commandes</span></a><a class="mc-quick-link" href="/admin/dish/list"><span>🍴</span><span>Modifier les plats</span></a><a class="mc-quick-link" href="/admin/table-reservation/list"><span>🪑</span><span>Voir les réservations</span></a><a class="mc-quick-link" href="/admin/contact-message/list"><span>✉</span><span>Lire les messages</span></a></div></div><div class="mc-panel"><div class="mc-panel-title">Aujourd’hui</div><div class="mc-panel-copy">Une belle journée commence avec une équipe bien organisée.</div><div class="mc-clock" id="mc-dashboard-clock">--:--</div><div class="mc-date" id="mc-dashboard-date"></div></div></section>'+
    '<div class="mc-day-modal" id="mc-day-modal" aria-hidden="true"><div class="mc-day-dialog" role="dialog" aria-modal="true"><div class="mc-day-dialog-header"><div><div class="mc-day-dialog-eyebrow">Réservations de la journée</div><div class="mc-day-dialog-title" id="mc-day-dialog-title"></div></div><button class="mc-day-close" id="mc-day-close" type="button" aria-label="Fermer">×</button></div><div class="mc-day-dialog-body" id="mc-day-dialog-body"></div></div></div></main>';
  }

  var mcCalendarCursor = new Date();
  mcCalendarCursor.setDate(1);

  function mcPad(value) {
      return String(value).padStart(2, "0");
  }

  function mcDateKey(year, month, day) {
      return year + "-" + mcPad(month + 1) + "-" + mcPad(day);
  }

  function mcEscape(value) {
      var div = document.createElement("div");
      div.textContent = value == null ? "" : String(value);
      return div.innerHTML;
  }

  function mcOpenDayModal(dateKey) {
      var modal = document.getElementById("mc-day-modal");
      var title = document.getElementById("mc-day-dialog-title");
      var body = document.getElementById("mc-day-dialog-body");
      if (!modal || !title || !body) return;

      title.dataset.mcDateKey = dateKey;
      title.textContent = mcFormatDayTitle(dateKey);

      body.innerHTML = '<div class="mc-day-empty">Chargement des réservations…</div>';
      modal.classList.add("mc-open");
      modal.setAttribute("aria-hidden", "false");
      document.body.dataset.mcPreviousOverflow = document.body.style.overflow || "";
      document.body.style.overflow = "hidden";
      mcApplyLanguage(body);

      fetch("/admin-calendar/day?date=" + encodeURIComponent(dateKey), {
          credentials: "same-origin"
      })
      .then(function (response) {
          if (!response.ok) throw new Error("Impossible de charger cette journée.");
          return response.json();
      })
      .then(function (data) {
          var tables = data.tables || [];
          var events = data.events || [];

          if (tables.length === 0 && events.length === 0) {
              body.innerHTML =
                  '<div class="mc-day-empty">Aucune réservation pour cette journée.</div>';
              mcApplyLanguage(body);
              return;
          }

          function tableCard(reservation) {
              var fullName =
                  (reservation.first_name + " " + reservation.last_name).trim()
                  || "Client";
              var status = (reservation.status || "nouvelle").replace(/_/g, " ");
              var note = reservation.note
                  ? '<span>📝 ' + mcEscape(reservation.note) + '</span>'
                  : "";

              return (
                  '<article class="mc-reservation-card mc-table-card">' +
                      '<div class="mc-reservation-time">' +
                          mcEscape(reservation.time || "—") +
                      '</div>' +
                      '<div>' +
                          '<div class="mc-reservation-name">🍽 ' +
                              mcEscape(fullName) +
                          '</div>' +
                          '<div class="mc-reservation-meta">' +
                              '<span>👥 ' + mcEscape(reservation.guests) +
                                  ' convive(s)</span>' +
                              '<span>☎ ' + mcEscape(reservation.phone || "—") +
                                  '</span>' +
                              note +
                          '</div>' +
                          '<a class="mc-reservation-details" href="' +
                              mcEscape(reservation.details_url) +
                              '">Voir la fiche complète →</a>' +
                      '</div>' +
                      '<span class="mc-reservation-status mc-table-status">' +
                          mcEscape(status) +
                      '</span>' +
                  '</article>'
              );
          }

          function eventCard(reservation) {
              var fullName =
                  (reservation.first_name + " " + reservation.last_name).trim()
                  || "Client";
              var status = (reservation.status || "nouvelle").replace(/_/g, " ");
              var note = reservation.note
                  ? '<span>📝 ' + mcEscape(reservation.note) + '</span>'
                  : "";

              return (
                  '<article class="mc-reservation-card mc-event-card">' +
                      '<div class="mc-reservation-time">' +
                          mcEscape(reservation.time || "—") +
                      '</div>' +
                      '<div>' +
                          '<div class="mc-reservation-name">🥂 ' +
                              mcEscape(reservation.event_type || "Événement") +
                              ' — ' + mcEscape(fullName) +
                          '</div>' +
                          '<div class="mc-reservation-meta">' +
                              '<span>👥 ' + mcEscape(reservation.guests) +
                                  ' participant(s)</span>' +
                              '<span>☎ ' + mcEscape(reservation.phone || "—") +
                                  '</span>' +
                              note +
                          '</div>' +
                          '<a class="mc-reservation-details" href="' +
                              mcEscape(reservation.details_url) +
                              '">Voir la fiche complète →</a>' +
                      '</div>' +
                      '<span class="mc-reservation-status mc-event-status">' +
                          mcEscape(status) +
                      '</span>' +
                  '</article>'
              );
          }

          var html =
              '<div class="mc-day-summary">' +
                  '<span class="mc-day-summary-badge mc-table">🍽 ' +
                      tables.length + ' table(s)</span>' +
                  '<span class="mc-day-summary-badge mc-event">🥂 ' +
                      events.length + ' événement(s)</span>' +
              '</div>';

          if (tables.length > 0) {
              html +=
                  '<section class="mc-day-section mc-table-section">' +
                      '<div class="mc-day-section-title">Réservations de tables ' +
                          '<span>' + tables.length + ' réservation(s)</span></div>' +
                      '<div class="mc-reservation-list">' +
                          tables.map(tableCard).join("") +
                      '</div>' +
                  '</section>';
          }

          if (events.length > 0) {
              html +=
                  '<section class="mc-day-section mc-event-section">' +
                      '<div class="mc-day-section-title">Événements privés ' +
                          '<span>' + events.length + ' événement(s)</span></div>' +
                      '<div class="mc-reservation-list">' +
                          events.map(eventCard).join("") +
                      '</div>' +
                  '</section>';
          }

          body.innerHTML = html;
          mcApplyLanguage(body);
      })
      .catch(function () {
          body.innerHTML =
              '<div class="mc-day-empty">Impossible de charger les réservations.</div>';
          mcApplyLanguage(body);
      });
  }

  function mcCloseDayModal() {
      var modal = document.getElementById("mc-day-modal");
      if (!modal) return;
      modal.classList.remove("mc-open");
      modal.setAttribute("aria-hidden", "true");
      document.body.style.overflow = document.body.dataset.mcPreviousOverflow || "";
      delete document.body.dataset.mcPreviousOverflow;
  }

  function mcRenderCalendar() {
      var monthLabel = document.getElementById("mc-calendar-month");
      var grid = document.getElementById("mc-calendar-grid");
      var tableTotal = document.getElementById("mc-calendar-table-total");
      var eventTotal = document.getElementById("mc-calendar-event-total");
      if (!monthLabel || !grid || !tableTotal || !eventTotal) return;

      var year = mcCalendarCursor.getFullYear();
      var month = mcCalendarCursor.getMonth();

      monthLabel.textContent = mcFormatMonthLabel(mcCalendarCursor);
      mcTranslateWeekdays();

      grid.innerHTML =
          '<div class="mc-calendar-loading">Chargement du calendrier…</div>';
      mcApplyLanguage(grid);

      fetch("/admin-calendar?year=" + year + "&month=" + (month + 1), {
          credentials: "same-origin"
      })
      .then(function (response) {
          if (!response.ok) throw new Error("Calendrier indisponible");
          return response.json();
      })
      .then(function (data) {
          var firstDay = new Date(year, month, 1);
          var lastDay = new Date(year, month + 1, 0);
          var mondayIndex = (firstDay.getDay() + 6) % 7;
          var today = new Date();
          var html = "";

          for (var empty = 0; empty < mondayIndex; empty++) {
              html += '<div class="mc-calendar-day mc-empty"></div>';
          }

          for (var day = 1; day <= lastDay.getDate(); day++) {
              var key = mcDateKey(year, month, day);
              var dayData = data.days[key] || {tables: 0, events: 0, total: 0};
              var tableCount = Number(dayData.tables || 0);
              var eventCount = Number(dayData.events || 0);
              var count = tableCount + eventCount;
              var isToday =
                  today.getFullYear() === year &&
                  today.getMonth() === month &&
                  today.getDate() === day;

              var classes = "mc-calendar-day";
              if (isToday) classes += " mc-today";
              if (count > 0) classes += " mc-has-reservations";
              if (tableCount > 0 && eventCount > 0) classes += " mc-mixed";
              else if (tableCount > 0) classes += " mc-table-only";
              else if (eventCount > 0) classes += " mc-event-only";

              html +=
                  '<button type="button" class="' + classes + '" data-date="' +
                  key + '" ' + (count === 0 ? 'aria-label="Aucune réservation"' : "") + '>' +
                      '<span class="mc-calendar-number">' + day + '</span>' +
                      (count > 0
                          ? '<span class="mc-calendar-badges">' +
                                (tableCount > 0
                                    ? '<span class="mc-calendar-type-badge mc-table" aria-label="' +
                                      tableCount + ' réservation(s) de table">' +
                                        '<span class="mc-badge-icon">🍽</span>' +
                                        '<span class="mc-badge-count">' + tableCount + '</span>' +
                                      '</span>'
                                    : '') +
                                (eventCount > 0
                                    ? '<span class="mc-calendar-type-badge mc-event" aria-label="' +
                                      eventCount + ' événement(s)">' +
                                        '<span class="mc-badge-icon">🥂</span>' +
                                        '<span class="mc-badge-count">' + eventCount + '</span>' +
                                      '</span>'
                                    : '') +
                            '</span>'
                          : "") +
                  '</button>';
          }

          grid.innerHTML = html;
          tableTotal.textContent = (data.totals && data.totals.tables) || 0;
          eventTotal.textContent = (data.totals && data.totals.events) || 0;
          mcApplyLanguage(document.querySelector('.mc-calendar-footer'));

          grid.querySelectorAll("[data-date]").forEach(function (button) {
              button.addEventListener("click", function () {
                  mcOpenDayModal(button.dataset.date);
              });
          });
      })
      .catch(function () {
          grid.innerHTML =
              '<div class="mc-calendar-error">Impossible de charger le calendrier.</div>';
          tableTotal.textContent = "0";
          eventTotal.textContent = "0";
          mcApplyLanguage(grid);
      });
  }

  function mcInitCalendar() {
      var prev = document.getElementById("mc-calendar-prev");
      var next = document.getElementById("mc-calendar-next");
      var close = document.getElementById("mc-day-close");
      var modal = document.getElementById("mc-day-modal");

      if (prev) {
          prev.addEventListener("click", function () {
              mcCalendarCursor.setMonth(mcCalendarCursor.getMonth() - 1);
              mcRenderCalendar();
          });
      }

      if (next) {
          next.addEventListener("click", function () {
              mcCalendarCursor.setMonth(mcCalendarCursor.getMonth() + 1);
              mcRenderCalendar();
          });
      }

      if (close) close.addEventListener("click", mcCloseDayModal);

      if (modal) {
          modal.addEventListener("click", function (event) {
              if (event.target === modal) mcCloseDayModal();
          });
      }

      document.addEventListener("keydown", function (event) {
          if (event.key === "Escape") mcCloseDayModal();
      });

      mcRenderCalendar();

      window.addEventListener("pageshow", function () {
          var activeModal = document.getElementById("mc-day-modal");
          if (!activeModal || !activeModal.classList.contains("mc-open")) {
              document.body.style.overflow =
                  document.body.dataset.mcPreviousOverflow || "";
              delete document.body.dataset.mcPreviousOverflow;
          }
      });
  }

  function renderDashboard(){
    var path=location.pathname.replace(/\/+$/,'');
    if(path!='/admin')return;
    var target=document.querySelector('.page-body')||document.querySelector('.page-wrapper');
    if(!target)return;
    target.innerHTML=dashboardMarkup();
    mcApplyLanguage(target);

    // Sort le modal de .mc-dashboard et le rattache à <body> :
    // sinon l'animation "mcPageIn" (transform) sur .mc-dashboard devient
    // le containing block du modal position:fixed, et sa position dépend
    // alors du scroll de la page au lieu de rester fixe par rapport à l'écran.
    var modalEl = document.getElementById('mc-day-modal');
    if (modalEl && modalEl.parentNode !== document.body) {
      document.body.appendChild(modalEl);
    }

    mcInitCalendar();

    fetch('/admin-dashboard-data',{credentials:'same-origin'})
      .then(function(r){if(!r.ok)throw new Error();return r.json()})
      .then(function(data){
        Object.keys(data).forEach(function(k){
          var el=document.querySelector('[data-stat="'+k+'"]');
          if(el)el.textContent=data[k];
        });
      })
      .catch(function(){
        document.querySelectorAll('[data-stat]').forEach(function(el){el.textContent='0'});
      });

    function clock(){
      var n=new Date(),
          c=document.getElementById('mc-dashboard-clock'),
          d=document.getElementById('mc-dashboard-date');
      var locale=mcCurrentLang()==='en'?'en-GB':'fr-FR';
      if(c)c.textContent=n.toLocaleTimeString(locale,{hour:'2-digit',minute:'2-digit'});
      if(d)d.textContent=n.toLocaleDateString(locale,{weekday:'long',day:'numeric',month:'long',year:'numeric'});
    }
    clock();
    setInterval(clock,30000);
  }



  /* =========================================================
     CARTES MOBILE POUR LES LISTES SQLADMIN
     - uniquement <= 575px
     - desktop/tablette inchangés
     - clic sur la carte = détails
     - les actions restent cliquables
  ========================================================= */
  function mcInitMobileTableCards(root){
    if (window.innerWidth > 575.98) {
      document.querySelectorAll('.mc-mobile-cards').forEach(function(el){
        el.remove();
      });
      document.querySelectorAll('.card.mc-mobile-card-mode').forEach(function(el){
        el.classList.remove('mc-mobile-card-mode');
      });
      document.querySelectorAll('.mc-dish-filters,.mc-dish-no-results').forEach(function(el){
        el.remove();
      });
      /* Repasse en desktop : réaffiche le bouton "Actions" natif s'il
         avait été masqué côté mobile. */
      document.querySelectorAll('[data-mc-actions-hidden="1"]').forEach(function(el){
        el.style.display = '';
        el.removeAttribute('data-mc-actions-hidden');
      });
      return;
    }
    if (!/^\/admin\/[^/]+\/list\/?$/.test(window.location.pathname)) return;

    var scope = root || document;
    var tables = scope.querySelectorAll
      ? scope.querySelectorAll('.card .table-responsive table')
      : [];

    /* La sélection multiple étant masquée sur mobile (voir CSS), le bouton
       natif "Actions" (qui n'agit que sur les lignes cochées) ne peut plus
       rien faire : on le cache pour ne pas laisser un bouton mort. */
    document.querySelectorAll('.card .card-body').forEach(function(body){
      Array.prototype.slice.call(body.querySelectorAll('button,a')).forEach(function(btn){
        var text = (btn.textContent || '').trim().toLowerCase();
        if (text === 'actions' || text === 'action') {
          var group = btn.closest('.dropdown') || btn.closest('.btn-group') || btn;
          group.style.display = 'none';
          group.setAttribute('data-mc-actions-hidden', '1');
        }
      });
    });

    tables.forEach(function(table){
      var card = table.closest('.card');
      if (!card) return;

      var responsive = table.closest('.table-responsive');
      if (!responsive) return;

      var oldCards = card.querySelector('.mc-mobile-cards');
      if (oldCards) oldCards.remove();

      var headers = Array.prototype.slice.call(
        table.querySelectorAll('thead th')
      ).map(function(th){
        return (th.textContent || '').replace(/\s+/g,' ').trim();
      });

      /* Colonne photo (ex: liste des Plats) : si elle existe, on l'affiche
         comme une vraie vignette en haut de chaque carte mobile plutôt que
         comme une ligne de détail parmi d'autres. */
      var photoColumnIndex = -1;
      headers.forEach(function(h, i){
        var n = (h || '').toLowerCase();
        if (photoColumnIndex === -1 && (n === 'photo' || n === 'image')) {
          photoColumnIndex = i;
        }
      });

      var rows = Array.prototype.slice.call(
        table.querySelectorAll('tbody tr')
      );

      if (!rows.length) return;

      var cardsWrap = document.createElement('div');
      cardsWrap.className = 'mc-mobile-cards';

      /* -----------------------------------------------------
         Selection bar
         It controls the ORIGINAL SQLAdmin checkboxes in the
         hidden table, so the native "Actions" dropdown works.
      ----------------------------------------------------- */
      var selectableOriginals = [];
      rows.forEach(function(row){
        var cb = row.querySelector('input[type="checkbox"]');
        if (cb && !cb.disabled) selectableOriginals.push(cb);
      });

      var selectBar = null;
      var selectAll = null;
      var selectedCount = null;

      if (selectableOriginals.length) {
        selectBar = document.createElement('div');
        selectBar.className = 'mc-mobile-selectbar';
        selectBar.innerHTML =
          '<label class="mc-mobile-selectbar-left">' +
            '<input type="checkbox" class="mc-mobile-select-all" aria-label="Tout sélectionner">' +
            '<span>Tout sélectionner</span>' +
          '</label>' +
          '<span class="mc-mobile-selected-count">0 sélectionné</span>';

        selectAll = selectBar.querySelector('.mc-mobile-select-all');
        selectedCount = selectBar.querySelector('.mc-mobile-selected-count');
        cardsWrap.appendChild(selectBar);
      }

      var mobileCheckboxes = [];

      function updateSelectionUI(){
        var checked = mobileCheckboxes.filter(function(info){
          return info.mobile.checked;
        }).length;

        if (selectedCount) {
          selectedCount.textContent =
            checked + (checked > 1 ? ' sélectionnés' : ' sélectionné');
        }

        if (selectAll) {
          selectAll.checked =
            mobileCheckboxes.length > 0 && checked === mobileCheckboxes.length;
          selectAll.indeterminate =
            checked > 0 && checked < mobileCheckboxes.length;
        }
      }

      function mcNormalizeStateText(value){
        return (value || '').toString().replace(/\s+/g,' ').trim().toLowerCase();
      }

      function mcStateColor(kind, value){
        var v = mcNormalizeStateText(value);
        if (kind === 'availability') {
          if (v.indexOf('indisponible') !== -1 || v.indexOf('unavailable') !== -1 || v === 'false' || v === 'non' || v === 'no') return 'red';
          if (v.indexOf('disponible') !== -1 || v.indexOf('available') !== -1 || v === 'true' || v === 'oui' || v === 'yes') return 'green';
          return 'yellow';
        }
        if (v.indexOf('annul') !== -1 || v.indexOf('cancel') !== -1 || v.indexOf('échou') !== -1 || v.indexOf('failed') !== -1 || v.indexOf('probl') !== -1 || v.indexOf('issue') !== -1 || v.indexOf('refus') !== -1 || v.indexOf('reject') !== -1) return 'red';
        if (v.indexOf('confirm') !== -1 || v.indexOf('livr') !== -1 || v.indexOf('delivered') !== -1 || v.indexOf('payé') !== -1 || v.indexOf('paid') !== -1 || v.indexOf('prête') !== -1 || v.indexOf('ready') !== -1 || v === 'lu' || v === 'read' || v.indexOf('répondu') !== -1 || v.indexOf('replied') !== -1) return 'green';
        if (v.indexOf('nouvel') !== -1 || v === 'new' || v.indexOf('attente') !== -1 || v.indexOf('pending') !== -1 || v.indexOf('préparation') !== -1 || v.indexOf('progress') !== -1) return 'yellow';
        return 'neutral';
      }

      rows.forEach(function(row, rowIndex){
        var cells = Array.prototype.slice.call(row.children);
        if (!cells.length) return;

        var originalCheckbox = row.querySelector('input[type="checkbox"]');
        var record = document.createElement('article');
        record.className = 'mc-mobile-record-card';

        var useful = [];
        var actionCell = null;
        var photoSrc = '';

        cells.forEach(function(cell, index){
          var label = headers[index] || '';
          var normalized = label.toLowerCase();
          var html = cell.innerHTML;
          var textValue = (cell.textContent || '').replace(/\s+/g,' ').trim();

          var isCheckbox = !!cell.querySelector('input[type="checkbox"]');
          var hasActions = !!cell.querySelector(
            'a[href*="/view"],a[href*="/edit"],a[href*="/delete"],[data-bs-target*="delete"],button'
          );
          var isActions =
            normalized.indexOf('action') !== -1 ||
            hasActions;

          if (isCheckbox) return;

          if (index === photoColumnIndex) {
            var imgEl = cell.querySelector('img');
            photoSrc = imgEl ? (imgEl.getAttribute('src') || '') : '';
            return;
          }

          if (isActions) {
            if (!actionCell && cell.querySelector('a,button')) {
              actionCell = cell;
            }
            return;
          }

          if (!textValue && !cell.querySelector('img,span,a')) return;

          useful.push({
            label: label || ('Info ' + (index + 1)),
            html: html,
            text: textValue
          });
        });

        var titleItem = useful[0] || {text:'Détails', html:'Détails', label:''};
        var subtitleItem = useful[1] || null;

        var stateKind = '';
        var stateValue = '';
        useful.forEach(function(item){
          var label = mcNormalizeStateText(item.label);
          if (!stateKind && (label.indexOf('disponibilité') !== -1 || label.indexOf('disponibilite') !== -1 || label.indexOf('availability') !== -1)) {
            stateKind = 'availability';
            stateValue = item.text;
          }
        });
        if (!stateKind) {
          useful.forEach(function(item){
            var label = mcNormalizeStateText(item.label);
            if (!stateKind && (label === 'statut' || label === 'status' || label === 'état' || label === 'etat')) {
              stateKind = 'status';
              stateValue = item.text;
            }
          });
        }
        var stateColor = stateKind ? mcStateColor(stateKind, stateValue) : '';
        if (stateKind) {
          record.dataset.mcStateKind = stateKind;
          record.dataset.mcStateValue = mcNormalizeStateText(stateValue);
          record.dataset.mcStateColor = stateColor;
        }

        /* Informations principales directement visibles dans les cartes mobiles. */
        var quickCategory = '';
        var quickPrice = '';
        useful.forEach(function(item){
          var label = mcNormalizeStateText(item.label);
          if (!quickCategory && (label === 'catégorie' || label === 'categorie' || label === 'category')) {
            quickCategory = item.text;
          }
          if (!quickPrice && (label === 'prix' || label === 'price')) {
            quickPrice = item.text;
          }
        });

        var summary = document.createElement('div');
        summary.className = 'mc-mobile-card-summary';

        var selectHtml = '';
        if (originalCheckbox && !originalCheckbox.disabled) {
          selectHtml =
            '<label class="mc-mobile-card-select-wrap" title="Sélectionner">' +
              '<input type="checkbox" class="mc-mobile-select" aria-label="Sélectionner cette ligne">' +
            '</label>';
        }

        /* Le statut (ex: Disponible/Indisponible) est représenté par un
           point coloré flottant en coin de carte plutôt que par un badge
           texte dans le bloc infos, pour rester compact. */

        var quickInfoHtml = '';
        if (quickCategory || quickPrice) {
          quickInfoHtml += '<div class="mc-mobile-card-quick">';
          if (quickCategory) {
            quickInfoHtml += '<span class="mc-mobile-card-category">' + mcEscape(quickCategory) + '</span>';
          }
          if (quickPrice) {
            quickInfoHtml += '<div class="mc-mobile-card-price">' + mcEscape(quickPrice) + '</div>';
          }
          quickInfoHtml += '</div>';
        }

        /* Bulle d'info du bouton "détails" : traduite selon la langue
           actuellement sélectionnée (FR/EN), pas figée en français. */
        var moreDetailsLabel = mcCurrentLang() === 'en'
          ? 'View more details'
          : 'Voir plus de détails';

        summary.innerHTML =
          selectHtml +
          '<button type="button" class="mc-mobile-card-main" aria-expanded="false">' +
            '<div class="mc-mobile-card-title">' + titleItem.html + '</div>' +
            (subtitleItem && (!quickCategory || mcNormalizeStateText(subtitleItem.text) !== mcNormalizeStateText(quickCategory))
              ? '<div class="mc-mobile-card-subtitle">' + mcEscape(subtitleItem.text) + '</div>'
              : '') +
            quickInfoHtml +
          '</button>' +
          '<button type="button" class="mc-mobile-card-chevron" aria-label="' + mcEscape(moreDetailsLabel) + '" data-tooltip="' + mcEscape(moreDetailsLabel) + '">⋮</button>';

        var mainButton = summary.querySelector('.mc-mobile-card-main');
        var chevronButton = summary.querySelector('.mc-mobile-card-chevron');
        var mobileCheckbox = summary.querySelector('.mc-mobile-select');

        var details = document.createElement('div');
        details.className = 'mc-mobile-card-details';

        var grid = document.createElement('div');
        grid.className = 'mc-mobile-card-grid';

        useful.forEach(function(item){
          var detailRow = document.createElement('div');
          var normalizedLabel = mcNormalizeStateText(item.label);
          var rowClasses = ['mc-mobile-detail-row'];

          /* Commandes : identifie précisément les deux blocs métriques
             pour pouvoir leur donner un layout responsive dédié. */
          if (window.location.pathname.replace(/\/+$/,'') === '/admin/order/list') {
            if (normalizedLabel === 'total' || normalizedLabel === 'prix total') {
              rowClasses.push('mc-order-metric-card', 'mc-order-metric-total');
            }

            if (
              normalizedLabel === 'créneau' ||
              normalizedLabel === 'creneau' ||
              normalizedLabel === 'time slot'
            ) {
              rowClasses.push('mc-order-metric-card', 'mc-order-metric-slot');
            }
          }

          detailRow.className = rowClasses.join(' ');
          detailRow.innerHTML =
            '<div class="mc-mobile-detail-label">' + mcEscape(item.label) + '</div>' +
            '<div class="mc-mobile-detail-value">' + item.html + '</div>';
          grid.appendChild(detailRow);
        });

        details.appendChild(grid);

        if (actionCell && actionCell.querySelector('a,button')) {
          var actions = document.createElement('div');
          actions.className = 'mc-mobile-card-actions';
          actions.innerHTML = actionCell.innerHTML;
          details.appendChild(actions);
        }

        function toggleDetails(){
          var open = record.classList.toggle('mc-open');
          mainButton.setAttribute('aria-expanded', open ? 'true' : 'false');
          chevronButton.setAttribute(
            'aria-label',
            open ? 'Masquer les détails' : 'Afficher les détails'
          );
        }

        mainButton.addEventListener('click', toggleDetails);
        chevronButton.addEventListener('click', toggleDetails);

        if (mobileCheckbox && originalCheckbox) {
          mobileCheckbox.checked = !!originalCheckbox.checked;
          record.classList.toggle('mc-selected', mobileCheckbox.checked);

          mobileCheckboxes.push({
            mobile: mobileCheckbox,
            original: originalCheckbox,
            card: record
          });

          mobileCheckbox.addEventListener('change', function(event){
            event.stopPropagation();

            originalCheckbox.checked = mobileCheckbox.checked;
            record.classList.toggle('mc-selected', mobileCheckbox.checked);

            /* Trigger native listeners used by SQLAdmin bulk actions */
            originalCheckbox.dispatchEvent(
              new Event('change', {bubbles:true})
            );

            updateSelectionUI();
          });

          /* Clicking the selection label must not open the card */
          var selectWrap = summary.querySelector('.mc-mobile-card-select-wrap');
          if (selectWrap) {
            selectWrap.addEventListener('click', function(event){
              event.stopPropagation();
            });
          }
        }

        details.addEventListener('click', function(event){
          if (event.target.closest('a,button,input,label')) {
            event.stopPropagation();
          }
        });

        if (photoColumnIndex !== -1) {
          var photoWrap = document.createElement('div');
          photoWrap.className = 'mc-mobile-card-photo-wrap';
          if (photoSrc) {
            var photoImg = document.createElement('img');
            photoImg.className = 'mc-mobile-card-photo';
            photoImg.src = photoSrc;
            photoImg.alt = '';
            photoImg.loading = 'lazy';
            /* Si l'URL ne charge pas (chemin relatif pensé pour un autre
               domaine, image supprimée, etc.), on bascule sur le
               placeholder plutôt que de montrer l'icône "image cassée"
               du navigateur. */
            photoImg.addEventListener('error', function(){
              photoWrap.innerHTML = '';
              photoWrap.classList.add('mc-mobile-card-photo-placeholder');
              photoWrap.textContent = '🍽️';
            });
            photoWrap.appendChild(photoImg);
          } else {
            photoWrap.classList.add('mc-mobile-card-photo-placeholder');
            photoWrap.textContent = '🍽️';
          }
          record.appendChild(photoWrap);
        }

        /* Statut (disponibilité, statut de commande...) : un point coloré
           flottant, ancré au vrai coin haut-droit de la carte entière
           (et non de la zone de texte), pas de doublon avec un badge texte. */
        if (stateKind) {
          var stateDot = document.createElement('span');
          stateDot.className = 'mc-mobile-state-dot mc-state-' + stateColor;
          stateDot.setAttribute('data-tooltip', mcTranslateText(stateValue));
          stateDot.setAttribute('aria-label', mcTranslateText(stateValue));
          record.appendChild(stateDot);
        }

        record.appendChild(summary);
        record.appendChild(details);
        cardsWrap.appendChild(record);
      });

      if (!cardsWrap.querySelector('.mc-mobile-record-card')) return;

      if (selectAll) {
        selectAll.addEventListener('change', function(){
          mobileCheckboxes.forEach(function(info){
            info.mobile.checked = selectAll.checked;
            info.original.checked = selectAll.checked;
            info.card.classList.toggle('mc-selected', selectAll.checked);
            info.original.dispatchEvent(
              new Event('change', {bubbles:true})
            );
          });
          updateSelectionUI();
        });
      }

      responsive.insertAdjacentElement('afterend', cardsWrap);
      card.classList.add('mc-mobile-card-mode');

      var currentMobileListPath = window.location.pathname.replace(/\/+$/,'');
      card.classList.toggle('mc-order-item-card-mode', currentMobileListPath === '/admin/order-item/list');
      card.classList.toggle('mc-dish-list-card-mode', currentMobileListPath === '/admin/dish/list');

      mcApplyLanguage(cardsWrap);
      updateSelectionUI();
      mcInitEventMobileFilters(card, cardsWrap);
      mcInitDishMobileFilters(card, cardsWrap);
      mcGroupOrderItemCards(card, cardsWrap);
      /* mcGroupOrderItemCards already builds the complete compact preview.
         Do not run mcEnhanceOrderItemCards here: it duplicates quantity, price
         and customization information inside the same card. */
      mcEnhanceDishCards(card, cardsWrap);
    });
  }


  /* =========================================================
     REGROUPEMENT DES ARTICLES COMMANDÉS PAR COMMANDE — MOBILE
     Sur /admin/order-item/list, chaque plat d'une même commande
     apparaissait comme une carte "Commande #X" séparée, ce qui
     prêtait à confusion. On les regroupe ici sous un seul en-tête
     par commande, en gardant chaque plat visible en dessous.
  ========================================================= */
  function mcGroupOrderItemCards(card, cardsWrap){
    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/order-item/list') return;
    if (!cardsWrap) return;

    var records = Array.prototype.slice.call(
      cardsWrap.querySelectorAll('.mc-mobile-record-card')
    );
    if (!records.length) return;

    function norm(value){
      return (value || '').toString().replace(/\s+/g,' ').trim().toLowerCase();
    }

    function valueFromRows(recordCard, acceptedLabels){
      var found = '';
      Array.prototype.slice.call(
        recordCard.querySelectorAll('.mc-mobile-detail-row')
      ).some(function(row){
        var labelEl = row.querySelector('.mc-mobile-detail-label');
        var valueEl = row.querySelector('.mc-mobile-detail-value');
        if (!labelEl || !valueEl) return false;
        var label = norm(labelEl.textContent);
        if (acceptedLabels.indexOf(label) === -1) return false;
        found = (valueEl.textContent || '').replace(/\s+/g,' ').trim();
        return true;
      });
      return found;
    }

    var groups = [];
    var groupByKey = {};

    records.forEach(function(recordCard){
      var titleEl = recordCard.querySelector('.mc-mobile-card-title');
      var subtitleEl = recordCard.querySelector('.mc-mobile-card-subtitle');
      var mainEl = recordCard.querySelector('.mc-mobile-card-main');
      var chevronEl = recordCard.querySelector('.mc-mobile-card-chevron');

      var orderLabel = titleEl ? titleEl.textContent.trim() : 'Commande';
      var dishLabel = subtitleEl ? subtitleEl.textContent.trim() : '';

      /* Le groupe porte le numéro de commande ; la carte porte uniquement le plat. */
      if (titleEl && dishLabel) titleEl.textContent = dishLabel;
      if (subtitleEl) subtitleEl.remove();

      var quantity = valueFromRows(recordCard, ['quantité','quantite','quantity']);
      var unitPrice = valueFromRows(recordCard, ['prix unitaire','unit price']);
      var removed = valueFromRows(recordCard, ['sans','without']);
      var customization = valueFromRows(recordCard, ['personnalisation','customization','customisation']);

      /* Classes ciblées pour le détail ouvert : évite le mot Commande coupé lettre par lettre. */
      Array.prototype.slice.call(
        recordCard.querySelectorAll('.mc-mobile-detail-row')
      ).forEach(function(row){
        var labelEl = row.querySelector('.mc-mobile-detail-label');
        if (!labelEl) return;
        var label = norm(labelEl.textContent);
        if (label === 'commande' || label === 'order') row.classList.add('mc-order-item-detail-order');
        if (label === 'plat' || label === 'dish') row.classList.add('mc-order-item-detail-dish');
        if (label === 'quantité' || label === 'quantite' || label === 'quantity') row.classList.add('mc-order-item-detail-qty');
        if (label === 'prix unitaire' || label === 'unit price') row.classList.add('mc-order-item-detail-price');
        if (label === 'sans' || label === 'without') row.classList.add('mc-order-item-detail-note');
        if (label.indexOf('personnalisation') !== -1 || label.indexOf('custom') !== -1) row.classList.add('mc-order-item-detail-options');
      });

      /* Résumé visible SANS ouvrir la carte. */
      if (mainEl && !mainEl.querySelector('.mc-order-item-preview')) {
        var preview = document.createElement('div');
        preview.className = 'mc-order-item-preview';

        var chips = document.createElement('div');
        chips.className = 'mc-order-item-preview-chips';

        if (quantity && quantity !== '—') {
          var qty = document.createElement('span');
          qty.className = 'mc-order-item-preview-chip mc-qty';
          qty.textContent = quantity;
          chips.appendChild(qty);
        }

        if (unitPrice && unitPrice !== '—') {
          var price = document.createElement('span');
          price.className = 'mc-order-item-preview-chip mc-price';
          price.textContent = unitPrice;
          chips.appendChild(price);
        }

        if (chips.childNodes.length) preview.appendChild(chips);

        if (removed && removed !== '—') {
          var withoutLine = document.createElement('div');
          withoutLine.className = 'mc-order-item-preview-note';
          withoutLine.innerHTML = '<strong>' +
            (mcCurrentLang()==='en' ? 'Without' : 'Sans') +
            ' :</strong> ' + mcEscape(removed);
          preview.appendChild(withoutLine);
        }

        if (customization && customization !== '—') {
          var customLine = document.createElement('div');
          customLine.className = 'mc-order-item-preview-note';
          customLine.innerHTML = '<strong>' +
            (mcCurrentLang()==='en' ? 'Custom' : 'Personnalisation') +
            ' :</strong> ' + mcEscape(customization);
          preview.appendChild(customLine);
        }

        mainEl.appendChild(preview);
      }

      if (chevronEl) {
        chevronEl.textContent = '›';
        chevronEl.setAttribute(
          'aria-label',
          mcCurrentLang()==='en' ? 'View item details' : 'Voir les détails de l’article'
        );
        chevronEl.setAttribute(
          'data-tooltip',
          mcCurrentLang()==='en' ? 'View details' : 'Voir les détails'
        );
      }

      if (!groupByKey[orderLabel]) {
        var group = {label: orderLabel, items: []};
        groupByKey[orderLabel] = group;
        groups.push(group);
      }
      groupByKey[orderLabel].items.push(recordCard);
    });

    var fragment = document.createDocumentFragment();

    groups.forEach(function(group){
      var wrap = document.createElement('section');
      wrap.className = 'mc-order-group';

      var header = document.createElement('div');
      header.className = 'mc-order-group-header';
      var cleanOrderNumber = (group.label || '')
        .replace(/^(Commande|Order)\s*/i, '')
        .trim()
        .replace(/^#+/, '');
      if (cleanOrderNumber) cleanOrderNumber = '#' + cleanOrderNumber;

      header.innerHTML =
        '<div class="mc-order-group-heading">' +
          '<span class="mc-order-group-kicker">' +
            (mcCurrentLang()==='en' ? 'ORDER' : 'COMMANDE') +
          '</span>' +
          '<span class="mc-order-group-title">' + mcEscape(cleanOrderNumber || group.label) + '</span>' +
        '</div>' +
        '<span class="mc-order-group-count">' +
          group.items.length + (group.items.length > 1 ? ' articles' : ' article') +
        '</span>';

      var itemsWrap = document.createElement('div');
      itemsWrap.className = 'mc-order-group-items';
      group.items.forEach(function(item){ itemsWrap.appendChild(item); });

      wrap.appendChild(header);
      wrap.appendChild(itemsWrap);
      fragment.appendChild(wrap);
    });

    cardsWrap.appendChild(fragment);
    mcApplyLanguage(cardsWrap);
  }


  /* =========================================================
     ARTICLES COMMANDÉS — enrichit les cartes avec les infos
     essentielles visibles immédiatement : quantité, prix,
     sans / personnalisation, et meilleures proportions.
  ========================================================= */
  function mcEnhanceOrderItemCards(card, cardsWrap){
    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/order-item/list') return;
    if (!card || !cardsWrap) return;

    var records = Array.prototype.slice.call(
      cardsWrap.querySelectorAll('.mc-mobile-record-card')
    );
    if (!records.length) return;

    function norm(value){
      return (value || '').toString().trim().replace(/\s+/g,' ').toLowerCase();
    }

    records.forEach(function(record){
      var main = record.querySelector('.mc-mobile-card-main');
      var grid = record.querySelector('.mc-mobile-card-grid');
      if (!main || !grid) return;

      var quantity = '';
      var unitPrice = '';
      var removed = '';
      var options = '';

      Array.prototype.slice.call(grid.querySelectorAll('.mc-mobile-detail-row')).forEach(function(row){
        var labelEl = row.querySelector('.mc-mobile-detail-label');
        var valueEl = row.querySelector('.mc-mobile-detail-value');
        if (!labelEl || !valueEl) return;

        var label = norm(labelEl.textContent);
        var value = (valueEl.textContent || '').replace(/\s+/g,' ').trim();

        if (label === 'commande' || label === 'order') {
          row.classList.add('mc-order-item-detail-order');
        }
        if (label === 'quantité' || label === 'quantite' || label === 'quantity') {
          quantity = value;
          row.classList.add('mc-order-item-detail-qty');
        }
        if (label === 'prix unitaire' || label === 'unit price') {
          unitPrice = value;
          row.classList.add('mc-order-item-detail-price');
        }
        if (label === 'sans' || label === 'without') {
          removed = value;
          row.classList.add('mc-order-item-detail-note');
        }
        if (label.indexOf('personnalisation') !== -1 || label.indexOf('custom') !== -1) {
          options = value;
          row.classList.add('mc-order-item-detail-options');
        }
      });

      var existingMetrics = main.querySelector('.mc-order-item-inline-metrics');
      if (!existingMetrics) {
        var summaryBits = [];
        if (quantity && quantity !== '—') {
          summaryBits.push('<span class="mc-order-item-chip">' + mcEscape(quantity) + '</span>');
        }
        if (unitPrice && unitPrice !== '—') {
          summaryBits.push('<span class="mc-order-item-chip mc-order-item-chip-price">' + mcEscape(unitPrice) + '</span>');
        }
        if (summaryBits.length) {
          main.insertAdjacentHTML('beforeend', '<div class="mc-order-item-inline-metrics">' + summaryBits.join('') + '</div>');
        }
      }

      if (!main.querySelector('.mc-order-item-note[data-role="removed"]') && removed && removed !== '—') {
        main.insertAdjacentHTML(
          'beforeend',
          '<div class="mc-order-item-note" data-role="removed"><strong>' +
            mcEscape(mcCurrentLang() === 'en' ? 'Without:' : 'Sans :') +
          '</strong> ' + mcEscape(removed) + '</div>'
        );
      }

      if (!main.querySelector('.mc-order-item-note[data-role="options"]') && options && options !== '—') {
        main.insertAdjacentHTML(
          'beforeend',
          '<div class="mc-order-item-note" data-role="options"><strong>' +
            mcEscape(mcCurrentLang() === 'en' ? 'Custom:' : 'Personnalisation :') +
          '</strong> ' + mcEscape(options) + '</div>'
        );
      }
    });
  }


  /* =========================================================
     PLATS — petit polissage de proportions en mobile pour que
     les cartes restent proches du nouveau style commandes.
  ========================================================= */
  function mcEnhanceDishCards(card, cardsWrap){
    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/dish/list') return;
    if (!card || !cardsWrap) return;

    Array.prototype.slice.call(cardsWrap.querySelectorAll('.mc-mobile-record-card')).forEach(function(record){
      var title = record.querySelector('.mc-mobile-card-title');
      var quick = record.querySelector('.mc-mobile-card-quick');
      var main = record.querySelector('.mc-mobile-card-main');
      if (title) title.classList.add('mc-dish-card-title-ready');
      if (quick) quick.classList.add('mc-dish-card-quick-ready');
      if (main) main.classList.add('mc-dish-card-main-ready');
    });
  }



  /* =========================================================
     FILTRES ÉVÉNEMENTS — MOBILE
     Construit les options à partir des lignes SQLAdmin présentes.
  ========================================================= */
  function mcInitEventMobileFilters(card, cardsWrap){
    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/event-reservation/list') return;
    if (!card || !cardsWrap) return;

    var old = cardsWrap.querySelector('.mc-event-filters');
    if (old) old.remove();

    var records = Array.prototype.slice.call(
      cardsWrap.querySelectorAll('.mc-mobile-record-card')
    );
    if (!records.length) return;

    function norm(value){
      return (value || '')
        .toString()
        .trim()
        .replace(/\s+/g,' ')
        .toLowerCase();
    }

    var types = [];
    var statuses = [];

    records.forEach(function(record){
      var details = Array.prototype.slice.call(
        record.querySelectorAll('.mc-mobile-detail-row')
      );

      var eventType = '';
      var status = '';

      details.forEach(function(row){
        var labelEl = row.querySelector('.mc-mobile-detail-label');
        var valueEl = row.querySelector('.mc-mobile-detail-value');
        if (!labelEl || !valueEl) return;

        var label = norm(labelEl.textContent);
        var value = (valueEl.textContent || '').replace(/\s+/g,' ').trim();

        if (
          !eventType &&
          (
            label.indexOf('événement') !== -1 ||
            label.indexOf('event') !== -1 ||
            label.indexOf('type') !== -1
          )
        ) {
          eventType = value;
        }

        if (
          !status &&
          (
            label.indexOf('statut') !== -1 ||
            label.indexOf('status') !== -1 ||
            label.indexOf('état') !== -1
          )
        ) {
          status = value;
        }
      });

      /* Fallback: sur cette liste, le titre de la carte est le type d'événement. */
      if (!eventType) {
        var title = record.querySelector('.mc-mobile-card-title');
        eventType = title ? (title.textContent || '').replace(/\s+/g,' ').trim() : '';
      }

      record.dataset.mcEventType = norm(eventType);
      record.dataset.mcEventStatus = norm(status);

      if (eventType && types.indexOf(eventType) === -1) types.push(eventType);
      if (status && statuses.indexOf(status) === -1) statuses.push(status);
    });

    types.sort(function(a,b){ return a.localeCompare(b, 'fr'); });
    statuses.sort(function(a,b){ return a.localeCompare(b, 'fr'); });

    var filters = document.createElement('section');
    filters.className = 'mc-event-filters';

    var typeOptions =
      '<option value="">Tous les types</option>' +
      types.map(function(value){
        return '<option value="'+mcEscape(norm(value))+'">'+mcEscape(value)+'</option>';
      }).join('');

    var statusOptions =
      '<option value="">Tous les statuts</option>' +
      statuses.map(function(value){
        return '<option value="'+mcEscape(norm(value))+'">'+mcEscape(value)+'</option>';
      }).join('');

    filters.innerHTML =
      '<div class="mc-event-filter-head">' +
        '<div class="mc-event-filter-title">Filtrer les événements</div>' +
        '<button type="button" class="mc-event-filter-reset">Réinitialiser</button>' +
      '</div>' +
      '<div class="mc-event-filter-grid">' +
        '<label class="mc-event-filter-field">' +
          '<span class="mc-event-filter-label">Type</span>' +
          '<select class="mc-event-filter-select" data-event-filter="type">' +
            typeOptions +
          '</select>' +
        '</label>' +
        '<label class="mc-event-filter-field">' +
          '<span class="mc-event-filter-label">Statut</span>' +
          '<select class="mc-event-filter-select" data-event-filter="status">' +
            statusOptions +
          '</select>' +
        '</label>' +
      '</div>' +
      '<div class="mc-event-filter-result"></div>';

    var selectBar = cardsWrap.querySelector('.mc-mobile-selectbar');
    if (selectBar) {
      selectBar.insertAdjacentElement('afterend', filters);
    } else {
      cardsWrap.insertBefore(filters, cardsWrap.firstChild);
    }

    var typeSelect = filters.querySelector('[data-event-filter="type"]');
    var statusSelect = filters.querySelector('[data-event-filter="status"]');
    var reset = filters.querySelector('.mc-event-filter-reset');
    var result = filters.querySelector('.mc-event-filter-result');

    var empty = document.createElement('div');
    empty.className = 'mc-event-no-results';
    empty.textContent = 'Aucun événement ne correspond à ces filtres.';
    empty.style.display = 'none';
    cardsWrap.appendChild(empty);

    function apply(){
      var wantedType = norm(typeSelect.value);
      var wantedStatus = norm(statusSelect.value);
      var visible = 0;

      records.forEach(function(record){
        var matchType =
          !wantedType || record.dataset.mcEventType === wantedType;
        var matchStatus =
          !wantedStatus || record.dataset.mcEventStatus === wantedStatus;

        var show = matchType && matchStatus;
        record.classList.toggle('mc-event-filter-hidden', !show);
        if (show) visible += 1;
      });

      result.textContent =
        visible + (visible > 1 ? ' événements affichés' : ' événement affiché');
      empty.style.display = visible === 0 ? 'block' : 'none';
    }

    typeSelect.addEventListener('change', apply);
    statusSelect.addEventListener('change', apply);

    reset.addEventListener('click', function(){
      typeSelect.value = '';
      statusSelect.value = '';
      apply();
    });

    apply();
    mcApplyLanguage(filters);
  }


  /* =========================================================
     FILTRE PLATS PAR CATÉGORIE — MOBILE
     Les catégories sont récupérées directement depuis les cartes.
  ========================================================= */
  function mcInitDishMobileFilters(card, cardsWrap){
    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/dish/list') return;
    if (!card || !cardsWrap) return;

    var old = cardsWrap.querySelector('.mc-dish-filters');
    if (old) old.remove();

    var oldEmpty = cardsWrap.querySelector('.mc-dish-no-results');
    if (oldEmpty) oldEmpty.remove();

    function clean(value){
      return (value || '').toString().replace(/\s+/g,' ').trim();
    }

    function norm(value){
      return clean(value).toLowerCase();
    }

    var table = card.querySelector('.table-responsive table');
    if (!table) return;

    var tbody = table.querySelector('tbody');
    if (!tbody) return;

    /* -------------------------------------------------------
       Le filtre mobile travaille sur TOUTES les pages.
       On ne dépend plus des cartes visibles seulement.
    ------------------------------------------------------- */

    function getCategoryColumnIndex(sourceTable){
      var headers = Array.prototype.slice.call(
        sourceTable.querySelectorAll('thead th')
      );

      for (var i = 0; i < headers.length; i++) {
        var label = norm(headers[i].textContent);
        if (
          label === 'catégorie' ||
          label === 'categorie' ||
          label === 'category'
        ) {
          return i;
        }
      }
      return -1;
    }

    function extractRows(sourceTable){
      var categoryIndex = getCategoryColumnIndex(sourceTable);
      if (categoryIndex < 0) return [];

      return Array.prototype.slice.call(
        sourceTable.querySelectorAll('tbody tr')
      ).map(function(row){
        var cells = Array.prototype.slice.call(row.children);

        var category =
          cells[categoryIndex]
            ? clean(cells[categoryIndex].textContent)
            : '';

        /* IMPORTANT:
           Les checkboxes SQLAdmin peuvent toutes avoir la même value
           (souvent "on"). On ne peut donc PAS les utiliser comme ID,
           sinon le dédoublonnage considère 79 plats comme une seule ligne.

           On cherche d'abord un vrai identifiant dans les URLs
           view/edit/delete. Sinon on utilise le HTML complet de la ligne.
        */
        var actionLink = row.querySelector(
          'a[href*="/view/"],a[href*="/edit/"],a[href*="/delete/"],a[href*="pks="]'
        );

        var rowKey = '';

        if (actionLink) {
          var href = actionLink.getAttribute('href') || '';
          var idMatch =
            href.match(/\/(?:view|edit|delete)\/([^/?#]+)/i) ||
            href.match(/[?&]pks=([^&#]+)/i);

          if (idMatch) {
            rowKey = 'pk:' + decodeURIComponent(idMatch[1]);
          }
        }

        if (!rowKey) {
          rowKey = 'row:' + row.outerHTML;
        }

        return {
          key: rowKey,
          html: row.outerHTML,
          category: category
        };
      });
    }

    function dedupeRows(rows){
      var seen = {};
      return rows.filter(function(item){
        if (seen[item.key]) return false;
        seen[item.key] = true;
        return true;
      });
    }

    function detectTotalPages(doc){
      var pageNumbers = Array.prototype.slice.call(
        doc.querySelectorAll('.pagination .page-link')
      )
      .map(function(link){
        var n = parseInt(clean(link.textContent), 10);
        return isNaN(n) ? null : n;
      })
      .filter(function(n){ return n !== null; });

      return pageNumbers.length
        ? Math.max.apply(null, pageNumbers)
        : 1;
    }

    function fetchPage(pageNo){
      var url = new URL(window.location.href);

      /* On garde le pageSize actuel, mais on force la page demandée
         et on enlève la recherche pour toujours charger la liste complète. */
      url.searchParams.delete('search');
      url.searchParams.set('page', String(pageNo));

      return fetch(url.toString(), {
        method:'GET',
        credentials:'same-origin',
        headers:{'X-Requested-With':'XMLHttpRequest'}
      })
      .then(function(response){
        if (!response.ok) throw new Error('dish page');
        return response.text();
      })
      .then(function(htmlText){
        var doc = new DOMParser().parseFromString(htmlText, 'text/html');
        var sourceTable = doc.querySelector('.table-responsive table');

        return {
          rows: sourceTable ? extractRows(sourceTable) : [],
          pages: detectTotalPages(doc)
        };
      });
    }

    var cache = window.__mcDishMobileCategoryCache || {
      ready:false,
      loading:false,
      rows:[],
      categories:[],
      selected:''
    };
    window.__mcDishMobileCategoryCache = cache;

    var filters = document.createElement('section');
    filters.className = 'mc-dish-filters';

    filters.innerHTML =
      '<div class="mc-dish-filter-head">' +
        '<div class="mc-dish-filter-title">Filtrer les plats</div>' +
        '<button type="button" class="mc-dish-filter-reset">Réinitialiser</button>' +
      '</div>' +
      '<label class="mc-dish-filter-field">' +
        '<span class="mc-dish-filter-label">Catégorie</span>' +
        '<select class="mc-dish-filter-select">' +
          '<option value="">Chargement des catégories…</option>' +
        '</select>' +
      '</label>' +
      '<div class="mc-dish-filter-result">Chargement…</div>';

    var selectBar = cardsWrap.querySelector('.mc-mobile-selectbar');

    if (selectBar) {
      selectBar.insertAdjacentElement('afterend', filters);
    } else {
      cardsWrap.insertBefore(filters, cardsWrap.firstChild);
    }

    var select = filters.querySelector('.mc-dish-filter-select');
    var reset = filters.querySelector('.mc-dish-filter-reset');
    var result = filters.querySelector('.mc-dish-filter-result');

    var empty = document.createElement('div');
    empty.className = 'mc-dish-no-results';
    empty.textContent = 'Aucun plat dans cette catégorie.';
    empty.style.display = 'none';
    cardsWrap.appendChild(empty);

    function renderOptions(){
      select.innerHTML =
        '<option value="">Toutes les catégories</option>' +
        cache.categories.map(function(category){
          return '<option value="' + mcEscape(category) + '">' +
            mcEscape(category) +
          '</option>';
        }).join('');

      select.value = cache.selected || '';
    }

    function hidePagination(){
      var footer = card.querySelector('.card-footer');
      if (footer) footer.style.display = 'none';
    }

    function showPagination(){
      var footer = card.querySelector('.card-footer');
      if (footer) footer.style.display = '';
    }

    function rebuildMobileCardsFromRows(rows){
      /* On remplace le contenu du tbody caché,
         puis on laisse mcInitMobileTableCards recréer les cartes. */
      tbody.innerHTML = rows.map(function(item){
        return item.html;
      }).join('');

      var oldCards = card.querySelector('.mc-mobile-cards');
      if (oldCards) oldCards.remove();

      card.classList.remove('mc-mobile-card-mode');

      mcInitMobileTableCards(document);
    }

    function restoreNativeCurrentPage(){
      /* Le reset doit revenir à la vraie page SQLAdmin actuelle.
         Le plus fiable est de recharger la page courante sans filtre. */
      var url = new URL(window.location.href);
      url.searchParams.delete('search');

      fetch(url.toString(), {
        method:'GET',
        credentials:'same-origin',
        headers:{'X-Requested-With':'XMLHttpRequest'}
      })
      .then(function(response){
        if (!response.ok) throw new Error('restore');
        return response.text();
      })
      .then(function(htmlText){
        var doc = new DOMParser().parseFromString(htmlText, 'text/html');
        var sourceTable = doc.querySelector('.table-responsive table');
        if (!sourceTable) return;

        tbody.innerHTML = Array.prototype.slice.call(
          sourceTable.querySelectorAll('tbody tr')
        ).map(function(row){
          return row.outerHTML;
        }).join('');

        var oldCards = card.querySelector('.mc-mobile-cards');
        if (oldCards) oldCards.remove();

        card.classList.remove('mc-mobile-card-mode');
        showPagination();
        mcInitMobileTableCards(document);
      })
      .catch(function(){
        showPagination();
      });
    }

    function applyCategory(category){
      cache.selected = clean(category);

      if (!cache.ready) return;

      var wanted = norm(cache.selected);

      if (!wanted) {
        restoreNativeCurrentPage();
        return;
      }

      var filtered = cache.rows.filter(function(item){
        return norm(item.category) === wanted;
      });

      rebuildMobileCardsFromRows(filtered);
      hidePagination();

      var liveSelect = card.querySelector('.mc-dish-filter-select');
      var liveResult = card.querySelector('.mc-dish-filter-result');
      var liveEmpty = card.querySelector('.mc-dish-no-results');

      if (liveSelect) liveSelect.value = cache.selected;

      if (liveResult) {
        liveResult.textContent =
          filtered.length +
          (filtered.length > 1 ? ' plats affichés' : ' plat affiché');
      }

      if (liveEmpty) {
        liveEmpty.style.display = filtered.length === 0 ? 'block' : 'none';
      }
    }

    function loadAllRows(){
      if (cache.ready) {
        renderOptions();
        result.textContent = cache.rows.length + ' plats disponibles';
        return;
      }

      if (cache.loading) return;
      cache.loading = true;

      /* MOBILE FIX:
         On ne parcourt plus la pagination visible, car SQLAdmin peut
         masquer certaines pages numériques dans la barre de pagination.
         Exemple : 79 plats avec 10/page => 8 pages, mais le DOM peut
         n'afficher que 1..7 + "suivant". Résultat : la page 8 n'était
         jamais chargée et une catégorie pouvait afficher 6 plats au lieu de 7.

         Comme sur desktop, on demande directement tous les plats en une fois.
      */
      var url = new URL(window.location.href);
      url.searchParams.delete('search');
      url.searchParams.delete('page_size');
      url.searchParams.set('pageSize', '1000');
      url.searchParams.set('page', '1');

      fetch(url.toString(), {
        method:'GET',
        credentials:'same-origin',
        headers:{'X-Requested-With':'XMLHttpRequest'}
      })
      .then(function(response){
        if (!response.ok) {
          throw new Error('Impossible de charger tous les plats sur mobile.');
        }
        return response.text();
      })
      .then(function(htmlText){
        var doc = new DOMParser().parseFromString(htmlText, 'text/html');
        var sourceTable = doc.querySelector('.table-responsive table');

        if (!sourceTable) {
          throw new Error('Table Plats introuvable sur mobile.');
        }

        var allRows = dedupeRows(extractRows(sourceTable));

        cache.rows = allRows;

        var categoryMap = {};
        allRows.forEach(function(item){
          if (item.category) categoryMap[item.category] = true;
        });

        cache.categories = Object.keys(categoryMap).sort(function(a,b){
          return a.localeCompare(b, 'fr', {sensitivity:'base'});
        });

        cache.ready = true;
        cache.loading = false;

        renderOptions();
        result.textContent = cache.rows.length + ' plats disponibles';

        /* Si une catégorie était déjà sélectionnée, on la réapplique
           maintenant sur la collection complète. */
        if (cache.selected) {
          applyCategory(cache.selected);
        }
      })
      .catch(function(error){
        console.error('Miss Chawarma mobile category filter:', error);

        /* Fallback : au moins la page visible */
        cache.rows = extractRows(table);

        var fallbackMap = {};
        cache.rows.forEach(function(item){
          if (item.category) fallbackMap[item.category] = true;
        });

        cache.categories = Object.keys(fallbackMap).sort(function(a,b){
          return a.localeCompare(b, 'fr', {sensitivity:'base'});
        });

        cache.ready = true;
        cache.loading = false;

        renderOptions();
        result.textContent = cache.rows.length + ' plats chargés';
      });
    }

    select.addEventListener('change', function(){
      applyCategory(select.value);
    });

    reset.addEventListener('click', function(){
      cache.selected = '';
      select.value = '';
      restoreNativeCurrentPage();
    });

    loadAllRows();
    mcApplyLanguage(filters);
  }

  /* =========================================================
     FILTRE PLATS PAR CATÉGORIE — DESKTOP
     - utilise uniquement la colonne Catégorie
     - charge tous les plats en arrière-plan
     - ne dépend pas de la pagination courante
  ========================================================= */
  function mcInitDishDesktopFilters(){
    if (window.innerWidth < 576) {
      document.querySelectorAll('.mc-dish-desktop-filters,.mc-dish-desktop-empty').forEach(function(el){
        el.remove();
      });
      return;
    }

    document.querySelectorAll('.mc-dish-filters,.mc-dish-no-results').forEach(function(el){
      el.remove();
    });

    var path = window.location.pathname.replace(/\/+$/,'');
    if (path !== '/admin/dish/list') return;

    var card = document.querySelector('.card');
    if (!card) return;

    /* Remove stale duplicate desktop filters before rebuilding */
    var existingDesktopFilters = card.querySelectorAll('.mc-dish-desktop-filters');
    if (existingDesktopFilters.length > 1) {
      Array.prototype.slice.call(existingDesktopFilters, 1).forEach(function(el){
        el.remove();
      });
    }

    if (card.dataset.mcDishDesktopFilterReady === '1' &&
        card.querySelector('.mc-dish-desktop-filters')) return;

    var table = card.querySelector('.table-responsive table');
    if (!table) return;

    var tbody = table.querySelector('tbody');
    if (!tbody) return;

    card.dataset.mcDishDesktopFilterReady = '1';

    function clean(value){
      return (value || '').toString().replace(/\s+/g,' ').trim();
    }

    function norm(value){
      return clean(value).toLowerCase();
    }

    function getCategoryColumnIndex(sourceTable){
      var headers = Array.prototype.slice.call(
        sourceTable.querySelectorAll('thead th')
      );

      for (var i = 0; i < headers.length; i++) {
        var label = norm(headers[i].textContent);
        if (
          label === 'catégorie' ||
          label === 'categorie' ||
          label === 'category'
        ) {
          return i;
        }
      }
      return -1;
    }

    function extractRows(sourceTable){
      var categoryIndex = getCategoryColumnIndex(sourceTable);
      if (categoryIndex < 0) return [];

      return Array.prototype.slice.call(
        sourceTable.querySelectorAll('tbody tr')
      ).map(function(row){
        var cells = Array.prototype.slice.call(row.children);
        var category =
          cells[categoryIndex]
            ? clean(cells[categoryIndex].textContent)
            : '';

        return {
          html: row.outerHTML,
          category: category
        };
      });
    }

    var originalRowsHtml = tbody.innerHTML;
    var footer = card.querySelector('.card-footer');
    var originalFooterDisplay = footer ? footer.style.display : '';

    var filter = document.createElement('section');
    filter.className = 'mc-dish-desktop-filters';
    filter.innerHTML =
      '<label class="mc-dish-desktop-filter-main">' +
        '<span class="mc-dish-desktop-filter-label">Filtrer par catégorie</span>' +
        '<select class="mc-dish-desktop-filter-select">' +
          '<option value="">Chargement des catégories…</option>' +
        '</select>' +
      '</label>' +
      '<div class="mc-dish-desktop-filter-result">Chargement…</div>' +
      '<button type="button" class="mc-dish-desktop-filter-reset">Réinitialiser</button>';

    var tableResponsive = table.closest('.table-responsive');
    tableResponsive.insertAdjacentElement('beforebegin', filter);

    var select = filter.querySelector('.mc-dish-desktop-filter-select');
    var result = filter.querySelector('.mc-dish-desktop-filter-result');
    var reset = filter.querySelector('.mc-dish-desktop-filter-reset');

    var empty = document.createElement('div');
    empty.className = 'mc-dish-desktop-empty';
    empty.textContent = 'Aucun plat dans cette catégorie.';
    empty.style.display = 'none';
    tableResponsive.insertAdjacentElement('afterend', empty);

    function showRows(rows){
      tbody.innerHTML = rows.map(function(item){
        return item.html;
      }).join('');
      mcApplyLanguage(tbody);
    }

    function restoreOriginalPage(){
      tbody.innerHTML = originalRowsHtml;
      if (footer) footer.style.display = originalFooterDisplay;
      empty.style.display = 'none';
      mcApplyLanguage(tbody);
    }

    var cache = window.__mcDishDesktopCategoryCache || {
      ready:false,
      loading:false,
      rows:[],
      categories:[]
    };
    window.__mcDishDesktopCategoryCache = cache;

    function renderOptions(){
      select.innerHTML =
        '<option value="">Toutes les catégories</option>' +
        cache.categories.map(function(category){
          return '<option value="' + mcEscape(category) + '">' +
            mcEscape(category) +
          '</option>';
        }).join('');
    }

    function applyCategory(){
      var wantedLabel = clean(select.value);
      var wanted = norm(wantedLabel);

      if (!wanted) {
        restoreOriginalPage();
        result.textContent = 'Toutes les catégories';
        return;
      }

      if (!cache.ready) return;

      var filtered = cache.rows.filter(function(item){
        return norm(item.category) === wanted;
      });

      showRows(filtered);

      /* Le résultat filtré contient déjà les plats de TOUTES les pages,
         donc la pagination SQLAdmin native n'a plus de sens. */
      var liveFooter = card.querySelector('.card-footer');
      if (liveFooter) liveFooter.style.display = 'none';

      result.textContent =
        filtered.length +
        (filtered.length > 1 ? ' plats affichés' : ' plat affiché');

      empty.style.display = filtered.length === 0 ? 'block' : 'none';
    }

    function loadAllDishes(){
      if (cache.ready) {
        renderOptions();
        result.textContent = cache.rows.length + ' plats disponibles';
        return;
      }

      if (cache.loading) return;
      cache.loading = true;

      var url = new URL(window.location.href);
      url.searchParams.delete('search');

      /* IMPORTANT:
         Ton SQLAdmin utilise `pageSize` (ex: ?pageSize=25&page=2),
         pas `page_size`. Si on laisse pageSize=25, le serveur ne renvoie
         que 25 plats et le filtre reste limité à une page.
      */
      url.searchParams.delete('page_size');
      url.searchParams.set('pageSize', '1000');
      url.searchParams.set('page', '1');

      fetch(url.toString(), {
        method:'GET',
        credentials:'same-origin',
        headers:{'X-Requested-With':'XMLHttpRequest'}
      })
      .then(function(response){
        if (!response.ok) throw new Error('Impossible de charger tous les plats.');
        return response.text();
      })
      .then(function(htmlText){
        var doc = new DOMParser().parseFromString(htmlText, 'text/html');
        var sourceTable = doc.querySelector('.table-responsive table');
        if (!sourceTable) throw new Error('Table Plats introuvable.');

        cache.rows = extractRows(sourceTable);

        var categoryMap = {};
        cache.rows.forEach(function(item){
          if (item.category) categoryMap[item.category] = true;
        });

        cache.categories = Object.keys(categoryMap).sort(function(a,b){
          return a.localeCompare(b, 'fr', {sensitivity:'base'});
        });

        cache.ready = true;
        cache.loading = false;

        renderOptions();
        result.textContent = cache.rows.length + ' plats disponibles';
      })
      .catch(function(error){
        console.error('Miss Chawarma desktop category filter:', error);
        cache.loading = false;

        /* Fallback: catégories de la page visible */
        cache.rows = extractRows(table);

        var fallbackMap = {};
        cache.rows.forEach(function(item){
          if (item.category) fallbackMap[item.category] = true;
        });

        cache.categories = Object.keys(fallbackMap).sort(function(a,b){
          return a.localeCompare(b, 'fr', {sensitivity:'base'});
        });

        cache.ready = true;
        renderOptions();
        result.textContent = cache.rows.length + ' plats chargés';
      });
    }

    select.addEventListener('change', applyCategory);

    reset.addEventListener('click', function(){
      select.value = '';
      restoreOriginalPage();

      var liveFooter = card.querySelector('.card-footer');
      if (liveFooter) liveFooter.style.display = originalFooterDisplay;

      result.textContent = 'Toutes les catégories';
    });

    loadAllDishes();
    mcApplyLanguage(filter);
  }

  /* =========================================================
     RECHERCHE À CHAQUE LETTRE SQLADMIN — sans rechargement de page
     Version robuste : intercepte TOUT clic dans la zone de recherche
     en phase capture, quel que soit le type d'élément (a, button,
     input[type=submit]) utilisé par SQLAdmin pour ses boutons.
  ========================================================= */

  function mcInitLiveSearch() {
    var listPathPattern = /^\/admin\/[^/]+\/list\/?$/;
    if (!listPathPattern.test(window.location.pathname)) return;

    var originalInput = document.querySelector('input[name="search"]');
    if (!originalInput || originalInput.dataset.mcLiveSearchReady === "1") return;

    // Clone le champ pour supprimer TOUT écouteur natif de SQLAdmin
    // (ex: un submit direct via form.submit() qui ignore preventDefault
    // car il ne passe pas par l'événement "submit").
    var searchInput = originalInput.cloneNode(true);
    originalInput.parentNode.replaceChild(searchInput, originalInput);

    // Supprime tout gestionnaire inline hérité du HTML natif de SQLAdmin
    // (ex: oninput="this.form.submit()"), que cloneNode() conserve tel quel
    // car ce sont des attributs HTML, pas des écouteurs addEventListener().
    ["oninput", "onchange", "onkeyup", "onkeypress", "onkeydown", "onclick"].forEach(function (attr) {
      searchInput.removeAttribute(attr);
    });
    searchInput.oninput = null;
    searchInput.onchange = null;
    searchInput.onkeyup = null;
    searchInput.onkeypress = null;
    searchInput.onkeydown = null;

    var searchForm = searchInput.closest("form");
    if (searchForm) {
      searchForm.removeAttribute("onsubmit");
      searchForm.onsubmit = null;
    }

    searchInput.dataset.mcLiveSearchReady = "1";
    searchInput.setAttribute(
      "placeholder",
      mcCurrentLang()==="en"
        ? "Search by name, email, phone…"
        : "Rechercher par nom, email, téléphone…"
    );

    var activeController = null;
    var lastRequestedValue = searchInput.value || "";

    function setLoading(isLoading) {
      var card = searchInput.closest(".card");
      if (!card) return;
      card.classList.toggle("mc-live-search-loading", isLoading);
      searchInput.setAttribute("aria-busy", isLoading ? "true" : "false");
    }

    function replaceResults(htmlText, requestedUrl) {
      var parser = new DOMParser();
      var nextDocument = parser.parseFromString(htmlText, "text/html");

      var currentTable = document.querySelector(".table-responsive");
      var nextTable = nextDocument.querySelector(".table-responsive");
      var currentFooter = document.querySelector(".card-footer");
      var nextFooter = nextDocument.querySelector(".card-footer");

      if (!currentTable || !nextTable) {
        throw new Error("Le tableau SQLAdmin est introuvable.");
      }

      // Sauvegarde le focus et la position du curseur AVANT toute
      // manipulation du DOM, pour les restaurer juste après — le champ
      // recherche n'est jamais retiré du DOM, mais certains navigateurs
      // déplacent le focus lors d'un remplacement de nœuds voisins.
      var hadFocus = document.activeElement === searchInput;
      var selectionStart = searchInput.selectionStart;
      var selectionEnd = searchInput.selectionEnd;

      currentTable.replaceWith(nextTable);

      if (currentFooter && nextFooter) {
        currentFooter.replaceWith(nextFooter);
      } else if (!currentFooter && nextFooter) {
        var currentCard = document.querySelector(".card");
        if (currentCard) currentCard.appendChild(nextFooter);
      }

      history.replaceState({}, "", requestedUrl);

      // Ne traduit QUE le nouveau contenu inséré — jamais tout le document,
      // ce qui évite de toucher au champ recherche ou à d'autres éléments
      // actifs pendant que l'utilisateur tape.
      mcApplyLanguage(nextTable);
      if (nextFooter) mcApplyLanguage(nextFooter);
      mcInitMobileTableCards(document);

      /* Le tableau vient d'être remplacé par la recherche :
         on reconstruit aussi le filtre desktop. */
      var currentCard = nextTable.closest('.card');
      if (currentCard) {
        currentCard.dataset.mcDishDesktopFilterReady = '';
        var oldDesktopFilter = currentCard.querySelector('.mc-dish-desktop-filters');
        if (oldDesktopFilter) oldDesktopFilter.remove();
        var oldDesktopEmpty = currentCard.querySelector('.mc-dish-desktop-empty');
        if (oldDesktopEmpty) oldDesktopEmpty.remove();
      }
      mcInitDishDesktopFilters();

      if (hadFocus) {
        searchInput.focus();
        if (typeof selectionStart === "number" && typeof selectionEnd === "number") {
          searchInput.setSelectionRange(selectionStart, selectionEnd);
        }
      }
    }

    function buildSearchUrl(value) {
      var url = new URL(window.location.href);
      url.searchParams.set("search", value);
      url.searchParams.delete("page");
      return url;
    }

    function runSearch() {
      var value = searchInput.value.trim();

      if (activeController) activeController.abort();
      activeController = new AbortController();

      var url = buildSearchUrl(value);
      lastRequestedValue = value;
      setLoading(true);

      fetch(url.toString(), {
        method: "GET",
        credentials: "same-origin",
        headers: { "X-Requested-With": "XMLHttpRequest" },
        signal: activeController.signal
      })
      .then(function (response) {
        if (!response.ok) throw new Error("La recherche a échoué.");
        return response.text();
      })
      .then(function (htmlText) {
        // Ignore une ancienne réponse arrivée après une saisie plus récente.
        if (searchInput.value.trim() !== lastRequestedValue) return;
        replaceResults(htmlText, url.toString());
      })
      .catch(function (error) {
        if (error.name === "AbortError") return;
        console.error("Miss Chawarma live search:", error);
      })
      .finally(function () {
        setLoading(false);
        if (document.activeElement !== searchInput) {
          searchInput.focus();
        }
      });
    }

    // Recherche à chaque frappe — déclenchement immédiat, sans bouton.
    searchInput.addEventListener("input", runSearch);

    // Filet de sécurité : empêche toute soumission native du formulaire
    // (touche Entrée incluse).
    if (searchForm) {
      searchForm.addEventListener("submit", function (event) {
        event.preventDefault();
        runSearch();
      });
    }

    // Intercepte TOUT clic dans la zone de recherche — bouton, lien, icône —
    // avant que le navigateur ne déclenche sa propre navigation native.
    // C'est le filet de sécurité principal : peu importe la balise exacte
    // utilisée par SQLAdmin pour son bouton "Search" ou son bouton "X".
    document.addEventListener("click", function (event) {
      var card = searchInput.closest(".card");
      if (!card || !card.contains(event.target)) return;

      var clickable = event.target.closest("a, button, input[type='submit']");
      if (!clickable) return;
      if (clickable === searchInput) return;

      event.preventDefault();
      event.stopImmediatePropagation();

      // Si c'est le bouton d'effacement (X), vide le champ avant de relancer.
      var text = (clickable.textContent || "").trim().toLowerCase();
      var isClearButton =
        clickable.matches('a[href*="search="], .btn-close, [aria-label="Clear"]') ||
        text === "×" || text === "x" || text === "clear";

      if (isClearButton) {
        searchInput.value = "";
      }

      searchInput.focus();
      runSearch();
    }, true);
  }


  /* =========================================================
     TABLE RESERVATION FORM
     Hide the internal "Slots" relation field from create/edit.
  ========================================================= */
  function mcHideTableReservationSlots(){
    var path = window.location.pathname.toLowerCase();

    var isTableReservationForm =
      path.indexOf('/admin/table-reservation/') !== -1 &&
      (path.indexOf('/edit') !== -1 || path.indexOf('/create') !== -1);

    if (!isTableReservationForm) return;

    var slotField = document.querySelector(
      'select[name="slots"], input[name="slots"], [name="slots"]'
    );

    if (slotField) {
      var wrapper =
        slotField.closest('.mb-3') ||
        slotField.closest('.form-group') ||
        slotField.closest('.col-md-12') ||
        slotField.closest('.col-12') ||
        slotField.parentElement;

      if (wrapper) {
        wrapper.remove();
        return;
      }
    }

    /* Fallback for SQLAdmin variants where the field name is not exposed
       directly but the visible label is "Slots". */
    document.querySelectorAll('label').forEach(function(label){
      if ((label.textContent || '').trim().toLowerCase() !== 'slots') return;

      var wrapper =
        label.closest('.mb-3') ||
        label.closest('.form-group') ||
        label.closest('.col-md-12') ||
        label.closest('.col-12') ||
        label.parentElement;

      if (wrapper) wrapper.remove();
    });
  }


  function init(){
    mcBuildCustomSidebar();
    createTopbar();
    initMobileNav();
    mcHideTableReservationSlots();
    renderDashboard();
    mcInitLiveSearch();
    mcInitMobileTableCards(document);
    mcInitDishDesktopFilters();
    window.addEventListener('resize', function(){
      if (window.innerWidth <= 575.98) {
        document.querySelectorAll('.mc-dish-desktop-filters,.mc-dish-desktop-empty').forEach(function(el){
          el.remove();
        });
        document.querySelectorAll('.card').forEach(function(el){
          el.dataset.mcDishDesktopFilterReady = '';
        });
        mcInitMobileTableCards(document);
      } else {
        document.querySelectorAll('.mc-mobile-cards,.mc-dish-filters,.mc-dish-no-results').forEach(function(el){
          el.remove();
        });
        document.querySelectorAll('.card.mc-mobile-card-mode').forEach(function(el){
          el.classList.remove('mc-mobile-card-mode');
        });
        mcInitDishDesktopFilters();
      }
    });
    // Traduit aussi les pages de liste SQLAdmin natives (Plats, Commandes, etc.)
    // qui ne passent pas par renderDashboard.
    if (location.pathname.replace(/\/+$/,'') !== '/admin') {
      mcApplyLanguage(document.body);
    }
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''


class AdminBrandMiddleware:
    """Injecte le thème dans toutes les pages HTML sous /admin."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        path = scope.get("path", "")
        if (
            scope.get("type") != "http"
            or not (path == "/admin" or path.startswith("/admin/"))
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
            headers = list(response_start.get("headers", [])) if response_start else []
            content_type = next(
                (v.decode("latin-1").lower() for k, v in headers if k.lower() == b"content-type"),
                "",
            )

            if "text/html" in content_type and b"</head>" in body:
                body = body.replace(
                  b"</head>",
                  MISS_CHAWARMA_ADMIN_CSS.encode("utf-8")
                  + ORDER_TICKET_MODAL_HTML.encode("utf-8")
                  + MISS_CHAWARMA_ADMIN_SCRIPT.encode("utf-8")
                  + b"</head>",
                  1,
               )
                headers = [(k, v) for k, v in headers if k.lower() != b"content-length"]
                headers.append((b"content-length", str(len(body)).encode("ascii")))

            if response_start:
                response_start["headers"] = headers
                await send(response_start)
            await send({"type": "http.response.body", "body": body, "more_body": False})

        await self.app(scope, receive, capture_send)
