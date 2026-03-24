import os
import re

files = [
    'index.html', 'curriculum.html', 'agency.html', 'energia.html', 
    'home.html', 'kord3.html', 'mfsports.html', 'natan.html', 'otros.html'
]

css_block = """
    /* --- GLOBAL PARTICLES --- */
    #bg-particles {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 10000 !important; /* ON TOP OF EVERYTHING */
      pointer-events: none;
    }
"""

def update_file(filename):
    path = os.path.join(r'c:\Users\valen\Documents\PROYECTOS\PORTAFOLIO', filename)
    if not os.path.exists(path):
        print(f"Skipping {filename}, not found.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Script
    content = re.sub(r'length:\s*\d+', 'length: 300', content)
    content = re.sub(r'r:\s*Math\.random\(\)\s*\*\s*[\d.]+\s*\+\s*[\d.]+', 'r: Math.random() * 2 + 0.5', content)
    content = re.sub(r'op:\s*Math\.random\(\)\s*\*\s*[\d.]+\s*\+\s*[\d.]+', 'op: Math.random() * 0.5 + 0.1', content)

    # 2. Update/Add CSS
    if '#bg-particles' in content:
        # Replace the existing block
        content = re.sub(r'#bg-particles\s*{[^}]+}', css_block.strip().replace('/* --- GLOBAL PARTICLES --- */', '').strip(), content, flags=re.DOTALL)
    else:
        # Add before closing style tag
        content = content.replace('</style>', css_block + '\n  </style>', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in files:
    update_file(f)
