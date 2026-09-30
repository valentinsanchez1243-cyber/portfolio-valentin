import sys

try:
    with open('agency.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update video URLs
    c = c.replace('videos/caida-de-mamas.mov', 'videos/LUXURY%20AGENCY%20-%20CAIDA%20DE%20MAMAS.mov')
    c = c.replace('videos/pin-pong.mov', 'videos/PIN%20PONG-LUXURY%20AGENCY.mov')
    c = c.replace('videos/vsl-lipoabdominoplastia-gluteos.mov', 'videos/VSL%20Lipoabdominoplastia%20%2B%20Gl%C3%BAteos%203D-Agency%20Luxury.mov')
    c = c.replace('videos/vsl-rediseno-de-mamas.mov', 'videos/VSL%20Redise%C3%B1o%20de%20Mamas.mov')
    c = c.replace('videos/vsl-rinoplastia-ultrasonica.mov', 'videos/VSL%20Rinoplastia%20ultras%C3%B3nica-feed.mov')

    # 2. Add 7th video
    vid6_end = '''        <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/PIN%20PONG-LUXURY%20AGENCY.mov" controls preload="metadata" style="width: 100%; aspect-ratio: 9/16; object-fit: contain; background: #111; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;"></video>
        <div style="font-family: 'Barlow Condensed', sans-serif; font-size: 1rem; letter-spacing: 2px; color: var(--w); text-align: center; text-transform: uppercase;">PIN PONG</div>
      </div>'''
      
    vid7_html = '''

      <!-- Video 7 - Riaño Con Portada -->
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/AGENCY-LUXURY/videos/1%C2%B0RIA%C3%91O29.10.2025%20CON%20PORTADA.mov" controls preload="none" style="width: 100%; aspect-ratio: 9/16; object-fit: contain; background: #111; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;"></video>
        <div style="font-family: 'Barlow Condensed', sans-serif; font-size: 1rem; letter-spacing: 2px; color: var(--w); text-align: center; text-transform: uppercase;">DR. RIAÑO CON PORTADA</div>
      </div>'''

    if vid6_end in c:
        c = c.replace(vid6_end, vid6_end + vid7_html)
    else:
        print('Error: Could not find PIN PONG video block')
        sys.exit(1)

    # 3. Change preload
    c = c.replace('preload="metadata"', 'preload="none"')

    # 4. Worklist replacements
    old_worklist = '''  <!-- SECCIÓN 3: LISTA DE TRABAJOS -->
  <section class="reveal">
    <div class="work-list">
      <div class="work-item">
        <h2 class="section-title">VSL & ANUNCIOS FACEBOOK ADS</h2>
        <!-- DRIVE_URL: Carpeta VSL & Anuncios Agency Luxury -->
        <a href="https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">THUMBNAILS & COVERS</h2>
        <!-- DRIVE_URL: Carpeta Thumbnails & Covers Agency Luxury -->
        <a href="https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">CONTENIDO AUDIOVISUAL</h2>
        <!-- DRIVE_URL: Carpeta Contenido Audiovisual Agency Luxury -->
        <a href="https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
    </div>
  </section>'''

    new_worklist = '''  <!-- SECCIÓN 3: LISTA DE TRABAJOS -->
  <section class="reveal">
    <div class="work-list">
      <div class="work-item">
        <h2 class="section-title">VSL & ANUNCIOS FACEBOOK ADS</h2>
        <a href="#" onclick="document.querySelector('.vid-carousel-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER VIDEOS ↓</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">THUMBNAILS & COVERS</h2>
        <a href="#" onclick="document.querySelector('[alt=\\'Dr. Hugo Ayarde - Cover\\']').closest('section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER PORTADAS ↓</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">CONTENIDO AUDIOVISUAL</h2>
        <a href="#" onclick="document.querySelector('.vid-carousel-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER TODO ↓</a>
      </div>
    </div>
  </section>'''

    if old_worklist in c:
        c = c.replace(old_worklist, new_worklist)
    else:
        print('Error: Could not find old worklist block')
        sys.exit(1)

    with open('agency.html', 'w', encoding='utf-8') as f:
        f.write(c)

    print('Success: agency.html updated')

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
