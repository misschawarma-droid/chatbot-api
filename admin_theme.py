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
</style>
'''

ORDER_TICKET_MODAL_HTML = """
<style>
  .order-ticket-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(20, 30, 20, 0.55);
    z-index: 9999;
    align-items: center;
    justify-content: center;
  }
  .order-ticket-overlay.open {
    display: flex;
  }
  .order-ticket-modal {
    position: relative;
    width: 460px;
    max-width: 92vw;
    height: 85vh;
    background: #f7f0e4;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
  }
  .order-ticket-modal iframe {
    width: 100%;
    height: 100%;
    border: 0;
  }
  .order-ticket-close {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: #1f6b2d;
    color: white;
    border: none;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    z-index: 2;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
<div id="order-ticket-overlay" class="order-ticket-overlay">
  <div class="order-ticket-modal">
    <button class="order-ticket-close" onclick="closeOrderTicket()">&#10005;</button>
    <iframe id="order-ticket-iframe" src=""></iframe>
  </div>
</div>
<script>
  function openOrderTicket(orderId) {
    document.getElementById('order-ticket-iframe').src = '/order-ticket/' + orderId;
    document.getElementById('order-ticket-overlay').classList.add('open');
  }
  function closeOrderTicket() {
    document.getElementById('order-ticket-overlay').classList.remove('open');
    document.getElementById('order-ticket-iframe').src = '';
  }
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('.ticket-trigger');
    if (trigger) {
      e.preventDefault();
      openOrderTicket(trigger.dataset.orderId);
    }
    if (e.target.id === 'order-ticket-overlay') {
      closeOrderTicket();
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeOrderTicket();
  });
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


  function init(){
    createTopbar();
    initMobileNav();
    renderDashboard();
    mcInitLiveSearch();
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
