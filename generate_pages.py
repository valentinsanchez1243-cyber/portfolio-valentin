import os
import re

base_dir = r"c:\Users\valen\Documents\PROYECTOS\PORTAFOLIO"

projects = {
    'agency.html': {
        'title': 'Agency Luxury - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-AGENCY.png',
        'desc': 'Trabajé como editor de video para Agency Luxury, una agencia de marketing con base en Buenos Aires especializada en el nicho de cirujanos plásticos. Mi rol estuvo enfocado en la edición de contenido audiovisual orientado a conversión, abordando cada pieza desde lo visual y lo estratégico. Realicé la edición de VSL (Video Sales Letters) y anuncios para Facebook Ads, optimizando ritmo, estructura, subtítulos y narrativa para mejorar la retención y el rendimiento de las campañas. Además, diseñé portadas (thumbnails y covers) para videos y anuncios, priorizando impacto visual, claridad del mensaje y coherencia con la identidad de cada marca. Trabajé en conjunto con el equipo de marketing, adaptando el contenido a objetivos comerciales concretos y manteniendo un estándar visual profesional alineado al posicionamiento premium del nicho médico.',
        'tags': ['EDICIÓN DE VIDEO', 'FACEBOOK ADS', 'VSL', 'THUMBNAILS', 'CONTENIDO PUBLICITARIO'],
        'list': [
            ('VSL & ANUNCIOS FACEBOOK ADS', 'https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=sharing'),
            ('THUMBNAILS & COVERS', 'https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=sharing'),
            ('CONTENIDO AUDIOVISUAL', 'https://drive.google.com/drive/folders/1IcUsqJ8yI4Taq-THSqp2ZrRZW80lawnv?usp=sharing')
        ],
        'hype': None,
        'ig_handle': '@LUXURY.AGENCY_LLC',
        'ig_link': 'https://www.instagram.com/luxury.agency_llc/'
    },
    'energia.html': {
        'title': 'Energía Fitness - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-ENERGIA.jpg',
        'desc': 'Trabajé en el rebranding y relanzamiento integral de Energía Fitness, redefiniendo la identidad visual y la comunicación de la marca en redes sociales. El proyecto comenzó con la reconstrucción total de la cuenta, reorganizando la presentación, el feed y el tono visual para darle una imagen clara, profesional y coherente. Me encargué de la edición de carruseles, videos y piezas gráficas, del rediseño de historias destacadas, y de la planificación de contenidos alineados a la nueva identidad. Además, llevé adelante la dirección y producción audiovisual completa, desde la idea y el concepto hasta la grabación y edición final.',
        'tags': ['REBRANDING', 'DIRECCIÓN CREATIVA', 'AUDIOVISUAL', 'REDES SOCIALES', 'CONTENIDO'],
        'list': [
            ('IDENTIDAD VISUAL & REBRANDING', 'https://drive.google.com/drive/folders/1Wm3IiHyRxUaHtxe2_hucsiBFcSka26sX?usp=sharing'),
            ('VIDEO DE PRESENTACIÓN', 'https://drive.google.com/drive/folders/1Wm3IiHyRxUaHtxe2_hucsiBFcSka26sX?usp=sharing'),
            ('CONTENIDO DE INSTAGRAM', 'https://drive.google.com/drive/folders/1Wm3IiHyRxUaHtxe2_hucsiBFcSka26sX?usp=sharing'),
            ('PLANTILLAS HISTORIAS DESTACADAS', 'https://drive.google.com/drive/folders/1Wm3IiHyRxUaHtxe2_hucsiBFcSka26sX?usp=sharing')
        ],
        'hype': {
            'title': 'SEMANA HYPE',
            'desc': 'Estrategia de contenido previa pensada para generar expectativa y atención antes de la presentación oficial. Produjimos y publicamos videos, posts e historias diseñados para despertar curiosidad y preparar a la audiencia, construyendo misterio y anticipación de forma progresiva. El cierre fue un video de presentación grabado desde cero que funcionó como pieza principal del relanzamiento.',
            'link': 'https://drive.google.com/drive/folders/1Wm3IiHyRxUaHtxe2_hucsiBFcSka26sX?usp=sharing'
        },
        'ig_handle': '@ENERGIAFITNESS.CBA',
        'ig_link': 'https://www.instagram.com/energiafitness.cba/'
    },
    'mfsports.html': {
        'title': 'MF Sports - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-MFSPORTS.png',
        'desc': 'Trabajé en el diseño de indumentaria deportiva para MF Sports, desarrollando conjuntos completos para fútbol y hockey, incluyendo camisetas, musculosas, buzos y equipamiento. El enfoque estuvo puesto en la identidad visual, la coherencia estética y la adaptación del diseño a cada equipo y necesidad específica. Además, realicé presentaciones visuales para sponsors, diseñadas para comunicar de forma clara y profesional la propuesta de la marca, sus productos y su valor comercial, facilitando su presentación ante posibles aliados y patrocinadores.',
        'tags': ['DISEÑO DE INDUMENTARIA', 'FÚTBOL', 'HOCKEY', 'SPONSORS', 'IDENTIDAD VISUAL'],
        'list': [
            ('DISEÑO DE CAMISETAS & CONJUNTOS', 'https://www.instagram.com/mfsports.ar/'),
            ('PRESENTACIONES PARA SPONSORS', 'https://www.instagram.com/mfsports.ar/')
        ],
        'hype': None,
        'ig_handle': '@MFSPORTS.AR',
        'ig_link': 'https://www.instagram.com/mfsports.ar/'
    },
    'home.html': {
        'title': 'Home Improvement Power - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-HOME.jpg',
        'desc': 'Actualmente trabajo con HomeImprovementPower, empresa del sector home improvement con base en Florida (EE. UU.), colaborando en la creación de contenido audiovisual y piezas creativas para campañas publicitarias en redes sociales. Mi rol se centra en la edición de videos cortos para ads en Facebook e Instagram, con un enfoque estilo UGC/influencer, priorizando contenido dinámico y cercano. El objetivo principal es generar videos con ganchos fuertes en los primeros segundos, subtítulos claros, buen ritmo visual y llamados a la acción orientados a conversión. También trabajo en la creación de videos apoyados por IA, incluyendo voz en off con inteligencia artificial y generación de recursos audiovisuales para escalar volumen de contenido sin perder efectividad publicitaria.',
        'tags': ['EDICIÓN DE VIDEO', 'FACEBOOK ADS', 'INSTAGRAM ADS', 'UGC', 'IA', 'CREATIVOS'],
        'list': [
            ('VIDEOS PARA ADS', 'https://drive.google.com/drive/folders/193iJy2NcTXkWi0dD5RpDsDyWeLwX5fFV?usp=sharing'),
            ('VIDEOS CON INTELIGENCIA ARTIFICIAL', 'https://drive.google.com/drive/folders/193iJy2NcTXkWi0dD5RpDsDyWeLwX5fFV?usp=sharing'),
            ('FLYERS & CREATIVOS ESTÁTICOS', 'https://drive.google.com/drive/folders/193iJy2NcTXkWi0dD5RpDsDyWeLwX5fFV?usp=sharing')
        ],
        'hype': None,
        'ig_handle': '@HOMEIMPROVEMENTPOWER',
        'ig_link': 'https://www.instagram.com/homeimprovementpower/'
    },
    'natan.html': {
        'title': 'The Natan Barber Estudio - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-NATAN.jpg',
        'desc': 'Trabajé en el desarrollo del branding y el lanzamiento completo de la comunicación digital de The Natan Barber Studio, construyendo la identidad visual y el estilo de la marca desde cero. El proyecto incluyó definir el tono, la estética y la presencia en redes sociales. Produje, dirigí y edité contenido audiovisual desde cero, incluyendo un video de presentación con eje conceptual en el cuarteto, incorporando un elemento cultural fuerte y local para conectar con la identidad de la marca y su público. También edité carruseles, piezas gráficas y diseñé stickers para ceras, extendiendo la identidad visual al producto físico.',
        'tags': ['BRANDING', 'DIRECCIÓN CREATIVA', 'AUDIOVISUAL', 'REDES SOCIALES', 'DISEÑO GRÁFICO'],
        'list': [
            ('IDENTIDAD VISUAL & BRANDING', 'https://drive.google.com/drive/folders/1ayGPRBRxmenzvTuW6wfJhDH-5xB8MN9q?usp=sharing'),
            ('VIDEO DE PRESENTACIÓN', 'https://drive.google.com/drive/folders/1ayGPRBRxmenzvTuW6wfJhDH-5xB8MN9q?usp=sharing'),
            ('STICKERS & DISEÑO GRÁFICO', 'https://drive.google.com/drive/folders/1ayGPRBRxmenzvTuW6wfJhDH-5xB8MN9q?usp=sharing')
        ],
        'hype': {
            'title': 'SEMANA HYPE',
            'desc': 'Estrategia previa al lanzamiento basada en la producción y publicación planificada de videos, posts e historias. Pensada para generar expectativa, misterio y atención progresiva antes de la presentación oficial del estudio y su identidad.',
            'link': 'https://drive.google.com/drive/folders/1ayGPRBRxmenzvTuW6wfJhDH-5xB8MN9q?usp=sharing'
        },
        'ig_handle': '@NATAN.BARBER.ESTUDIO',
        'ig_link': 'https://www.instagram.com/natan.barber.estudio/'
    },
    'otros.html': {
        'title': 'Otros Proyectos - Valentín Sánchez',
        'hero_img': '../PORTADA PROYECTOS/PORTADA-OTROS.jpg',
        'desc': 'Además de los proyectos principales, trabajé en la edición de contenido audiovisual para distintas marcas y empresas, adaptando cada pieza a su rubro, público y objetivo comunicacional.',
        'tags': ['EDICIÓN DE VIDEO', 'COMUNICACIÓN DIGITAL', 'REDES SOCIALES', 'ADS'],
        'list': [
            ('ZETTA SECURITY — Cámaras de seguridad, Córdoba', 'https://www.instagram.com/zettasecurity.ht/'),
            ('FARMACIA PAVAN — Farmacia, Córdoba', 'https://www.instagram.com/farmaciapavan/'),
            ('LEGAL LEADS — Estudio jurídico, Chile', 'https://www.instagram.com/legal.leadsmkt/'),
            ('VER TODOS LOS VIDEOS', 'https://drive.google.com/drive/folders/1pS9hHRjSssUQIilfyibPq_kYH52Ov9ru?usp=sharing')
        ],
        'hype': None,
        'ig_handle': '@VAALENSNCHZ',
        'ig_link': 'https://www.instagram.com/vaalensnchz/'
    }
}

