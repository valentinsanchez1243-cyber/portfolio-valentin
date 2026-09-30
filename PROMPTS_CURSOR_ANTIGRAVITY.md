# PROMPTS PARA CURSOR DE ANTIGRAVITY
# Portfolio Valentín Sánchez — Optimización de Performance
# Copiar y pegar CADA prompt por separado en el Cursor de Antigravity

---

## PROMPT 1: energia.html — Fix preload auto + loading eager

```
En el archivo energia.html, necesito que hagas exactamente estos 2 cambios SIN modificar nada estético ni visual:

CAMBIO 1: Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Esto está dentro de un script al final del archivo, en una función que maneja los videos con IntersectionObserver. Solo hay UNA ocurrencia de esta línea.

CAMBIO 2: Buscar la etiqueta de imagen que tiene:
loading="eager"

Y cambiarla a:
loading="lazy"

Solo hay UNA imagen con loading="eager" en este archivo (es un GIF).

NO modifiques nada más. No cambies estilos, no muevas elementos, no toques el HTML visual. Solo estos 2 valores.
```

---

## PROMPT 2: home.html — Fix preload auto

```
En el archivo home.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Está dentro de un script al final del archivo, en la función que usa IntersectionObserver para los videos. Solo hay UNA ocurrencia.

NO modifiques nada más. No cambies estilos, clases, estructura HTML ni nada visual. Solo cambiar 'auto' por 'none' en esa línea exacta.
```

---

## PROMPT 3: natan.html — Fix preload auto

```
En el archivo natan.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Está dentro de un script al final del archivo, en la función de IntersectionObserver. Solo hay UNA ocurrencia.

NO modifiques absolutamente nada más. Solo ese valor de 'auto' a 'none'.
```

---

## PROMPT 4: kord3.html — Fix preload auto

```
En el archivo kord3.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Está dentro de un script al final del archivo. Solo hay UNA ocurrencia.

NO modifiques nada más. Cero cambios estéticos. Solo ese valor.
```

---

## PROMPT 5: manblue.html — Fix preload auto

```
En el archivo manblue.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Está dentro de un script al final del archivo. Solo hay UNA ocurrencia.

NO modifiques nada más. Solo ese valor.
```

---

## PROMPT 6: opero.html — Fix preload auto

```
En el archivo opero.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
v.setAttribute('preload', 'auto');

Y cambiarla a:
v.setAttribute('preload', 'none');

Está dentro de un script al final del archivo. Solo hay UNA ocurrencia. Aunque esta página no tiene videos visibles, el script está ahí y hay que corregirlo igualmente.

NO modifiques nada más.
```

---

## PROMPT 7: agency.html — Agregar preload none (caso especial)

```
En el archivo agency.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar la línea que dice:
document.querySelectorAll('video').forEach(v => vidObs.observe(v));

Y cambiarla a:
document.querySelectorAll('video').forEach(v => { v.preload = 'none'; vidObs.observe(v); });

Esta línea está dentro de un script al final del archivo que usa IntersectionObserver (vidObs) para observar los videos. El problema es que los 17 videos de esta página no tienen preload definido, entonces el navegador usa el default "metadata" que aún descarga datos de cada video al cargar. Agregando v.preload = 'none' antes de observarlos, evitamos cualquier descarga hasta que el usuario scrollee hasta ellos.

NO modifiques nada más. No cambies los atributos HTML de los videos, no toques estilos, no muevas nada visual.
```

---

## PROMPT 8: index.html — Cambiar preload metadata a none (10 videos)

```
En el archivo index.html, necesito que hagas exactamente este cambio SIN modificar nada estético ni visual:

Buscar TODAS las ocurrencias de:
preload="metadata"

Y cambiar CADA UNA a:
preload="none"

Hay exactamente 10 ocurrencias, todas en etiquetas <video> que usan el patrón data-src para lazy loading. Están en la sección de proyectos (HOME-IMPROVEMENT y ENERGIA-FITNESS).

NO modifiques nada más. No cambies data-src, no toques estilos, no muevas nada. Solo el valor del atributo preload en esas 10 etiquetas video.
```

---

## PROMPT 9: index.html — Agregar lazy loading para background-images

