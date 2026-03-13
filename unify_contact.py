import re
import os

# Definir el bloque maestro de contacto con z-index corregidos y Rojo Puro
# {{PATH}} será reemplazado por '' o '../' según corresponda

MASTER_CONTACT = '''  <!-- CONTACTO -->
  <section id="contacto" style="
    background-image: url(\'{{PATH}}IMAGENES MIAS/dearriba.png\');
    background-size: cover;
    background-position: center top;
    position: relative;
    padding: 120px 40px 60px;
    text-align: center;
    overflow: hidden;
  ">

    <!-- Overlay oscuro -->
    <div style="
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.55);
      z-index: 1;
    "></div>

    <!-- Watermark -->
    <div style="
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 12rem;
      font-weight: 900;
      font-family: \'Bebas Neue\', sans-serif;
      color: rgba(255,255,255,0.06);
      z-index: 2;
      pointer-events: none;
      white-space: nowrap;
      letter-spacing: 10px;
    ">CONTACTO</div>

    <!-- Contenido -->
    <div style="position: relative; z-index: 3;">

      <!-- Subtítulo -->
      <p style="
        color: #FF0000;
        font-size: 11px;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-family: \'Barlow Condensed\', sans-serif;
        margin-bottom: 16px;
      ">— HABLEMOS —</p>

      <!-- Título -->
      <h2 style="
        color: #ffffff;
        font-size: 3.5rem;
        font-weight: 900;
        font-family: \'Bebas Neue\', sans-serif;
        text-transform: uppercase;
        line-height: 1.1;
        margin-bottom: 20px;
      ">¿TENÉS UN PROYECTO?</h2>

      <!-- Descripción -->
      <p style="
        color: #ffffff;
        font-size: 1rem;
        max-width: 560px;
        margin: 0 auto 40px;
        line-height: 1.7;
        font-family: \'Barlow\', sans-serif;
      ">Disponible para proyectos freelance, colaboraciones y trabajos de largo plazo. Desde el concepto hasta la
        ejecución.</p>

      <!-- Email -->
      <div style="margin-bottom: 50px;">
        <a href="mailto:vaalentinsanchez5@gmail.com" style="
          display: inline-block;
          color: #ffffff;
          font-size: 2.2rem;
          font-weight: 900;
          font-family: \'Bebas Neue\', sans-serif;
          text-transform: uppercase;
          text-decoration: none;
          letter-spacing: 2px;
          border-bottom: 3px solid #FF0000;
          padding-bottom: 8px;
        ">VAALENTINSANCHEZ5@GMAIL.COM</a>
      </div>

      <!-- 3 columnas info -->
      <div style="
        display: flex;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
        margin-bottom: 50px;
        color: #ffffff;
        font-size: 0.85rem;
        letter-spacing: 1.5px;
        font-family: \'Barlow Condensed\', sans-serif;
        text-transform: uppercase;
      ">
        <span>+54 9 351 555 8997 · TELÉFONO / WHATSAPP</span>
        <span>@VAALENSNCHZ · INSTAGRAM</span>
        <span>CÓRDOBA, ARGENTINA · UBICACIÓN</span>
      </div>

      <!-- Botones -->
      <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">

        <a href="https://wa.me/5493515558997" target="_blank" style="
          background: #FF0000;
          color: #ffffff;
          padding: 14px 32px;
          font-size: 0.85rem;
          font-weight: 700;
          font-family: \'Barlow Condensed\', sans-serif;
          letter-spacing: 2px;
          text-transform: uppercase;
          text-decoration: none;
          border: 2px solid #FF0000;
        ">WHATSAPP</a>

        <a href="https://instagram.com/vaalensnchz" target="_blank" style="
          background: transparent;
          color: #ffffff;
          padding: 14px 32px;
          font-size: 0.85rem;
          font-weight: 700;
          font-family: \'Barlow Condensed\', sans-serif;
          letter-spacing: 2px;
          text-transform: uppercase;
          text-decoration: none;
          border: 2px solid #ffffff;
        ">INSTAGRAM</a>

        <a href="https://drive.google.com/file/d/1IFJ14ORA0Bx63gSytOimdtCGJsHbDbLd/view?usp=sharing" target="_blank"
          style="
          background: transparent;
          color: #ffffff;
          padding: 14px 32px;
          font-size: 0.85rem;
          font-weight: 700;
          font-family: \'Barlow Condensed', sans-serif;
          letter-spacing: 2px;
          text-transform: uppercase;
          text-decoration: none;
          border: 2px solid #ffffff;
        ">DESCARGAR CV</a>

      </div>
    </div>
  </section>'''

def update_file(filepath, is_subpage=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    path_prefix = '../' if is_subpage else ''
    new_contact = MASTER_CONTACT.replace('{{PATH}}', path_prefix)
    
    # Regex para encontrar la sección de contacto completa
    # Buscamos desde <!-- CONTACTO --> hasta el final de la sección o el inicio del footer/script
    contact_pattern = r'<!-- CONTACTO -->\s*<section id="contacto"[\s\S]*?</section>'
    
    if re.search(contact_pattern, content):
        updated_content = re.sub(contact_pattern, new_contact, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated {filepath}")
    else:
        print(f"Contact section not found in {filepath}")

# Actualizar archivos principales
update_file('index.html')
update_file('curriculum.html')
update_file('kord3.html', is_subpage=True)

print("Running generate_pages.py...")
os.system('python generate_pages.py')
