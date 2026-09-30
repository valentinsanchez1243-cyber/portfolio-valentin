import sys

try:
    with open('energia.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Part A
    old_a = '''    <div class="work-list">
      <div class="work-item">
        <h2 class="section-title">IDENTIDAD VISUAL & REBRANDING</h2>
        <!-- DRIVE_URL: Carpeta Identidad Visual & Rebranding Energía Fitness -->
        <a href="https://drive.google.com/drive/folders/1I1RO36YFsDQ-Ia3OM-yKdHe1AKGtMHRq?usp=sharing" target="_blank"
          class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">VIDEO DE PRESENTACIÓN</h2>
        <!-- VIDEO_URL: Video de Presentación Energía Fitness -->
        <a href="https://drive.google.com/file/d/1-j-hn0HflrCUChlCsPfQs9L0doaL5ZsR/view?usp=drive_link" target="_blank"
          class="btn-red" data-pending="VIDEO_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">CONTENIDO DE INSTAGRAM</h2>
        <!-- DRIVE_URL: Carpeta Contenido Instagram Energía Fitness -->
        <a href="https://drive.google.com/drive/folders/1nlq1aGqI45O7k_BP4C4S5h3iMj6XEd9U?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">PLANTILLAS HISTORIAS DESTACADAS</h2>
        <!-- DRIVE_URL: Carpeta Plantillas Historias Energía Fitness -->
        <a href="https://drive.google.com/drive/folders/1mbII1NVnXG9QOdG0jyaMP30lQ5cCFtc1?usp=drive_link"
          target="_blank" class="btn-red" data-pending="DRIVE_URL">VER →</a>
      </div>
    </div>'''

    new_a = '''    <div class="work-list">
      <div class="work-item">
        <h2 class="section-title">IDENTIDAD VISUAL & REBRANDING</h2>
        <a href="https://www.instagram.com/energiafitness.cba/" target="_blank" class="btn-red">VER INSTAGRAM →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">VIDEO DE PRESENTACIÓN</h2>
        <a href="#" onclick="document.querySelector('.vid-carousel-section').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER VIDEO ↓</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">CONTENIDO DE INSTAGRAM</h2>
        <a href="https://www.instagram.com/energiafitness.cba/" target="_blank" class="btn-red">VER INSTAGRAM →</a>
      </div>
      <div class="work-item">
        <h2 class="section-title">SEMANA HYPE</h2>
        <a href="#" onclick="document.querySelector('.hype-wrapper').scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER HYPE ↓</a>
      </div>
    </div>'''

    if old_a in c:
        c = c.replace(old_a, new_a)
    else:
        print('Error: Could not find Part A (old_a)')

    # Part B
    old_b = '''<!-- DRIVE_URL: Carpeta Semana Hype Energía Fitness -->
      <a href="https://drive.google.com/drive/folders/1oZKPKXJ7KaSE_ak6GSJkgiyeXaaZtpqs?usp=drive_link" target="_blank"
        class="btn-red" data-pending="DRIVE_URL">VER CONTENIDO →</a>'''
    
    new_b = '''<!-- DRIVE_URL: Carpeta Semana Hype Energía Fitness -->
      <a href="#" onclick="document.querySelectorAll('.hype-grid')[0].scrollIntoView({behavior:'smooth'});return false;" class="btn-red">VER VIDEOS ↓</a>'''

    if old_b in c:
        c = c.replace(old_b, new_b)
    else:
        print('Error: Could not find Part B (old_b)')

    with open('energia.html', 'w', encoding='utf-8') as f:
        f.write(c)

    print('Success: energia.html updated')

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
