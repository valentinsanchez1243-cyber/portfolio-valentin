/* motion.js · salida suave entre páginas */
(function(){
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  addEventListener('pageshow',function(){document.documentElement.classList.remove('vs-leaving');});
  if(reduce)return;
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]');
    if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    if(a.target&&a.target!=='_self')return;
    var u;try{u=new URL(a.href,location.href);}catch(_){return;}
    if(u.origin!==location.origin||!/\.html$|\/$/.test(u.pathname))return;
    if(u.pathname===location.pathname)return;
    e.preventDefault();
    document.documentElement.classList.add('vs-leaving');
    setTimeout(function(){location.href=u.href;},320);
  });
})();
