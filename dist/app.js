const siteHeader=document.querySelector('.header');
const headerSentinel=document.querySelector('.header-sentinel');
// The homepage overlays the photo only when scroll-state enhancement is ready.
// Missing JavaScript or observer support leaves a readable white sticky header.
if(siteHeader&&headerSentinel&&'IntersectionObserver' in window){
  siteHeader.classList.toggle('is-scrolled',window.scrollY>48);
  document.body.classList.add('nav-enhanced');
  new IntersectionObserver(([entry])=>{
    siteHeader.classList.toggle('is-scrolled',!entry.isIntersecting&&entry.boundingClientRect.top<0);
  }).observe(headerSentinel);
  // Paint the transparent initial state before enabling scroll/menu fades.
  requestAnimationFrame(()=>requestAnimationFrame(()=>siteHeader.classList.add('nav-ready')));
}
const menuButton=document.querySelector('.menu-toggle');
const navigation=document.querySelector('.navlinks');
const serviceNav=document.querySelector('.services-nav');
const serviceToggle=document.querySelector('.services-toggle');
const servicePanel=document.querySelector('.services-panel');
const desktopNav=window.matchMedia('(min-width: 1200px)');
const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
let serviceCloseTimer;
let servicePinned=false;
function setServices(open){clearTimeout(serviceCloseTimer);if(!open)servicePinned=false;serviceToggle?.setAttribute('aria-expanded',String(open));serviceToggle?.setAttribute('aria-label',open?'Hide electrical services':'Show electrical services');if(servicePanel)servicePanel.hidden=!open;}
function setMenu(open){menuButton?.setAttribute('aria-expanded',String(open));menuButton?.setAttribute('aria-label',open?'Close navigation':'Open navigation');navigation?.classList.toggle('open',open);siteHeader?.classList.toggle('menu-open',open);const label=menuButton?.querySelector('.menu-label');if(label)label.textContent=open?'Close':'Menu';if(!open)setServices(false);}
menuButton?.addEventListener('click',()=>setMenu(menuButton.getAttribute('aria-expanded')!=='true'));
serviceToggle?.addEventListener('click',event=>{if(event.detail&&desktopNav.matches){servicePinned=!servicePinned;setServices(servicePinned);}else setServices(serviceToggle.getAttribute('aria-expanded')!=='true');});
serviceNav?.addEventListener('pointerenter',event=>{if(desktopNav.matches&&event.pointerType==='mouse')setServices(true);});
serviceNav?.addEventListener('pointerleave',()=>{if(desktopNav.matches&&!serviceNav.contains(document.activeElement))serviceCloseTimer=setTimeout(()=>setServices(false),150);});
serviceNav?.addEventListener('focusout',()=>{queueMicrotask(()=>{if(desktopNav.matches&&!serviceNav.contains(document.activeElement))setServices(false);});});
document.addEventListener('pointerdown',event=>{if(!serviceNav?.contains(event.target))setServices(false);if(!siteHeader?.contains(event.target))setMenu(false);});
navigation?.addEventListener('click',event=>{if(event.target.closest('a'))setMenu(false);});
document.addEventListener('keydown',event=>{if(event.key!=='Escape')return;if(serviceToggle?.getAttribute('aria-expanded')==='true'){setServices(false);serviceToggle.focus();}else if(menuButton?.getAttribute('aria-expanded')==='true'){setMenu(false);menuButton.focus();}});
desktopNav.addEventListener('change',()=>{setMenu(false);setServices(false);});

