import re

with open('kord3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace colors
content = content.replace('#e63946', '#FF0000')
content = content.replace('#CC0000', '#FF0000')

# Replace marquee padding specifically in .mw
content = re.sub(r'\.mw\s*\{([^}]*?)padding:\s*18px\s*0;', r'.mw {\1padding: 25px 0;', content)

# Replace marquee font-size specifically in .mi
content = re.sub(r'\.mi\s*\{([^}]*?)font-size:\s*1.4rem;', r'.mi {\1font-size: 2.2rem;', content)

# Fix border-bottom 3 to 3px
content = content.replace('border-bottom: 3 solid #FF0000;', 'border-bottom: 3px solid #FF0000;')

with open('kord3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
