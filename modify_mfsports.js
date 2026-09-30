const fs = require('fs');

let c = fs.readFileSync('mfsports.html', 'utf8');

let html = '<!-- GALERIA DE PRODUCTOS -->\n';
html += '  <section class="reveal" style="padding: 60px 64px; max-width: 1200px; margin: 0 auto;">\n';
html += '    <div class="section-subtitle" style="font-family: \'Barlow Condensed\', sans-serif; font-size: 11px; letter-spacing: 4px; text-transform: uppercase; color: var(--rb); margin-bottom: 12px;">— INDUMENTARIA</div>\n';
html += '    <h2 class="section-title">GALERÍA</h2>\n';
html += '    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 24px;">\n';

for (let i = 1; i <= 47; i++) {
    html += '      <img src="https://valentin-cdn.b-cdn.net/' + i + '.png" style="width: 100%; border-radius: 8px; object-fit: contain; aspect-ratio: 1/1; background: #111;" loading="lazy" alt="MF Sports ' + i + '">\n';
}

html += '    </div>\n';
html += '  </section>\n';
html += '  \n';
html += '  <section class="reveal" style="padding: 60px 64px; max-width: 1200px; margin: 0 auto;">\n';
html += '    <div class="pdf-showcase" style="margin: 40px 0 60px; border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; overflow: hidden; background: #0d0d0d;">\n';
html += '      <div class="pdf-showcase-hd" style="padding: 14px 24px; border-bottom: 1px solid rgba(255,255,255,0.06); display: flex; flex-direction: column; gap: 3px;">\n';
html += '        <span class="pdf-showcase-title" style="font-family: \'Bebas Neue\', sans-serif; font-size: 1rem; letter-spacing: 5px; color: var(--rb);">SPONSOR KIT</span>\n';
html += '        <span class="pdf-showcase-sub" style="font-family: \'Barlow Condensed\', sans-serif; font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.35);">MF Sports</span>\n';
html += '      </div>\n';
html += '      <iframe src="https://valentin-cdn.b-cdn.net/MF%20sports-Sponsor.pdf#toolbar=0" class="proj-pdf-frame" style="width: 100%; height: 700px; border: none; display: block; background: #111;" title="MF Sports Sponsor Kit"></iframe>\n';
html += '    </div>\n';
html += '  </section>';

c = c.replace(/<!-- CARRUSEL DE VIDEOS -->[\s\S]*?<\/section>/, html);

fs.writeFileSync('mfsports.html', c);
console.log('Done mapping mfsports!');
