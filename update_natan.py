import sys

try:
    with open('natan.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Part A
    old_a = '''        <div class="vid-slide active">
          <div class="vid-placeholder">
            <!-- VIDEO_URL: Video presentación Natan Barber Estudio -->
            <div class="vid-label">VIDEO 01</div>
            <div class="vid-ph-icon">▶</div>
            <div class="vid-desc">VIDEO PRESENTACIÓN</div>
            <span class="vid-pending-tag">VIDEO PENDIENTE</span>
          </div>
        </div>
        <div class="vid-slide">
          <div class="vid-placeholder">
            <!-- VIDEO_URL: Semana hype Natan Barber -->
            <div class="vid-label">VIDEO 02</div>
            <div class="vid-ph-icon">▶</div>
            <div class="vid-desc">SEMANA HYPE</div>
            <span class="vid-pending-tag">VIDEO PENDIENTE</span>
          </div>
        </div>
        <div class="vid-slide">
          <div class="vid-placeholder">
            <!-- VIDEO_URL: Reels Instagram Natan Barber -->
            <div class="vid-label">VIDEO 03</div>
            <div class="vid-ph-icon">▶</div>
            <div class="vid-desc">REELS INSTAGRAM</div>
            <span class="vid-pending-tag">VIDEO PENDIENTE</span>
          </div>
        </div>'''
        
    new_a = '''        <div class="vid-slide active">
          <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/reel-1.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:contain;background:#000;"></video>
          <div class="vid-label">VIDEO 01</div>
          <div class="vid-desc">REEL INSTAGRAM</div>
        </div>
        <div class="vid-slide">
          <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/0307.mov" muted loop playsinline preload="none" style="width:100%;height:100%;object-fit:contain;background:#000;"></video>
          <div class="vid-label">VIDEO 02</div>
          <div class="vid-desc">CORTE EN CÁMARA</div>
        </div>
        <div class="vid-slide">
          <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/videos/corte-primer-plano.mov" muted loop playsinline preload="none" style="width:100%;height:100%;object-fit:contain;background:#000;"></video>
          <div class="vid-label">VIDEO 03</div>
          <div class="vid-desc">PRIMER PLANO · ESTUDIO</div>
        </div>'''

    if old_a in c:
        c = c.replace(old_a, new_a)
    else:
        print('Error: Could not find Part A (old_a)')

    # Part B
    old_b = '''      <!-- DRIVE_URL: Carpeta Semana Hype Natan Barber -->
      <a href="https://drive.google.com/drive/folders/10VDCAvcV0GHDqey07kYphW-ownJEupqn?usp=drive_link" target="_blank"
        class="btn-red" data-pending="DRIVE_URL">VER CONTENIDO →</a>
    </div>
  </div>'''

    new_b = '''    </div>
  </div>

  <!-- GALERÍA SEMANA HYPE NATAN -->
  <section class="reveal" style="padding: 0 64px 60px; max-width: 1200px; margin: 0 auto;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-width:500px;">
      <div style="position:relative;overflow:hidden;border-radius:8px;border:1px solid rgba(255,255,255,.08);">
        <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/semana-hype/escribiendo.mp4" muted loop playsinline preload="none" style="width:100%;aspect-ratio:9/16;object-fit:cover;display:block;cursor:pointer;" onclick="this.paused?this.play():this.pause()" onmouseenter="this.play()" onmouseleave="this.pause()"></video>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:2px;color:rgba(255,255,255,.7);text-transform:uppercase;">Escribiendo</div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:8px;border:1px solid rgba(255,255,255,.08);">
        <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/semana-hype/terminado.mp4" muted loop playsinline preload="none" style="width:100%;aspect-ratio:9/16;object-fit:cover;display:block;cursor:pointer;" onclick="this.paused?this.play():this.pause()" onmouseenter="this.play()" onmouseleave="this.pause()"></video>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:2px;color:rgba(255,255,255,.7);text-transform:uppercase;">Terminado</div>
      </div>
    </div>
    <style>@media(max-width:768px){.natan-hype-grid{max-width:100%!important;}}</style>
  </section>'''

    if old_b in c:
        c = c.replace(old_b, new_b)
    else:
        print('Error: Could not find Part B (old_b)')

    # Part C
    old_c = '''      <div class="work-item">
        <h2 class="section-title">IDENTIDAD VISUAL & BRANDING</h2>
        <!-- DRIVE_URL: Carpeta Identidad Visual & Branding Natan Barber -->
        <a href="https://drive.google.com/drive/folders/1sBn4a-ErgBiuKHKNNLZyNWWM_Y2kqZjG?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">VIDEO DE PRESENTACIÓN</h2>
        <!-- VIDEO_URL: Video de Presentación Natan Barber Estudio -->
        <a href="https://drive.google.com/file/d/1988-W1wE0dAxAsf6wLktvnxCiRNH8HLA/view?usp=drive_link" target="_blank"
          class="btn-red" data-pending="VIDEO_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">STICKERS & DISEÑO GRÁFICO</h2>
        <!-- DRIVE_URL: Carpeta Stickers & Diseño Gráfico Natan Barber -->
        <a href="https://drive.google.com/drive/folders/1ayGPRBRxmenzvTuW6wfJhDH-5xB8MN9q?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>'''

    new_c = '''      <div class="work-item">
        <h2 class="section-title">IDENTIDAD VISUAL & BRANDING</h2>
        <a href="https://www.instagram.com/natan.barber.estudio/" target="_blank" class="btn-red">VER INSTAGRAM →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">VIDEO DE PRESENTACIÓN</h2>
        <a href="#" onclick="document.querySelector('.vid-carousel-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER VIDEOS ↓</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">STICKERS & DISEÑO GRÁFICO</h2>
        <a href="https://www.instagram.com/natan.barber.estudio/" target="_blank" class="btn-red">VER INSTAGRAM →</a>
      </div>'''

    if old_c in c:
        c = c.replace(old_c, new_c)
    else:
        print('Error: Could not find Part C (old_c)')

    with open('natan.html', 'w', encoding='utf-8') as f:
        f.write(c)

    print('Success: natan.html updated')

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
