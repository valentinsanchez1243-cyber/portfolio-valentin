import re
import os

# Bloque Mobile CSS Premium
MOBILE_CSS = '''
  /* --- PREMIUM MOBILE & UX SYSTEM --- */
  :root {
    --fs-h1: clamp(3.2rem, 10vw, 7.5rem);
    --fs-h2: clamp(2.2rem, 6vw, 4rem);
    --fs-h3: clamp(1.5rem, 4vw, 2.22rem);
    --fs-body: clamp(0.9rem, 2vw, 1.05rem);
  }

  .rv { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
  .rv.vi { opacity: 1; transform: translateY(0); }

  @media (max-width: 768px) {
    body { background-size: 30px 30px; cursor: default !important; }
    #cd, #cr, #cursor, .trail, .trp { display: none !important; }
    nav { padding: 15px 25px !important; background: rgba(8, 8, 8, .98) !important; }
    .nls { display: none !important; }
    .mtog { display: block !important; }
    .hero-title, .ht, h1, .hero-banner-content .hero-title, .cv-title { font-size: 3.5rem !important; line-height: 1 !important; }
    .hero-sub, .hs { font-size: 13px !important; letter-spacing: 2px !important; }
    .hero-banner { height: 350px !important; padding: 40px 20px !important; }
    .mi { font-size: 1.4rem !important; padding: 0 15px !important; }
    .mw { padding: 15px 0 !important; }
    section, .hype-inner, .instagram-section { padding: 60px 25px !important; }
    .section-title, h2, .hype-title { font-size: 2.2rem !important; }
    .section-desc { font-size: 16px !important; line-height: 1.6 !important; }
    #skills-section { grid-template-columns: 1fr !important; gap: 20px !important; }
    .c-i, div[style*="gap: 60px"] { gap: 25px !important; flex-direction: column !important; align-items: center !important; text-align: center !important; }
    #contacto { padding: 80px 25px 60px !important; }
    #contacto div[style*="font-size: 12rem"], .c-w { font-size: 3.8rem !important; letter-spacing: 4px !important; opacity: 0.1 !important; }
    #contacto a[href^="mailto:"], .c-e { font-size: 1.15rem !important; word-break: break-all !important; border-bottom-width: 2px !important; }
    #contacto div[style*="display: flex; justify-content: center; gap: 20px"] { flex-direction: column !important; width: 100% !important; margin: 0 auto !important; gap: 12px !important; }
    #contacto a[style*="padding: 14px 32px"] { width: 100% !important; display: block !important; padding: 12px !important; font-size: 0.8rem !important; backdrop-filter: blur(5px); background: rgba(255,0,0,0.1) !important; border-color: #FF0000 !important; }
    #contacto a[style*="background: #FF0000"] { background: #FF0000 !important; }
    .cv-grid { grid-template-columns: 1fr !important; gap: 30px !important; }
  }

  /* MENU ELEMENTS */
  .mtog { display: none; background: none; border: none; padding: 10px; z-index: 6000; cursor: pointer; }
  .mtog span { display: block; width: 25px; height: 2px; background: var(--w); margin: 5px 0; transition: .3s; }
  .mtog.active span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
  .mtog.active span:nth-child(2) { opacity: 0; }
  .mtog.active span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
  
  .movl { position: fixed; inset: 0; background: rgba(8,8,8,0.98); backdrop-filter: blur(10px); z-index: 5500; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; opacity: 0; pointer-events: none; transition: opacity .4s cubic-bezier(0.16, 1, 0.3, 1); }
  .movl.active { opacity: 1; pointer-events: auto; }
  .movl a { font-family: 'Bebas Neue', sans-serif; font-size: 2.5rem; letter-spacing: 4px; color: var(--w); text-decoration: none; transition: .3s; }
  .movl a:hover { color: var(--r); }
'''

# Script JS Premium
PREMIUM_JS = '''
    // === PREMIUM UX SYSTEM ===
    const mtog = document.getElementById('mtog');
    const movl = document.getElementById('movl');
    function toggleMenu() {
      movl.classList.toggle('active');
      mtog.classList.toggle('active');
      document.body.style.overflow = movl.classList.contains('active') ? 'hidden' : '';
    }
    if(mtog) mtog.addEventListener('click', toggleMenu);

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('vi'); }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.rv').forEach(el => observer.observe(el));
'''

MASTER_CONTACT_TEMPLATE = '''  <!-- CONTACTO -->
  <section id="contacto" class="rv" style="background-image: url(\'{{PATH}}IMAGENES MIAS/dearriba.png\'); background-size: cover; background-position: center top; position: relative; padding: 120px 40px 60px; text-align: center; overflow: hidden;">
    <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.55); z-index: 2;"></div>
    <div class="c-w" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 12rem; font-weight: 900; font-family: \'Bebas Neue\', sans-serif; color: rgba(255,255,255,0.06); z-index: 1; pointer-events: none; white-space: nowrap; letter-spacing: 10px;">CONTACTO</div>
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

    # 1. Update Styles
    if 'PREMIUM MOBILE' not in content:
        content = re.sub(r'</style>', MOBILE_CSS + '\n</style>', content, count=1)
    
    # 2. Update Nav to include Toggle
    if 'mtog' not in content:
        nav_match = re.search(r'(<nav id="nav">.*?</nav>)', content, re.DOTALL)
        if nav_match:
            old_nav = nav_match.group(1)
            new_nav = old_nav.replace('</nav>', '  <button class="mtog" id="mtog"><span></span><span></span><span></span></button>\n  </nav>')
            # Add Overlay after Nav
            overlay = f'\\n  <!-- MOBILE OVERLAY -->\\n  <div class="movl" id="movl">\\n    <a href="{"../" if is_subpage else ""}index.html#proyectos" onclick="toggleMenu()">Proyectos</a>\\n    <a href="{"../" if is_subpage else ""}index.html#experiencia" onclick="toggleMenu()">Experiencia</a>\\n    <a href="{"../" if is_subpage else ""}curriculum.html" onclick="toggleMenu()">Currículum</a>\\n    <a href="{"../" if is_subpage else ""}index.html#contacto" onclick="toggleMenu()" style="color:var(--r)">Contacto</a>\\n  </div>'
            content = content.replace(old_nav, new_nav + overlay.replace('\\n', '\n'))

    # 3. Add Reveal classes to sections
    content = content.replace('<section id="proyectos"', '<section id="proyectos" class="rv"')
    content = content.replace('<section id="experiencia"', '<section id="experiencia" class="rv"')
    content = content.replace('<section id="servicios"', '<section id="servicios" class="rv"')
    content = content.replace('.prs', '.prs rv') # Procesos

    # 4. Update JS
    if 'PREMIUM UX SYSTEM' not in content:
        content = re.sub(r'</script>', PREMIUM_JS + '\n</script>', content, count=1)

    # 5. Update Contact Section
    path_prefix = '../' if is_subpage else ''
    new_contact = MASTER_CONTACT_TEMPLATE.replace('{{PATH}}', path_prefix)
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
