document.documentElement.classList.add('js');
const menu=document.querySelector('.menu');const nav=document.querySelector('#navigation');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.textContent=open?'Close':'Menu';});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){menu.click();menu.focus();}});
