# PROMPT MAESTRO v2 — Portfolio Valentín Sánchez
# Ingeniero Senior — HTML/CSS/JS puro, Vercel deploy, Bunny CDN
# Fases: WOLDI + LLUVIA CON SOL + reestructurar index + homogeneizar REDES SOCIALES
# Ejecutar EN ORDEN. Cada fase termina con un check antes de avanzar.

---

## CONTEXTO TÉCNICO DEL REPO

Sitio estático HTML/CSS/JS puro sin frameworks, deployado en Vercel desde la subcarpeta `PORTAFOLIO/` del repo.
Vercel sirve **únicamente** los archivos dentro de `PORTAFOLIO/` — nunca toques archivos en la raíz.

**Stack:**
- Fuentes: `Bebas Neue`, `Barlow Condensed`, `Barlow` (Google Fonts)
- CDN assets: `https://valentin-cdn.b-cdn.net/` (pull zone pública, no auth)
- CSS compartido: `project-base.css` (nav, footer, cursor, reveal)
- Variables CSS en cada página: `--rb` (color acento), `--b` (fondo), `--w` (blanco), `--g` (gris)
- Patrón lazy video: `preload="none"` + `IntersectionObserver` en script al pie — NUNCA `preload="auto"`
- Patrón lazy PDF: `data-src` en iframe, cargado cuando viewport lo alcanza
- Mobile-only: todo override CSS va en `@media (max-width: 768px)` con `!important`. NUNCA tocar desktop layout

**Rama git:** `limpio` → push siempre como `git push origin limpio:main`

---

## REGLAS ABSOLUTAS

1. Solo modificar archivos dentro de `PORTAFOLIO/`
2. No tocar layout desktop — solo mobile en `@media (max-width: 768px)`
3. Usar EXACTAMENTE las URLs de Bunny que se listan abajo — no inventar ni modificar
4. Usar EXACTAMENTE los textos redactados — no reescribir ni resumir
5. Copiar el patrón de IntersectionObserver de `natan.html` para videos (ver abajo)
6. Copiar el patrón de PDF embed de `kord3.html` (desktop iframe `data-src` + mobile Google Docs viewer)
7. Al final de cada fase: `git add PORTAFOLIO/<archivos> && git commit -m "..." && git push origin limpio:main`

---

## ASSETS EN BUNNY CDN — URLs EXACTAS

### WOLDI
```
PORTADA:  https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-WOLDI.webp
VIDEO 1:  https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/TP4.mp4
VIDEO 2:  https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/video%20woldi.mp4
PDF:      https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/MANUAL%20DE%20MARCA-WOLDI.pdf
```

### LLUVIA CON SOL
```
PORTADA:  https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-LLLUEVE-CON-SOL.webp
          ⚠️ "LLLUEVE" con triple L — es el nombre real del archivo en Bunny, usarlo tal cual
VIDEO 1:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/0611.mov
VIDEO 2:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/0616%20(1).mov
VIDEO 3:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/0619.mov
VIDEO 4:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/0623%20(2).mov
VIDEO 5:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/0625.mov
VIDEO 6:  https://valentin-cdn.b-cdn.net/PROYECTOS/LLUVIA%20CON%20SOL/12.6.R.mov
          ⚠️ Son .mov — más pesados. Usarlos así por ahora, después se reemplazan por .mp4 solo cambiando extensión
```

---

## TEXTOS EXACTOS (no reescribir)

### WOLDI — descripción
```
Desarrollé la identidad de marca completa de WOLDI como trabajo práctico final de Diseño de Comunicación Visual II (Universidad Siglo 21, cátedra Camila Young Romanutti), junto a Tomás Bertona y Carmela Russo, actuando los tres como estudio de diseño. WOLDI es un emprendimiento gastronómico cordobés real —propio— especializado en sandwiches de bondiola desmenuzada para autoservicio de eventos, con proyección futura hacia catering, congelados y envasado al vacío.

El proceso arrancó con un brief exhaustivo relevando valores de marca, personalidad y público objetivo, seguido de un análisis de competencia que detectó un mercado saturado de recursos visuales literales. A partir de ahí encaramos un proceso de naming evaluando varias alternativas hasta llegar a WOLDI, fusión entre "Wol" y "bondi" (bondiola).

Con esa base construimos el sistema visual completo: logotipo, tipografías, paleta cromática e iconografía, sintetizando el pan tipo bollo con guiños sutiles al universo del lobo, evitando toda representación literal del producto para diferenciarnos de la competencia y ganar recordación de marca.
```
Tags WOLDI: `BRANDING` `NAMING` `SISTEMA VISUAL` `IDENTIDAD EDITORIAL`