def extract_hero_banner(content):
    start = content.find('<div class="hero-banner">')
    if start == -1: return ""
    count = 1
    idx = start + len('<div class="hero-banner">')
    while count > 0 and idx < len(content):
        next_open = content.find('<div', idx)
        next_close = content.find('</div', idx)
        if next_open != -1 and next_open < next_close:
            count += 1
            idx = next_open + 4
        elif next_close != -1:
            count -= 1
            idx = next_close + 6
        else: break
    return content[start:idx]

# Read template once
with open(os.path.join(base_dir, 'kord3.html'), 'r', encoding='utf-8') as f:
    shared_template = f.read()

def generate_html(filename, data):
    template = str(shared_template)
    original_path = os.path.join(base_dir, filename)
    with open(original_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    new_content = re.sub(r'<title>[^<]*</title>', f'<title>{data["title"]}</title>', template)

    # Update hero banner background image in style tag (specifically the one with the background image)
    hero_pattern = r"(\.hero-banner\s*\{[^}]*?background-image:\s*url\(')[^']*('\);)"
    new_content = re.sub(hero_pattern, r"\1" + data['hero_img'] + r"\2", new_content)

    hero_banner = extract_hero_banner(original_content)
    if hero_banner:
        new_content = re.sub(r'<!-- SECCIÓN 1: HERO BANNER -->\s*<div class="hero-banner">[\s\S]*?</div>\s*</div>\s*<!-- SECCIÓN 2: DESCRIPCIÓN -->', f'<!-- SECCIÓN 1: HERO BANNER -->\n{hero_banner}\n\n<!-- SECCIÓN 2: DESCRIPCIÓN -->', new_content)

    desc_html = f'<p class="section-desc" style="margin-bottom:0;">\n    {data["desc"]}\n  </p>'
    new_content = re.sub(r'<p class="section-desc" style="margin-bottom:0;">.*?</p>', desc_html, new_content, flags=re.DOTALL)

    tags_html = '\n    '.join([f'<span class="tag">{tag}</span>' for tag in data['tags']])
    new_content = re.sub(r'<div class="tag-list">.*?</div>', f'<div class="tag-list">\n    {tags_html}\n  </div>', new_content, count=1, flags=re.DOTALL)

    items_html = ""
    for title, link in data['list']:
        items_html += f'''    <div class="work-item">
      <h2 class="section-title">{title}</h2>
      <a href="{link}" target="_blank" class="btn-red">VER →</a>
    </div>\n'''
    new_content = re.sub(r'<div class="work-list">[\s\S]*?</div>\s*</section>', f'<div class="work-list">\n{items_html}  </div>\n</section>', new_content)

    if data['hype']:
        hype_html = f'''<!-- SECCIÓN 4: SEMANA HYPE -->
<div class="hype-wrapper reveal">
  <div class="hype-inner">
    <div class="section-subtitle">— ESTRATEGIA DE LANZAMIENTO</div>
    <h2 class="hype-title">{data["hype"]["title"]}</h2>
    <p class="section-desc">
      {data["hype"]["desc"]}
    </p>
    <a href="{data["hype"]["link"]}" target="_blank" class="btn-red">VER CONTENIDO →</a>
  </div>
</div>'''
        new_content = re.sub(r'<!-- SECCIÓN 4: SEMANA HYPE -->[\s\S]*?<!-- SECCIÓN 5: INSTAGRAM -->', f'{hype_html}\n\n<!-- SECCIÓN 5: INSTAGRAM -->', new_content)
    else:
        new_content = re.sub(r'<!-- SECCIÓN 4: SEMANA HYPE -->[\s\S]*?<!-- SECCIÓN 5: INSTAGRAM -->', '<!-- SECCIÓN 5: INSTAGRAM -->', new_content)

    new_content = re.sub(r'<div class="instagram-handle">[^<]*</div>', f'<div class="instagram-handle">{data["ig_handle"]}</div>', new_content)
    new_content = re.sub(r'<a href="[^"]*" target="_blank" class="btn-outline-red">VER INSTAGRAM →</a>', f'<a href="{data["ig_link"]}" target="_blank" class="btn-outline-red">VER INSTAGRAM →</a>', new_content)

    with open(original_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")

for filename, data in projects.items():
    if filename == 'kord3.html':
        continue
    print(f"Generating {filename}...")
    generate_html(filename, data)
