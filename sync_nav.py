import os
import re

files = [
    "index.html",
    "curriculum.html",
    "kord3.html",
    "agency.html",
    "mfsports.html",
    "home.html",
    "opero.html",
    "natan.html",
    "energia.html",
    "manblue.html",
    "woldi.html",
    "lluviaconsol.html"
]

# Patterns for Task 8 (Nav Update)
# 1. Desktop Nav Links
# <li><a href="otros.html">Otros Clientes</a></li> -> <li><a href="manblue.html">Man Blue FC</a></li>
# 2. Mobile Overlay Links
# <a href="otros.html" onclick="toggleMenu()">Otros</a> -> <a href="manblue.html" onclick="toggleMenu()">Man Blue</a>

def update_nav(content):
    # Desktop Nav
    # We look for links to otros.html and replace them. 
    # The text might vary (Otros Clientes, otros, etc.), but the user said "Add link to manblue.html in the same position".
    
    # Pattern for li/a combo
    content = re.sub(r'<li><a href="otros.html".*?</a></li>', '<li><a href="manblue.html">Man Blue FC</a></li>', content, flags=re.IGNORECASE)
    
    # Pattern for standalone a (mobile menu)
    content = re.sub(r'<a href="otros.html".*?</a>', '<a href="manblue.html" onclick="toggleMenu()">Man Blue FC</a>', content, flags=re.IGNORECASE)
    
    return content

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = update_nav(content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated nav in {filename}")
        else:
            print(f"No nav changes needed in {filename}")
