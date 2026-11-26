/* motion.js · v2 · transición de página + entradas escalonadas entre secciones */
(function(){
  var d=document,root=d.documentElement;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce)return;
  root.classList.add('js-m');
  // cortina
  var wipe=d.createElement('div');wipe.className='m-wipe';
  function ready(fn){d.readyState!=='loading'?fn():d.addEventListener('DOMContentLoaded',fn)}
  ready(function(){
    d.body.appendChild(wipe);
    requestAnimationFrame(function(){requestAnimationFrame(function(){wipe.classList.add('is-open')})});
    mark();observe();
  });
  addEventListener('pageshow',function(e){if(e.persisted){wipe.className='m-wipe is-open'}});
  // objetivos de entrada
  var SEL=[
    '.section-subtitle','.section-title','.section-desc','.overview-text > *','.meta2','.tag-list','.software-used',
    '.alx-k','.alx-quote','.alx-p','.alx-team','.alx-idcard','.alx-stat','.alx-bento figure','.alx-chip','.mx-dev','.cta2',
    '.section > h2','.section > p','.section > .grid > *','.section figure','.section .card','.gallery > *','.grid > *',
    '#sobre .container > *','#proceso .container > *','#servicios h2','#servicios .section-sub','#proyectos-carousel h2'
  ].join(',');
  function mark(){
    var seen=new Set(),groups=new Map();
    d.querySelectorAll(SEL).forEach(function(el){
      if(seen.has(el)||el.closest('.pjx,header,nav,.m-wipe,#previews,.ptabs,.hero-banner,#hero,.mw'))return;
      seen.add(el);
      var type=/title|^H[12]$/.test(el.className+el.tagName)?'line':(el.tagName==='FIGURE'||/bento|alx-idcard|mx-dev/.test(el.className+el.parentNode.className)?'img':'');
      el.setAttribute('data-m',type||'fade');
      var p=el.parentNode,n=groups.get(p)||0;groups.set(p,n+1);
      el.style.setProperty('--i',Math.min(n,7));
    });
  }
  function observe(){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('m-in');io.unobserve(e.target)}});
    },{threshold:.12,rootMargin:'0px 0px -6% 0px'});
    d.querySelectorAll('[data-m]').forEach(function(el){io.observe(el)});
    // contadores
    var co=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting)return;co.unobserve(e.target);
        var el=e.target,end=+el.dataset.count,t0=performance.now(),dur=1400;
        (function tick(t){var k=Math.min(1,(t-t0)/dur),v=1-Math.pow(1-k,4);el.textContent=Math.round(end*v);if(k<1)requestAnimationFrame(tick)})(t0);
      });
    },{threshold:.6});
    d.querySelectorAll('[data-count]').forEach(function(el){co.observe(el)});
  }
  // salir de la página con cortina
  d.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]');
    if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    if(a.target&&a.target!=='_self')return;
    var u;try{u=new URL(a.href,location.href)}catch(_){return}
    if(u.origin!==location.origin||!/\.html$|\/$/.test(u.pathname)||u.pathname===location.pathname)return;
    e.preventDefault();
    wipe.className='m-wipe is-ready';void wipe.offsetWidth;
    wipe.className='m-wipe is-closing is-covering';
    setTimeout(function(){location.href=u.href},560);
  });
})();
