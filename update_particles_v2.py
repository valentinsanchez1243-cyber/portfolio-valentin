import os
import re

files = [
    'index.html', 'curriculum.html', 'agency.html', 'energia.html', 
    'home.html', 'kord3.html', 'mfsports.html', 'natan.html', 'otros.html'
]

css_block = """    /* --- GLOBAL PARTICLES --- */
    #bg-particles {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 10000; /* ON TOP OF EVERYTHING */
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
    content = re.sub(r'r:\s*Math\.random\(\)\s*\*\s*1\.5\s*\+\s*0\.5', 'r: Math.random() * 2 + 0.5', content)
    content = re.sub(r'op:\s*Math\.random\(\)\s*\*\s*0\.3\s*\+\s*0\.1', 'op: Math.random() * 0.5 + 0.1', content)

    # 2. Update/Add CSS
    if '#bg-particles' in content:
        # Update existing z-index
        content = re.sub(r'z-index:\s*\d+;[^}]*#bg-particles', 'z-index: 10000; /* ON TOP OF EVERYTHING */', content, flags=re.DOTALL)
        # Or more simply, match the whole block
        content = re.sub(r'#bg-particles\s*{[^}]+}', css_block.strip(), content)
    else:
        # Add before first media query or before </style>
        if '@media' in content:
            content = content.replace('@media', css_block + '\n    @media', 1)
        else:
            content = content.replace('</style>', css_block + '\n  </style>', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in files:
    update_file(f)
