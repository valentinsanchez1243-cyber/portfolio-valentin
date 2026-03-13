import re
import os

# Bloque Mobile CSS Definitivo
MOBILE_CSS = '''
  /* --- MOBILE SYSTEM --- */
  @media (max-width: 768px) {
    body { background-size: 30px 30px; }
    nav { padding: 15px 20px !important; background: rgba(8, 8, 8, .98) !important; }
    .nls { display: none !important; }
    .nl { font-size: 1.1rem !important; }
    .hero-title, .ht, h1, .hero-banner-content .hero-title, .cv-title { font-size: 3.2rem !important; line-height: 1 !important; }
    .hero-sub, .hs { font-size: 13px !important; letter-spacing: 2px !important; }
    .hero-banner { height: 350px !important; padding: 40px 20px !important; }
    .mi { font-size: 1.4rem !important; padding: 0 15px !important; }
    .mw { padding: 15px 0 !important; }
    section, .hype-inner, .instagram-section { padding: 50px 20px !important; }
    .section-title, h2, .hype-title { font-size: 2.2rem !important; }
    .section-desc { font-size: 15px !important; line-height: 1.6 !important; }
    #skills-section { grid-template-columns: 1fr !important; gap: 20px !important; }
    .c-i, div[style*="gap: 60px"] { gap: 25px !important; flex-direction: column !important; align-items: center !important; text-align: center !important; }
    #contacto { padding: 80px 20px 60px !important; }
    #contacto div[style*="font-size: 12rem"], .c-w { font-size: 3.8rem !important; letter-spacing: 4px !important; opacity: 0.15 !important; }
    #contacto h2, .c-t { font-size: 2.22rem !important; }
    #contacto a[href^="mailto:"], .c-e { font-size: 1.15rem !important; word-break: break-all !important; border-bottom-width: 2px !important; }
    #contacto div[style*="display: flex; justify-content: center; gap: 20px"] { flex-direction: column !important; width: 100% !important; max-width: 320px !important; margin: 0 auto !important; gap: 12px !important; }
    #contacto a[style*="padding: 14px 32px"] { width: 100% !important; display: block !important; padding: 12px !important; font-size: 0.8rem !important; }
    .work-item { padding: 25px 0 !important; }
    .work-item .section-title { font-size: 1.5rem !important; }
    .cv-grid { grid-template-columns: 1fr !important; gap: 30px !important; }
    .cv-item { flex-direction: column !important; align-items: flex-start !important; gap: 10px !important; }
    .cv-date { width: auto !important; margin-bottom: 5px !important; }
  }
'''

MASTER_CONTACT_TEMPLATE = '''  <!-- CONTACTO -->
  <section id="contacto" style="background-image: url(\'{{PATH}}IMAGENES MIAS/dearriba.png\'); background-size: cover; background-position: center top; position: relative; padding: 120px 40px 60px; text-align: center; overflow: hidden;">
    
    <!-- Overlay oscuro (Z-INDEX 2) -->
    <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 2;"></div>
    
    <!-- Watermark (Z-INDEX 1 - Detrás del overlay) -->
    <div class="c-w" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12rem; font-weight: 900; font-family: \'Bebas Neue\', sans-serif; color: rgba(255,255,255,0.06); z-index: 1; pointer-events: none; white-space: nowrap; letter-spacing: 10px;">CONTACTO</div>
    
    <!-- Contenido (Z-INDEX 3) -->
    <div style="position: relative; z-index: 3;">
      <p style="color: #FF0000; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; font-family: \'Barlow Condensed\', sans-serif; margin-bottom: 16px;">— HABLEMOS —</p>
      <h2 class="c-t" style="color: #ffffff; font-size: 3.5rem; font-weight: 900; font-family: \'Bebas Neue\', sans-serif; text-transform: uppercase; line-height: 1.1; margin-bottom: 20px;">¿TENÉS UN PROYECTO?</h2>
      <p style="color: #ffffff; font-size: 1rem; max-width: 560px; margin: 0 auto 40px; line-height: 1.7; font-family: \'Barlow\', sans-serif;">Disponible para proyectos freelance, colaboraciones y trabajos de largo plazo. Desde el concepto hasta la ejecución.</p>
      <div style="margin-bottom: 50px;">
        <a href="mailto:vaalentinsanchez5@gmail.com" class="c-e" style="display: inline-block; color: #ffffff; font-size: 2.2rem; font-weight: 900; font-family: \'Bebas Neue\', sans-serif; text-transform: uppercase; text-decoration: none; letter-spacing: 2px; border-bottom: 3px solid #FF0000; padding-bottom: 8px;">VAALENTINSANCHEZ5@GMAIL.COM</a>
      </div>
      <div class="c-i" style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; margin-bottom: 50px; color: #ffffff; font-size: 0.85rem; letter-spacing: 1.5px; font-family: \'Barlow Condensed\', sans-serif; text-transform: uppercase;">
        <span>+54 9 351 555 8997 · TELÉFONO / WHATSAPP</span>
        <span>@VAALENSNCHZ · INSTAGRAM</span>
        <span>CÓRDOBA, ARGENTINA · UBICACIÓN</span>
      </div>
      <div class="c-b" style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <a href="https://wa.me/5493515558997" target="_blank" style="background: #FF0000; color: #ffffff; padding: 14px 32px; font-size: 0.85rem; font-weight: 700; font-family: \'Barlow Condensed\', sans-serif; letter-spacing: 2px; text-transform: uppercase; text-decoration: none; border: 2px solid #FF0000;">WHATSAPP</a>
        <a href="https://instagram.com/vaalensnchz" target="_blank" style="background: transparent; color: #ffffff; padding: 14px 32px; font-size: 0.85rem; font-weight: 700; font-family: \'Barlow Condensed\', sans-serif; letter-spacing: 2px; text-transform: uppercase; text-decoration: none; border: 2px solid #ffffff;">INSTAGRAM</a>
        <a href="https://drive.google.com/file/d/1IFJ14ORA0Bx63gSytOimdtCGJsHbDbLd/view?usp=sharing" target="_blank" style="background: transparent; color: #ffffff; padding: 14px 32px; font-size: 0.85rem; font-weight: 700; font-family: \'Barlow Condensed\', sans-serif; letter-spacing: 2px; text-transform: uppercase; text-decoration: none; border: 2px solid #ffffff;">DESCARGAR CV</a>
      </div>
    </div>
  </section>'''

def force_update(filepath, is_subpage=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Mobile Styles
    if 'MOBILE SYSTEM' not in content:
        # Append to the first <style> tag found
        content = re.sub(r'</style>', MOBILE_CSS + '\n</style>', content, count=1)
    
    # 2. Update Contact Section
    path_prefix = '../' if is_subpage else ''
    new_contact = MASTER_CONTACT_TEMPLATE.replace('{{PATH}}', path_prefix)
    
    # Search for <!-- CONTACTO --> and replace everything until </section>
    content = re.sub(r'<!-- CONTACTO -->\s*<section id="contacto".*?</section>', new_contact, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Force updated {filepath}")

# Process files
force_update('index.html')
force_update('curriculum.html')
force_update('kord3.html', is_subpage=True)

# Regenerate projects
print("Regenerating all 프로젝트 pages...")
os.system('python generate_pages.py')

print("All tasks completed successfully.")
