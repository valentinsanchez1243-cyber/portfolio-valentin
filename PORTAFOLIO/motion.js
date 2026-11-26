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

  // Mi trabajo en acción: ajusta cada pestaña para que contenido + secuencia entren en pantalla
  function fitTabs(){
    if(innerWidth<=1000)return;
    d.querySelectorAll('#previews .ptab-body').forEach(function(b){
      var i=b.firstElementChild;if(!i||!b.offsetParent)return;
      i.style.transform='none';i.style.margin='0';i.style.maxHeight='none';
      var cs=getComputedStyle(b),av=b.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);
      var h=i.offsetHeight;
      if(h>av&&av>0){
        var k=Math.max(.42,av/h*.97),m=-(h*(1-k)/2);
        i.style.transformOrigin='center center';i.style.transform='scale('+k.toFixed(3)+')';i.style.margin=m.toFixed(1)+'px 0';
      }
    });
  }
  ready(function(){
    var pv=d.getElementById('previews');if(!pv)return;
    pv.addEventListener('click',function(){[150,500,1200,2500,4000].forEach(function(t){setTimeout(fitTabs,t)})},true);
    addEventListener('resize',fitTabs);addEventListener('load',function(){setTimeout(fitTabs,300)});
    pv.addEventListener('load',function(){setTimeout(fitTabs,100)},true);
  });

  // divisores animados entre secciones
  function dividers(){
    var secs=[].filter.call(d.querySelectorAll('section'),function(s){
      return !s.closest('#previews,.pjx,header')&&!s.parentElement.closest('section')&&!/hero/.test(s.id+s.className);
    });
    var total=secs.length;
    secs.forEach(function(s,k){
      var prev=s.previousElementSibling;if(prev&&prev.classList.contains('m-div'))return;
      var el=d.createElement('div');el.className='m-div';el.setAttribute('aria-hidden','true');
      var n=function(v){return (v<10?'0':'')+v};
      el.innerHTML='<i class="m-d-no">'+n(k+1)+'</i><span class="m-d-line"></span><i class="m-d-no">'+n(total)+'</i>';
      s.parentNode.insertBefore(el,s);
      el.setAttribute('data-mdiv','');
    });
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('m-in');io.unobserve(e.target)}})},{threshold:.5});
    d.querySelectorAll('.m-div').forEach(function(el){io.observe(el)});
  }
  ready(dividers);
  // cursor oscuro sobre bandas claras
  ready(function(){
    var c=d.getElementById('cursor');if(!c)return;
    var x=0,y=0;
    function tone(){var el=d.elementFromPoint(x,y),dk=!!(el&&el.closest&&el.closest('.m-tint'));c.classList.toggle('dark',dk);d.querySelectorAll('.trail').forEach(function(t){t.classList.toggle('dark',dk)})}
    addEventListener('mousemove',function(e){x=e.clientX;y=e.clientY;tone()},{passive:true});
    addEventListener('scroll',tone,{passive:true});
  });
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