Índice WOLDI:
- BRIEF & INVESTIGACIÓN → `#brief`
- NAMING → `#naming`
- SISTEMA VISUAL → `#sistema`
- PIEZAS APLICADAS → `#piezas`

### LLUVIA CON SOL — descripción
```
Trabajo como editor de video y diseñador de contenido para Lluvia con Sol, agencia de comunicación y marketing con base en Córdoba, en modalidad remota desde mayo de 2026. Me encargo de la edición de reels y videos para marcas locales de gastronomía, restaurantes y otros rubros, además del diseño de placas visuales y piezas gráficas para redes sociales, adaptando cada pieza al estilo y la identidad de marca de cada cliente. Trabajo de forma coordinada con la dirección de la agencia, cumpliendo tiempos de entrega y el estándar visual que exige cada cuenta.
```
Tags LLUVIA CON SOL: `EDICIÓN DE VIDEO` `DISEÑO GRÁFICO` `CONTENIDO PARA REDES` `GESTIÓN DE CUENTAS`

Índice LLUVIA CON SOL:
- REELS & VIDEOS → `#reels`
- PLACAS & DISEÑO GRÁFICO → `#placas` (pendiente, sin imágenes aún)
- HISTORIAS & CONTENIDO → `#historias` (pendiente, sin imágenes aún)

---

## PATRONES DE CÓDIGO A COPIAR EXACTAMENTE

### Patrón IntersectionObserver para videos (de natan.html — copiar al pie de cada página nueva)
```html
<script>
  const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const v = entry.target;
      if (entry.isIntersecting) {
        if (v.preload === 'none') { v.preload = 'auto'; v.load(); }
        v.play().catch(() => {});
      } else {
        v.pause();
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('video').forEach(v => {
    v.setAttribute('autoplay', '');
    v.setAttribute('muted', '');
    v.setAttribute('loop', '');
    v.setAttribute('playsinline', '');
    v.setAttribute('preload', 'none');
    videoObserver.observe(v);
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('vs', 'in');
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.rv, .reveal').forEach(el => revealObserver.observe(el));
</script>
```

### Patrón PDF embed (de kord3.html — desktop iframe lazy + mobile Google Docs viewer)
```html
<div class="pdf-showcase" style="border:1px solid rgba(255,255,255,0.08); border-radius:10px; overflow:hidden; background:#0d0d0d;">
  <div class="pdf-showcase-hd" style="padding:14px 24px; border-bottom:1px solid rgba(255,255,255,0.06); display:flex; flex-direction:column; gap:3px;">
    <span class="pdf-showcase-title" style="font-family:'Bebas Neue',sans-serif; font-size:1rem; letter-spacing:5px; color:var(--rb);">MANUAL DE MARCA</span>
    <span class="pdf-showcase-sub" style="font-family:'Barlow Condensed',sans-serif; font-size:0.68rem; letter-spacing:2px; text-transform:uppercase; color:rgba(255,255,255,0.35);">WOLDI</span>
  </div>
  <!-- Desktop -->
  <iframe data-src="TU_URL_PDF#toolbar=0" class="proj-pdf-frame pdf-desktop" style="width:100%; height:680px; border:none; display:block; background:#111;" title="Manual de Marca WOLDI"></iframe>
  <!-- Mobile -->
  <div class="pdf-mobile" style="display:none;">
    <iframe src="https://docs.google.com/viewer?url=TU_URL_PDF&embedded=true" style="width:100%; height:520px; border:none; display:block; background:#111;" title="Manual de Marca WOLDI Mobile"></iframe>
  </div>
</div>
```

