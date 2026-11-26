/* Modo claro / oscuro: recuerda la elección y la aplica antes de pintar */
(function () {
  var K = 'vs-theme', root = document.documentElement;
  function read() { try { return localStorage.getItem(K); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(K, v); } catch (e) {} }
  function apply(v) {
    if (v === 'light') root.setAttribute('data-theme', 'light'); else root.removeAttribute('data-theme');
    var on = v === 'light';
    [].forEach.call(document.querySelectorAll('.vs-theme'), function (b) {
      b.setAttribute('aria-checked', on ? 'true' : 'false');
      b.setAttribute('title', on ? 'Cambiar a modo oscuro' : 'Cambiar a modo claro');
    });
  }
  apply(read() === 'light' ? 'light' : 'dark');
  function make(cls) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'vs-theme ' + (cls || ''); b.setAttribute('role', 'switch');
    b.setAttribute('aria-label', 'Modo claro u oscuro');
    b.innerHTML = '<svg class="vt-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="vt-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg><span class="vt-k"></span>';
    b.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      save(next); apply(next);
    });
    return b;
  }
  function mount() {
    var ul = document.querySelector('.nls');
    if (ul && !ul.querySelector('.vs-theme')) {
      var li = document.createElement('li'); li.className = 'vs-theme-li'; li.appendChild(make('vs-theme-desk'));
      if (ul.firstElementChild) ul.firstElementChild.insertAdjacentElement('afterend', li); else ul.appendChild(li);
    }
    var tog = document.querySelector('.mtog');
    if (tog && !document.querySelector('.vs-theme-mob')) tog.parentNode.insertBefore(make('vs-theme-mob'), tog);
    apply(root.getAttribute('data-theme') === 'light' ? 'light' : 'dark');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
