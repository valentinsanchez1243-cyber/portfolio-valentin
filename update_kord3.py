import sys

try:
    with open('kord3.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Part A
    old_a = '''      <div class="work-item">
        <h2 class="section-title">REMERAS & INDUMENTARIA</h2>
        <!-- NOTA: Las fotos de remeras están siendo procesadas para subir -->
        <a href="https://drive.google.com/drive/folders/1ly87LmFk6pps-RF6W_E8Y8V2Lz5xOqOF?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>'''
    new_a = '''      <div class="work-item">
        <h2 class="section-title">REMERAS & INDUMENTARIA</h2>
        <a href="#remeras-section" onclick="document.getElementById('remeras-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER COLECCIÓN ↓</a>
      </div>'''

    if old_a in c:
        c = c.replace(old_a, new_a)
    else:
        print('Error: Could not find Part A (old_a)')

    # Part B
    old_b = '''      <div class="work-item">
        <h2 class="section-title">PRODUCCIÓN AUDIOVISUAL</h2>
        <a href="https://drive.google.com/drive/folders/1xuUjEc9q29kmz87H9jvJQNv2ebxSppiq?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>'''
    new_b = '''      <div class="work-item">
        <h2 class="section-title">PRODUCCIÓN AUDIOVISUAL</h2>
        <a href="#" onclick="document.querySelector('.vid-carousel-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER VIDEOS ↓</a>
      </div>'''

    if old_b in c:
        c = c.replace(old_b, new_b)
    else:
        print('Error: Could not find Part B (old_b)')

    # Part C
    old_c = '''  <!-- SECCIÓN: MANUAL DE MARCA -->
  <section class="reveal" style="padding: 20px 64px 60px; max-width: 1200px; margin: 0 auto;">'''
    
    new_c_insert = '''  <!-- SECCIÓN: REMERAS & INDUMENTARIA -->
  <section id="remeras-section" class="reveal" style="padding: 20px 64px 80px; max-width: 1400px; margin: 0 auto;">
    <div class="section-subtitle">— DROP 0.0 · COLECCIÓN COMPLETA</div>
    <h2 class="section-title" style="margin-bottom: 40px;">REMERAS<br><em>KORD3</em></h2>

    <!-- FILTRO COLOR -->
    <div style="display:flex;gap:12px;margin-bottom:32px;flex-wrap:wrap;" id="remera-filter">
      <button onclick="filterRemeras('all')" class="rf-btn rf-active" style="font-family:'Barlow Condensed',sans-serif;font-size:.75rem;letter-spacing:3px;text-transform:uppercase;padding:8px 20px;border:1px solid var(--r);background:var(--r);color:#fff;cursor:pointer;transition:.2s;">TODAS</button>
      <button onclick="filterRemeras('NEGRO')" class="rf-btn" style="font-family:'Barlow Condensed',sans-serif;font-size:.75rem;letter-spacing:3px;text-transform:uppercase;padding:8px 20px;border:1px solid rgba(255,255,255,.3);background:none;color:var(--w);cursor:pointer;transition:.2s;">NEGRA</button>
      <button onclick="filterRemeras('BLANCO')" class="rf-btn" style="font-family:'Barlow Condensed',sans-serif;font-size:.75rem;letter-spacing:3px;text-transform:uppercase;padding:8px 20px;border:1px solid rgba(255,255,255,.3);background:none;color:var(--w);cursor:pointer;transition:.2s;">BLANCA</button>
    </div>

    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;" id="remeras-grid" class="rem-grid">

      <!-- REMERA 1 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA1-FRONT-NEGRA.png" loading="lazy" alt="REMERA 1 NEGRA FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA1-BACK-NEGRA.png" loading="lazy" alt="REMERA 1 NEGRA BACK" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">1 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA1-FRONT-BLANCA.png" loading="lazy" alt="REMERA 1 BLANCA FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA1-BACK-BLANCA.png" loading="lazy" alt="REMERA 1 BLANCA BACK" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">1 · BLANCA</div>
      </div>

      <!-- REMERA 2 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA2-FRONT-NEGRO.png" loading="lazy" alt="REMERA 2 NEGRO FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA2-BACK-NEGRO.png" loading="lazy" alt="REMERA 2 NEGRO BACK" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">2 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA2-FRONT-BLANCO.png" loading="lazy" alt="REMERA 2 BLANCO FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA2-BACK-BLANCO.png" loading="lazy" alt="REMERA 2 BLANCO BACK" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">2 · BLANCA</div>
      </div>

      <!-- REMERA 3 (tiene versión púrpura extra) -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA3-FRONT-NEGRO.png" loading="lazy" alt="REMERA 3 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA3-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">3 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA3-FRONT-BLANCO.png" loading="lazy" alt="REMERA 3 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA3-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">3 · BLANCA</div>
      </div>

      <!-- REMERA 4 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA4-FRONT-NEGRO.png" loading="lazy" alt="REMERA 4 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA4-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">4 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA4-FRONT-BLANCO.png" loading="lazy" alt="REMERA 4 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA4-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">4 · BLANCA</div>
      </div>

      <!-- REMERA 5 CODE001 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA5-CODE001-FRONT-NEGRO.png" loading="lazy" alt="REMERA 5 CODE001" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA5-CODE001-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">5 CODE001 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA5-CODE001-FRONT-BLANCO.png" loading="lazy" alt="REMERA 5 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA5-CODE001-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">5 CODE001 · BLANCA</div>
      </div>

      <!-- REMERA 6 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA6-FRONT.png" loading="lazy" alt="REMERA 6 FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA6-BACK.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">6</div>
      </div>

      <!-- REMERA 7 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA7-FRONT-NEGRO.jpg" loading="lazy" alt="REMERA 7 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA7-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">7 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA7-FRONT-BLANCO.png" loading="lazy" alt="REMERA 7 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA7-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">7 · BLANCA</div>
      </div>

      <!-- REMERA 8 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA8-FRONT.png" loading="lazy" alt="REMERA 8 FRONT" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA8-BACK.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">8</div>
      </div>

      <!-- REMERA 9 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA9-FRONT-NEGRO.png" loading="lazy" alt="REMERA 9 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA9-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">9 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA9-FRONT-BLANCO.png" loading="lazy" alt="REMERA 9 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA9-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">9 · BLANCA</div>
      </div>

      <!-- REMERA 10 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA10-FRONT.png" loading="lazy" alt="REMERA 10" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA10-BACK.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">10</div>
      </div>

      <!-- REMERA 11 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA11-FRONT-NEGRO.png" loading="lazy" alt="REMERA 11 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA11-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">11 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA11-FRONT-BLANCO.png" loading="lazy" alt="REMERA 11 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA11-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">11 · BLANCA</div>
      </div>

      <!-- REMERA 12 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA12-FRONT-NEGRO.png" loading="lazy" alt="REMERA 12 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA12-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">12 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA12-FRONT-BLANCO.png" loading="lazy" alt="REMERA 12 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA12-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">12 · BLANCA</div>
      </div>

      <!-- REMERA 13 -->
      <div class="rem-item" data-color="NEGRO" style="position:relative;overflow:hidden;border-radius:6px;background:#0d0d0d;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA13-FRONT-NEGRO.png" loading="lazy" alt="REMERA 13 NEGRO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA13-BACK-NEGRO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(255,255,255,.5);">13 · NEGRA</div>
      </div>
      <div class="rem-item" data-color="BLANCO" style="position:relative;overflow:hidden;border-radius:6px;background:#f5f5f5;cursor:pointer;" onmouseover="this.querySelector('.rem-back').style.opacity='1'" onmouseout="this.querySelector('.rem-back').style.opacity='0'">
        <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA13-FRONT-BLANCO.png" loading="lazy" alt="REMERA 13 BLANCO" style="width:100%;aspect-ratio:3/4;object-fit:cover;display:block;">
        <div class="rem-back" style="position:absolute;inset:0;opacity:0;transition:opacity .35s;">
          <img src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/remeras/REMERA13-BACK-BLANCO.png" loading="lazy" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="position:absolute;bottom:8px;left:8px;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:2px;color:rgba(0,0,0,.4);">13 · BLANCA</div>
      </div>

    </div>

    <style>
      @media (max-width: 1024px) { #remeras-grid { grid-template-columns: repeat(3,1fr) !important; } }
      @media (max-width: 640px) { #remeras-grid { grid-template-columns: repeat(2,1fr) !important; } }
      .rf-btn { transition: background .2s, color .2s, border-color .2s !important; }
      .rf-active { background: var(--r) !important; border-color: var(--r) !important; color: #fff !important; }
    </style>
    <script>
      function filterRemeras(color) {
        const items = document.querySelectorAll('.rem-item');
        const btns = document.querySelectorAll('.rf-btn');
        btns.forEach(b => b.classList.remove('rf-active'));
        event.target.classList.add('rf-active');
        items.forEach(item => {
          if (color === 'all' || item.dataset.color === color) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
        // Re-adjust grid columns
        const grid = document.getElementById('remeras-grid');
        if (color === 'all') {
          grid.style.gridTemplateColumns = 'repeat(4,1fr)';
        } else {
          grid.style.gridTemplateColumns = 'repeat(4,1fr)';
        }
      }
    </script>
  </section>
\n'''

    if old_c in c:
        c = c.replace(old_c, new_c_insert + old_c)
    else:
        print('Error: Could not find Part C (old_c)')

    # Part D
    old_d = '''        <div class="vid-slide">
          <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/NATAN-BARBER/semana-hype/terminado.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:contain;background:#000;"></video>
          <div class="vid-label">VIDEO 03</div>
          <div class="vid-desc">SEMANA HYPE · CONTENIDO</div>
        </div>'''
    
    new_d = '''        <div class="vid-slide">
          <video src="https://valentin-cdn.b-cdn.net/PROYECTOS/KORD3/video-logo-horizontal.mp4" autoplay muted loop playsinline style="width:100%;height:100%;object-fit:contain;background:#000;"></video>
          <div class="vid-label">VIDEO 03</div>
          <div class="vid-desc">LOGO REVEAL · HORIZONTAL</div>
        </div>'''
    
    if old_d in c:
        c = c.replace(old_d, new_d)
    else:
        print('Error: Could not find Part D (old_d)')

    with open('kord3.html', 'w', encoding='utf-8') as f:
        f.write(c)

    print('Success: kord3.html updated')

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