// One anchor coordinator. Real hrefs preserve direct entry and modified clicks.
document.querySelectorAll('a[href^="#"],.brand[href="/"]').forEach(link=>link.addEventListener('click',event=>{
  if(event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  const href=link.getAttribute('href');
  if(href==='/'&&!document.body.classList.contains('home-page'))return;
  const target=href==='/'?document.body:document.querySelector(href);
  if(!target)return;
  event.preventDefault();
  const behavior=event.detail&&!reducedMotion.matches?'smooth':'instant';
  if(href==='/')window.scrollTo({top:0,behavior});
  else {const top=target.getBoundingClientRect().top+window.scrollY-(siteHeader?.getBoundingClientRect().height||0)-16;target.focus({preventScroll:true});window.scrollTo({top:Math.max(0,top),behavior});}
}));

// A manual, native scroll-snap gallery. Swipe/keyboard work without a timer.
document.querySelectorAll('.project-slider').forEach(slider=>{
  const track=slider.querySelector('.gallery-track');
  const cards=[...track.children];
  const controls=slider.querySelector('.carousel-controls');
  const previous=slider.querySelector('.carousel-prev');
  const next=slider.querySelector('.carousel-next');
  const status=slider.querySelector('.carousel-status');
  slider.classList.add('is-enhanced');
  let index=0;
  const step=()=>cards[0]?.getBoundingClientRect().width+parseFloat(getComputedStyle(track).columnGap);
  function update(){const stride=step();if(!stride)return;index=Math.round(track.scrollLeft/stride);const visible=Math.max(1,Math.round((track.clientWidth+parseFloat(getComputedStyle(track).columnGap))/stride));previous.disabled=index===0;next.disabled=track.scrollLeft>=track.scrollWidth-track.clientWidth-2;status.textContent=`${index+1}${visible>1?' to '+Math.min(index+visible,cards.length):''} of ${cards.length}`;}
  function move(direction,event){const stride=step();const goal=Math.max(0,Math.min(track.scrollWidth-track.clientWidth,(Math.round(track.scrollLeft/stride)+direction)*stride));track.scrollTo({left:goal,behavior:event.detail&&!reducedMotion.matches?'smooth':'instant'});}
  previous.addEventListener('click',event=>move(-1,event));
  next.addEventListener('click',event=>move(1,event));
  controls.hidden=cards.length<2;
  if('IntersectionObserver' in window){const observer=new IntersectionObserver(update,{root:track,threshold:[.5,.95]});cards.forEach(card=>observer.observe(card));}
  if('ResizeObserver' in window)new ResizeObserver(update).observe(track);
  track.addEventListener('scrollend',update);
  reducedMotion.addEventListener('change',()=>{track.scrollTo({left:track.scrollLeft,behavior:'instant'});update();});
  update();
});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{const category=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));let count=0;document.querySelectorAll('.gallery-grid > [data-category]').forEach(card=>{card.hidden=category!=='All'&&card.dataset.category!==category;if(!card.hidden)count++;});document.querySelector('.gallery-count').textContent=`${count} projects`; }));
const lightbox=document.querySelector('.lightbox');
let currentProject=0;let currentSet=[];let previousFocus;
function showProject(index){currentProject=(index+currentSet.length)%currentSet.length;const item=currentSet[currentProject];lightbox.querySelector('img').src=item.dataset.image;lightbox.querySelector('img').alt=item.dataset.title;lightbox.querySelector('h2').textContent=item.dataset.title;lightbox.querySelector('.lightbox-count').textContent=`${currentProject+1} of ${currentSet.length} · ${item.dataset.category}`;}
document.querySelectorAll('.project-open').forEach(button=>button.addEventListener('click',e=>{if(e.button!==0||e.ctrlKey||e.metaKey||e.shiftKey||e.altKey||!lightbox?.showModal)return;e.preventDefault();previousFocus=button;currentSet=[...document.querySelectorAll('.project-open')].filter(b=>!b.closest('[hidden]'));showProject(currentSet.indexOf(button));lightbox.showModal();}));
lightbox?.querySelector('.lightbox-close').addEventListener('click',()=>lightbox.close());
lightbox?.querySelector('.lightbox-prev').addEventListener('click',()=>showProject(currentProject-1));
lightbox?.querySelector('.lightbox-next').addEventListener('click',()=>showProject(currentProject+1));
lightbox?.addEventListener('close',()=>previousFocus?.focus());
lightbox?.addEventListener('click',e=>{if(e.target===lightbox){const r=lightbox.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)lightbox.close();}});
lightbox?.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();showProject(currentProject+1);}if(e.key==='ArrowLeft'){e.preventDefault();showProject(currentProject-1);}});
const quoteForm=document.querySelector('#quote-form');
if(quoteForm){const select=quoteForm.querySelector('[name=service]');const selected=new URLSearchParams(location.search).get('service');if(selected&&[...select.options].some(o=>o.value===selected))select.value=selected;quoteForm.addEventListener('submit',async e=>{e.preventDefault();if(!quoteForm.reportValidity())return;const data=new FormData(quoteForm);const summary=`Free quote request: Montesinos Electric\n\nName: ${data.get('name')}\nPhone: ${data.get('phone')}\nEmail: ${data.get('email')||'Not provided'}\nProject location: ${data.get('location')}\nService: ${select.selectedOptions[0].textContent}\n\nProject details:\n${data.get('details')}`;const result=document.querySelector('#quote-result');result.querySelector('textarea').value=summary;result.hidden=false;result.scrollIntoView({behavior:'auto',block:'center'});result.querySelector('h3').focus();});
document.querySelector('#copy-request').addEventListener('click',async()=>{const summary=document.querySelector('#request-summary');const status=document.querySelector('#copy-status');try{await navigator.clipboard.writeText(summary.value);status.textContent='Copied. You can paste your project details wherever you choose.';}catch{summary.focus();summary.select();status.textContent='Select and copy the highlighted details to share your request.';}});}
