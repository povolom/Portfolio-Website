// Menu, nav bar shade, and the click animations: button ripples, copy email,
// "coming soon" toasts, opening panels and the build-stage switcher.
document.documentElement.classList.add('js');
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;

const menu = document.querySelector('.menu');
const nav = document.querySelector('#navigation');
function setMenu(open) {
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  nav.classList.toggle('open', open);
  document.body.classList.toggle('menu-open', open);
  if (open) setTimeout(() => nav.querySelector('a')?.focus({ preventScroll: true }), 80);
}
menu?.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
nav?.addEventListener('click', e => { if (e.target.closest('a') && menu.getAttribute('aria-expanded') === 'true') setMenu(false); });
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') { setMenu(false); menu.focus(); }
});
// Leaving phone width with the menu open shouldn't leave the page locked.
matchMedia('(max-width: 700px)').addEventListener('change', e => { if (!e.matches) setMenu(false); });

// Phones: "Read the full story" on project pages, "Show all" on long lists.
document.querySelectorAll('.story-toggle').forEach(b => b.addEventListener('click', () => {
  b.setAttribute('aria-expanded', 'true');
  b.closest('.p-story').classList.add('story-open');
}));
document.querySelectorAll('.show-all').forEach(b => b.addEventListener('click', () => {
  b.setAttribute('aria-expanded', 'true');
  b.closest('.clip').classList.add('open');
}));

const bar = document.querySelector('.nav-bar');
const shade = () => bar?.classList.toggle('scrolled', scrollY > 8);
addEventListener('scroll', shade, { passive: true }); shade();

// Ripple from the point you pressed.
document.addEventListener('pointerdown', e => {
  const b = e.target.closest('.pill, .btn2');
  if (!b || still) return;
  const r = b.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2.2;
  const s = document.createElement('span');
  s.className = 'ripple';
  s.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
  b.appendChild(s);
  s.addEventListener('animationend', () => s.remove());
});

// A small message that slides up from the bottom.
let toastTimer;
function toast(msg) {
  let t = document.querySelector('.toast');
  if (!t) { t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
  t.textContent = msg; t.classList.add('show');
  clearTimeout(toastTimer); toastTimer = setTimeout(() => t.classList.remove('show'), 2600);
}
document.querySelectorAll('[data-toast]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); toast(b.dataset.toast); }));

// Copy the email address, with a tick.
document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(b.dataset.copy); } catch { /* clipboard blocked: the toast still says what to copy */ }
  const label = b.querySelector('span'), was = label.textContent;
  b.classList.add('done'); label.textContent = 'Copied';
  toast(`${b.dataset.copy} copied`);
  setTimeout(() => { b.classList.remove('done'); label.textContent = was; }, 2000);
}));

// Panels that open and close.
document.querySelectorAll('.disclose > button').forEach(btn => btn.addEventListener('click', () => {
  const open = btn.getAttribute('aria-expanded') !== 'true';
  btn.setAttribute('aria-expanded', String(open));
  btn.parentElement.classList.toggle('open', open);
}));

// Build stages: the highlight slides to the stage you pick and its card swaps in.
document.querySelectorAll('.segments').forEach(seg => {
  const glider = seg.querySelector('.seg-glider');
  const tabs = [...seg.querySelectorAll('[role="tab"]')];
  const move = t => { glider.style.width = t.offsetWidth + 'px'; glider.style.transform = `translateX(${t.offsetLeft - 4}px)`; };
  function pick(t, focus) {
    tabs.forEach(x => {
      const on = x === t;
      x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).classList.toggle('on', on);
    });
    move(t); if (focus) t.focus();
    t.scrollIntoView({ block: 'nearest', inline: 'center', behavior: still ? 'auto' : 'smooth' });
  }
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => pick(t));
    t.addEventListener('keydown', e => {
      const n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
      if (n !== null) { e.preventDefault(); pick(tabs[(n + tabs.length) % tabs.length], true); }
    });
  });
  const first = tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0];
  glider.style.transition = 'none'; move(first);
  requestAnimationFrame(() => { glider.style.transition = ''; });
  addEventListener('resize', () => move(tabs.find(t => t.getAttribute('aria-selected') === 'true')));
});