CSS mobile para PDF (agregar en `@media (max-width: 768px)`):
```css
.pdf-desktop { display: none !important; }
.pdf-mobile { display: block !important; }
```

### Patrón hero-banner con color acento (copiar de kord3, cambiar color y portada)
```css
:root {
  --rb: #COLOR_ACENTO;   /* WOLDI: usar un tono cálido, ej #E8B84B (dorado). LLUVIA CON SOL: ej #38BDF8 (celeste) */
  --rb-rgb: R, G, B;
  --r: #COLOR_ACENTO;
  --b: #080808;
  --w: #ffffff;
  --g: #aaaaaa;
}

.hero-banner {
  background-image: url('URL_PORTADA');
  background-size: cover;
  background-position: center;
  /* resto igual que kord3 */
}
```

### Patrón grid de videos 2 columnas (para WOLDI — texto izquierda, videos derecha)
```html
<section class="reveal" style="padding: 60px 64px; max-width: 1200px; margin: 0 auto;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start;">
    <!-- Columna texto -->
    <div>
      <div class="section-subtitle" style="letter-spacing:6px;">— TRABAJO PRÁCTICO FINAL · SIGLO 21</div>
      <h2 class="section-title" style="margin-bottom:16px;">WOLDI<br><em>IDENTIDAD DE MARCA</em></h2>
      <p class="section-desc">TEXTO_WOLDI_EXACTO</p>
      <div class="tag-list" style="margin-top:18px;">
        <span class="tag">BRANDING</span>
        <span class="tag">NAMING</span>
        <span class="tag">SISTEMA VISUAL</span>
        <span class="tag">IDENTIDAD EDITORIAL</span>
      </div>
    </div>
    <!-- Columna videos -->
    <div style="display: flex; flex-direction: column; gap: 20px;">
      <video preload="none" controls style="width:100%; border-radius:10px; border:1px solid rgba(255,255,255,0.1);">
        <source src="https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/TP4.mp4" type="video/mp4">
      </video>
      <video preload="none" controls style="width:100%; border-radius:10px; border:1px solid rgba(255,255,255,0.1);">
        <source src="https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/video%20woldi.mp4" type="video/mp4">
      </video>
    </div>
  </div>
</section>
```

CSS mobile para ese grid (en `@media (max-width: 768px)`):
```css
/* WOLDI — texto+videos grid */
.woldi-content-grid { grid-template-columns: 1fr !important; gap: 32px !important; }
```
(Agregar `class="woldi-content-grid"` al div del grid en el HTML)

### Patrón grid de videos para LLUVIA CON SOL (6 videos en grilla)
```html
<section class="reveal" id="reels" style="padding: 60px 64px; max-width: 1400px; margin: 0 auto;">
  <div class="section-subtitle" style="letter-spacing:6px;">— EDICIÓN DE VIDEO</div>
  <h2 class="section-title" style="margin-bottom:32px;">REELS<br><em>& VIDEOS</em></h2>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
    <!-- repetir por cada video .mov -->
    <video preload="none" controls style="width:100%; aspect-ratio:9/16; object-fit:cover; border-radius:12px; border:1px solid rgba(255,255,255,0.08);">
      <source src="URL_VIDEO" type="video/quicktime">
    </video>
  </div>
</section>
```

CSS mobile (en `@media (max-width: 768px)`):
```css
/* LLUVIA CON SOL — reels grid */
.lcs-reels-grid { grid-template-columns: 1fr !important; gap: 16px !important; }
```

---

## FASE 1 — Crear `PORTAFOLIO/woldi.html`

**Base:** duplicar `kord3.html`, renombrar `woldi.html`, y hacer estos cambios:

