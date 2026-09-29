document.documentElement.classList.add('js');
const menu=document.querySelector('.menu');const nav=document.querySelector('#navigation');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.setAttribute('aria-label',open?'Close menu':'Open menu');});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){menu.click();menu.focus();}});
// Demo window: buttons with data-demo open that page in a framed window on top of this one.
const demoButtons=document.querySelectorAll('[data-demo]');
if(demoButtons.length){
const dlg=document.createElement('dialog');dlg.className='demo-window';dlg.setAttribute('aria-labelledby','demo-title');
dlg.innerHTML='<div class="demo-bar"><span class="demo-dots" aria-hidden="true"><i></i><i></i><i></i></span><strong id="demo-title"></strong><a class="demo-open" target="_blank" rel="noopener noreferrer">Open in new tab <svg class="arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5 11 11 5M6 5h5v5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a><button class="demo-close" type="button">Close</button></div><iframe></iframe>';
document.body.append(dlg);
const frame=dlg.querySelector('iframe'),title=dlg.querySelector('#demo-title'),openLink=dlg.querySelector('.demo-open');
demoButtons.forEach(b=>b.addEventListener('click',()=>{title.textContent=b.dataset.demoTitle;frame.title=b.dataset.demoTitle+' demo';openLink.href=b.dataset.demoFull;frame.src=b.dataset.demo;dlg.showModal();}));
dlg.querySelector('.demo-close').addEventListener('click',()=>dlg.close());
dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close();});
dlg.addEventListener('close',()=>{frame.src='about:blank';});
}