```
En el archivo index.html, necesito que agregues este script JUSTO ANTES de la etiqueta </body> (antes del cierre del body, después de todos los demás scripts):

<script>
(function () {
  if (!('IntersectionObserver' in window)) return;
  var bgRx = /background-image:\s*url\(['"]?(https:\/\/valentin-cdn[^'")]+)['"]?\)/;
  var bgObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var url = el.getAttribute('data-lazy-bg');
      if (url) {
        el.style.backgroundImage = "url('" + url + "')";
        el.removeAttribute('data-lazy-bg');
      }
      bgObs.unobserve(el);
    });
  }, { rootMargin: '400px 0px' });
  document.querySelectorAll('[style]').forEach(function (el) {
    var s = el.getAttribute('style') || '';
    var m = s.match(bgRx);
    if (m) {
      el.setAttribute('data-lazy-bg', m[1]);
      el.style.backgroundImage = 'none';
      bgObs.observe(el);
    }
  });
})();
</script>

Este script hace lazy loading de las 41 imágenes de fondo (background-image) que están en elementos con style inline apuntando a valentin-cdn.b-cdn.net. En vez de cargar todas las imágenes al abrir la página (incluso las que están en paneles ocultos/acordeones cerrados), las carga solo cuando el usuario está a 400px de verlas.

NO modifiques nada más del archivo. No toques los estilos inline existentes, no cambies clases, no muevas HTML. Solo agregar este script antes de </body>.
```

---

## PROMPT 10: TODOS LOS ARCHIVOS — Cambiar URLs de .mov a .mp4 (EJECUTAR DESPUÉS DE SUBIR LOS MP4 A BUNNY CDN)

```
IMPORTANTE: Este cambio solo se aplica DESPUÉS de haber subido los archivos .mp4 convertidos a Bunny CDN.

En TODOS estos archivos, necesito que reemplaces las extensiones .mov por .mp4 en las URLs de video que apuntan a valentin-cdn.b-cdn.net:

ARCHIVO: index.html
Cambiar estas URLs (solo la extensión .mov → .mp4):
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.4.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/2.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.3.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/energia-fitness.mov → .mp4

ARCHIVO: home.html
Cambiar estas URLs:
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/2.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/1.4.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/HOME-IMPROVEMENT/3.3.mov → .mp4

ARCHIVO: energia.html
Cambiar estas URLs:
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/MODALIDAD.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/PROMOCION.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/VIDEO%20PRESENTACION.mov → VIDEO-PRESENTACION.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-1.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-2.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-3.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/semana-hype/semana-hype-4.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/ENERGIA-FITNESS/videos/energia-fitness.mov → .mp4

ARCHIVO: natan.html
Cambiar estas URLs:
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/natan%20ahora.mov → natan-ahora.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/0307.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/asmr.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/corte-primer-plano.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-1.mov → .mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/session-2.mov → .mp4

ARCHIVO: agency.html
Cambiar estas URLs:
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/1%C2%B0RIA%C3%91O29.10.2025%20CON%20PORTADA.mov → 1-RIANIO-CON-PORTADA.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/AGENCY%20LUXURY.mov → AGENCY-LUXURY.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20-%20CAIDA%20DE%20MAMAS.mov → LUXURY-AGENCY-CAIDA-DE-MAMAS.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(1).mov → LUXURY-AGENCY-1.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(2).mov → LUXURY-AGENCY-2.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(3).mov → LUXURY-AGENCY-3.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(4).mov → LUXURY-AGENCY-4.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(5).mov → LUXURY-AGENCY-5.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(6).mov → LUXURY-AGENCY-6.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(7).mov → LUXURY-AGENCY-7.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(8).mov → LUXURY-AGENCY-8.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY%20(9).mov → LUXURY-AGENCY-9.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/LUXURY%20AGENCY.mov → LUXURY-AGENCY.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/luxury-agency.mov → luxury-agency.mp4
- https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/PIN%20PONG-LUXURY%20AGENCY.mov → PIN-PONG-LUXURY-AGENCY.mp4
- https://valentin-cdn.b-cdn.net/VSL%20RIGE%C3%91O.mov → VSL/VSL-RIGENIO.mp4
- https://valentin-cdn.b-cdn.net/VSL%20REDISE%C3%91O%20DE%20MAMAS.mov → VSL/VSL-REDISENO-DE-MAMAS.mp4

NOTA: Los archivos con espacios y caracteres especiales (%20, %C3%91, etc.) fueron renombrados a versiones con guiones en la conversión a .mp4. Las nuevas URLs son limpias sin %20.

NO modifiques nada más. No toques estilos, no muevas elementos, no cambies atributos que no sean las URLs de src o data-src de los videos.
```

---

## RESUMEN DE ORDEN DE EJECUCIÓN:

1. **Prompts 1-9**: Ejecutarlos YA (son cambios de código que no dependen de nada)
2. **Ejecutar el script `convertir_videos.bat`** para convertir los .mov a .mp4
3. **Subir los .mp4 a Bunny CDN** en las carpetas correspondientes
4. **Prompt 10**: Ejecutarlo DESPUÉS de subir los .mp4 al CDN

## IMPACTO ESPERADO:
- Carga inicial: de 85+ requests a ~30 requests
- Peso de videos: reducción del ~90% (de .mov a .mp4)
- Tiempo de carga: de 10+ segundos a 2-3 segundos
- Sin cambios estéticos ni visuales