1. `<title>`: `WOLDI - Valentín Sánchez`
2. `--rb`: color dorado/cálido (ej: `#E8B84B`) — WOLDI es gastronomía cálida
3. `.hero-banner` background: `https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-WOLDI.webp`
4. `.hero-tag`: `Proyecto Académico · Siglo 21 · 2025`
5. `.hero-title`: `WOLDI`
6. `.hero-sub`: `Branding · Naming · Sistema Visual · Identidad Editorial`
7. Marquee items: `BRANDING ✦ NAMING ✦ SISTEMA VISUAL ✦ IDENTIDAD EDITORIAL ✦` (repetir x2)
8. Sección descripción + videos (grid 2 col): usar el patrón exacto de arriba con texto WOLDI
9. Debajo del grid: PDF embed (patrón kord3) con URL `https://valentin-cdn.b-cdn.net/PROYECTOS/WOLDI/MANUAL%20DE%20MARCA-WOLDI.pdf`
10. Índice: `#brief` · `#naming` · `#sistema` · `#piezas`
11. **Eliminar** las secciones de remeras/marquee infinito/hype/editorial/ig-feed de kord3 — no aplican
12. **Eliminar** el bloque de Instagram — no aplica
13. Agregar mobile CSS override: `.woldi-content-grid { grid-template-columns: 1fr !important; gap: 32px !important; }`
14. Agregar script IntersectionObserver al pie (patrón natan.html de arriba)

**CHECK FASE 1:** Mostrar el HTML de la sección descripción+videos+PDF antes de avanzar.

---

## FASE 2 — Crear `PORTAFOLIO/lluviaconsol.html`

**Base:** duplicar woldi.html (ya limpio), renombrar `lluviaconsol.html`, y hacer estos cambios:

1. `<title>`: `Lluvia con Sol - Valentín Sánchez`
2. `--rb`: celeste/azul (ej: `#38BDF8`) — agencia, comunicación, modernidad
3. `.hero-banner` background: `https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-LLLUEVE-CON-SOL.webp`
4. `.hero-tag`: `Trabajo Freelance · Mayo 2026 — Presente`
5. `.hero-title`: `LLUVIA<br><em>CON SOL</em>`
6. `.hero-sub`: `Edición de Video · Diseño Gráfico · Contenido para Redes`
7. Marquee items: `EDICIÓN DE VIDEO ✦ DISEÑO GRÁFICO ✦ CONTENIDO PARA REDES ✦ GESTIÓN DE CUENTAS ✦` (x2)
8. Descripción: texto LLUVIA CON SOL exacto (arriba) — solo texto, sin videos al lado (layout 1 col)
9. Tags: `EDICIÓN DE VIDEO` `DISEÑO GRÁFICO` `CONTENIDO PARA REDES` `GESTIÓN DE CUENTAS`
10. Índice: `#reels` · `#placas` · `#historias`
11. Sección `#reels`: grid 3 cols con los 6 videos .mov (patrón de arriba), class `lcs-reels-grid`
12. Sección `#placas`: solo el comentario `<!-- PENDIENTE: placas y diseño gráfico — esperando material -->`
13. Sección `#historias`: solo el comentario `<!-- PENDIENTE: historias — esperando material -->`
14. **Sin** PDF embed, **sin** bloque Instagram
15. Mobile override: `.lcs-reels-grid { grid-template-columns: 1fr !important; gap: 16px !important; }`
16. Script IntersectionObserver al pie (patrón natan.html)

**CHECK FASE 2:** Confirmar 6 videos en el HTML y los 2 comentarios PENDIENTE presentes.

---

## FASE 3 — Actualizar `PORTAFOLIO/index.html`

### 3a. Agregar 2 tarjetas nuevas al grid `.pg`

El markup exacto de cada tarjeta existente (copiar este patrón, NO inventar clases):
```html
<a class="pc" href="woldi.html">
  <div class="pcb" style="background-image: url('https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-WOLDI.webp');"></div>
  <div class="po">
    <div class="pt">
      <span class="pn">WOLDI</span>
      <span class="pd">Branding · Naming · Sistema Visual</span>
    </div>
  </div>
</a>

<a class="pc" href="lluviaconsol.html">
  <div class="pcb" style="background-image: url('https://valentin-cdn.b-cdn.net/PORTADAS/portadas-proyectos/PORTADA-LLLUEVE-CON-SOL.webp');"></div>
  <div class="po">
    <div class="pt">
      <span class="pn">LLUVIA CON SOL</span>
      <span class="pd">Edición de Video · Diseño de Contenido</span>
    </div>
  </div>
</a>
```

### 3b. Reestructurar el grid en 4 categorías

Antes de cada grupo de tarjetas, insertar un separador con esta clase (buscar en el CSS de index.html la clase de subtítulo que ya existe — puede ser `.section-subtitle`, `.sl`, o similar — usar esa misma sin crear clases nuevas):

```html
<!-- Grupo 1 -->
<div class="pg-category">— BRANDING / IDENTIDAD DE MARCA</div>
<!-- tarjetas: WOLDI · KORD3 · OPERO (en ese orden) -->

<!-- Grupo 2 -->
<div class="pg-category">— EDICIÓN DE VIDEOS</div>
<!-- tarjetas: LLUVIA CON SOL · AGENCY LUXURY · HOME IMPROVEMENT POWER (en ese orden) -->

<!-- Grupo 3 -->
<div class="pg-category">— MANEJO DE CUENTAS / REDES SOCIALES</div>
<!-- tarjetas: MAN BLUE FC · ENERGÍA FITNESS · NATAN BARBER (en ese orden) -->

<!-- Grupo 4 -->
<div class="pg-category">— INDUMENTARIA</div>
<!-- tarjetas: MF SPORTS (sola — si el grid es 3 cols, esta tarjeta va a quedar en 1/3 del ancho, está bien) -->
```

CSS a agregar para `.pg-category` (en el bloque de estilos de index.html, NO en mobile):
```css
.pg-category {
  grid-column: 1 / -1;          /* ocupa el ancho completo del grid */
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 0.75rem;
  letter-spacing: 6px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.4);
  padding: 32px 0 8px;
  border-top: 1px solid rgba(255,255,255,0.08);
  margin-top: 16px;
}
.pg-category:first-child { border-top: none; margin-top: 0; padding-top: 0; }
```

**Orden final del DOM** dentro del `.pg`:
1. `<div class="pg-category">— BRANDING / IDENTIDAD DE MARCA</div>`
2. tarjeta WOLDI
3. tarjeta KORD3
4. tarjeta OPERO
5. `<div class="pg-category">— EDICIÓN DE VIDEOS</div>`
6. tarjeta LLUVIA CON SOL
7. tarjeta AGENCY LUXURY
8. tarjeta HOME IMPROVEMENT POWER
9. `<div class="pg-category">— MANEJO DE CUENTAS / REDES SOCIALES</div>`
10. tarjeta MAN BLUE FC
11. tarjeta ENERGÍA FITNESS
12. tarjeta NATAN BARBER
13. `<div class="pg-category">— INDUMENTARIA</div>`
14. tarjeta MF SPORTS

**No borres ni recrees tarjetas** — reordená el DOM y agregá los separadores.

**CHECK FASE 3:** Mostrar el HTML completo de `#proyectos` con las 10 tarjetas y 4 categorías.

---

## FASE 4 — Sincronizar navegación

En **cada archivo** del proyecto (`index.html`, `woldi.html`, `lluviaconsol.html` y todas las páginas existentes: `kord3.html`, `agency.html`, `manblue.html`, `energia.html`, `natan.html`, `opero.html`, `mfsports.html`, `home.html`, `curriculum.html`), agregar en el `<nav>` desktop y en el overlay mobile:

```html
<li><a href="woldi.html">WOLDI</a></li>
<li><a href="lluviaconsol.html">LLUVIA CON SOL</a></li>
```

Seguir el mismo orden y clases que los links existentes. No alterar el estilo del nav.

**CHECK FASE 4:** Confirmar que los links aparecen en nav desktop Y mobile overlay de al menos 3 páginas distintas.

---

## FASE 5 — Homogeneizar galerías de MANEJO DE CUENTAS / REDES SOCIALES

### Patrón objetivo (manblue.html) — copiar este CSS en energia y natan
```css
.media-grid { display: grid; gap: 16px; margin-top: 30px; }
.grid-feed { grid-template-columns: repeat(5, 1fr); }
.grid-stories { grid-template-columns: repeat(6, 1fr); }
.media-card { background: #0d0d0d; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,.08); transition: .4s; position: relative; }
.media-card:hover { border-color: var(--rb); transform: translateY(-8px); box-shadow: 0 20px 40px rgba(var(--rb-rgb),0.2); }
.media-card img { width: 100%; display: block; transition: .5s; }
.media-card.feed img { aspect-ratio: 4/5; object-fit: cover; }
.media-card.story img { aspect-ratio: 9/16; object-fit: cover; }
.media-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); opacity: 0; transition: .3s; display: flex; flex-direction: column; justify-content: flex-end; padding: 16px; }
.media-card:hover .media-overlay { opacity: 1; }
.media-label { font-family: 'Barlow Condensed', sans-serif; font-size: 0.7rem; letter-spacing: 3px; color: #fff; text-transform: uppercase; }
```

Mobile overrides para este patrón (en `@media (max-width: 768px)`):
```css
.grid-feed { grid-template-columns: repeat(3, 1fr) !important; gap: 8px !important; }
.grid-stories { grid-template-columns: repeat(3, 1fr) !important; gap: 6px !important; }
```

### En energia.html — qué sacar y qué poner

**Sacar:** el bloque completo del carrusel de historias:
- `.carousel-wrap` → `.carousel-track#storiesTrack` → `.carousel-slide` (x11 slides)
- Los botones `.carousel-btn` prev/next y `.carousel-dots`
- El `<script>` del carrusel (la función anónima que hace el auto-slide)

**NO tocar:** `.grid` de posts/placas, `.ig-feed` de reels, hype feed, sección de video intro

**Poner en su lugar** (mismas imágenes del carrusel, ahora en grid estático):
```html
<div class="media-grid grid-stories">
  <div class="media-card story"><img src="URL_HISTORIA_1" loading="lazy"><div class="media-overlay"><span class="media-label">HISTORIA</span></div></div>
  <!-- repetir por cada imagen que tenía el carrusel -->
</div>
```

Las URLs de las imágenes están en los `.carousel-slide` del HTML actual de energia.html — copiarlas tal cual.

### En natan.html — qué sacar y qué poner

**Sacar carrusel de productos** (`#productTrack`):
- El `.carousel-wrap` con `.product-slide` × 8 imágenes
- Sus botones prev/next

**Sacar carrusel de stories** (`#storiesTrack`):
- El `.carousel-wrap` con `.carousel-slide` × 5 imágenes
- Sus botones prev/next

**Sacar el script** `initCarousel()` completo si no lo usa ninguna otra sección

**NO tocar:** `.ig-feed` reels, `.sessions-grid`, hype feed, secciones de video

**Poner en lugar del carrusel de productos:**
```html
<div class="media-grid grid-feed">
  <!-- 8 .media-card.feed con las mismas URLs de .product-slide -->
</div>
```

**Poner en lugar del carrusel de stories:**
```html
<div class="media-grid grid-stories">
  <!-- 5 .media-card.story con las mismas URLs de .carousel-slide -->
</div>
```

**CHECK FASE 5:** Confirmar que energia y natan ya no tienen `.carousel-wrap` en las secciones de fotos y que el grid se ve con las mismas imágenes.

---

## COMMIT FINAL

```bash
cd C:\Users\valen\Documents\PROYECTOS\PORTAFOLIO
git add PORTAFOLIO/woldi.html PORTAFOLIO/lluviaconsol.html PORTAFOLIO/index.html PORTAFOLIO/kord3.html PORTAFOLIO/agency.html PORTAFOLIO/manblue.html PORTAFOLIO/energia.html PORTAFOLIO/natan.html PORTAFOLIO/opero.html PORTAFOLIO/mfsports.html PORTAFOLIO/home.html PORTAFOLIO/curriculum.html
git commit -m "feat: woldi + lluviaconsol, index categorias, nav sync, galerías homogeneizadas"
git push origin limpio:main
```

Vercel despliega en ~1 min en `portafolio-valentin-omega.vercel.app`.
