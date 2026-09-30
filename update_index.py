import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# CSS REPLACEMENT
old_css_pattern = r"/\* ---- TABS STACK ---- \*/\s*\.ptabs \{.*?\.ptab\.is-open \.ptab-arrow \{.*?\}"
new_css = """/* ---- TABS STACK ---- */
.ptabs {
  display: flex;
  flex-direction: column;
  gap: 0;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 4px;
  overflow: hidden;
}

.ptab {
  position: relative;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.ptab:last-child { border-bottom: none; }

/* ---- HEADER ROW (always visible) ---- */
.ptab-hd {
  height: 88px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 0;
  padding: 0;
  cursor: pointer;
  user-select: none;
  position: relative;
  overflow: hidden;
  transition: background 0.3s;
}

/* Barra de color izquierda — más gruesa, más visible */
.ptab-hd::before {
  content: '';
  width: 5px;
  height: 100%;
  flex-shrink: 0;
  transition: width 0.3s;
}
#ptab-branding .ptab-hd::before     { background: #FF0000; }
#ptab-videos .ptab-hd::after        { display: none; }
#ptab-videos .ptab-hd::before       { background: #0EA5E9; }
#ptab-community .ptab-hd::before    { background: #FFD700; }
#ptab-indumentaria .ptab-hd::before { background: #8B5CF6; }

.ptab:hover .ptab-hd::before   { width: 7px; }
.ptab.is-open .ptab-hd::before { width: 9px; }

/* Fondo de color sutil al hover/abrir */
#ptab-branding .ptab-hd:hover,
#ptab-branding.is-open .ptab-hd     { background: rgba(255,0,0,0.055); }
#ptab-videos .ptab-hd:hover,
#ptab-videos.is-open .ptab-hd       { background: rgba(14,165,233,0.055); }
#ptab-community .ptab-hd:hover,
#ptab-community.is-open .ptab-hd    { background: rgba(255,215,0,0.055); }
#ptab-indumentaria .ptab-hd:hover,
#ptab-indumentaria.is-open .ptab-hd { background: rgba(139,92,246,0.055); }

/* Gradiente overlay de fondo */
.ptab-hd-bg {
  position: absolute; inset: 0;
  opacity: 0;
  transition: opacity 0.4s;
  pointer-events: none;
}
#ptab-branding .ptab-hd-bg     { background: linear-gradient(90deg, rgba(255,0,0,0.10) 0%, transparent 55%); }
#ptab-videos .ptab-hd-bg       { background: linear-gradient(90deg, rgba(14,165,233,0.10) 0%, transparent 55%); }
#ptab-community .ptab-hd-bg    { background: linear-gradient(90deg, rgba(255,215,0,0.10) 0%, transparent 55%); }
#ptab-indumentaria .ptab-hd-bg { background: linear-gradient(90deg, rgba(139,92,246,0.10) 0%, transparent 55%); }
.ptab-hd:hover .ptab-hd-bg, .ptab.is-open .ptab-hd .ptab-hd-bg { opacity: 1; }

.ptab-idx {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 0.58rem;
  letter-spacing: 3px;
  color: #fff;
  opacity: 0.2;
  flex-shrink: 0;
  transition: opacity 0.3s;
  position: relative;
  z-index: 1;
}
.ptab.is-open .ptab-idx { opacity: 0.5; }

.ptab-hd-bar {
  width: 1px;
  height: 26px;
  background: rgba(255,255,255,0.15);
  flex-shrink: 0;
  margin: 0 18px;
  transition: height 0.3s;
  position: relative;
  z-index: 1;
}
.ptab:hover .ptab-hd-bar   { height: 36px; }
.ptab.is-open .ptab-hd-bar { height: 44px; background: rgba(255,255,255,0.25); }

.ptab-icon {
  width: 56px;
  height: 88px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}
.ptab-icon svg {
  width: 22px;
  height: 22px;
  opacity: 0.28;
  transition: opacity 0.3s;
}
#ptab-branding .ptab-icon svg     { stroke: #FF0000; }
#ptab-videos .ptab-icon svg       { stroke: #0EA5E9; }
#ptab-community .ptab-icon svg    { stroke: #FFD700; }
#ptab-indumentaria .ptab-icon svg { stroke: #8B5CF6; }
.ptab:hover .ptab-icon svg   { opacity: 0.7; }
.ptab.is-open .ptab-icon svg { opacity: 1; }

.ptab-name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.85rem;
  letter-spacing: 8px;
  color: #fff;
  opacity: 0.45;
  transition: opacity 0.25s, letter-spacing 0.3s;
  flex: 1;
  position: relative;
  z-index: 1;
  line-height: 1;
}
.ptab:hover .ptab-name   { opacity: 0.9; letter-spacing: 9px; }
.ptab.is-open .ptab-name { opacity: 1;   letter-spacing: 9px; }

.ptab-arrow {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 32px;
  flex-shrink: 0;
  font-size: 0.9rem;
  color: rgba(255,255,255,0.3);
  transition: transform 0.45s cubic-bezier(0.4,0,0.2,1), border-color 0.3s, color 0.3s, background 0.3s;
  position: relative;
  z-index: 1;
}
.ptab.is-open .ptab-arrow {
  transform: rotate(180deg);
  border-color: rgba(255,0,0,0.5);
  color: #FF0000;
  background: rgba(255,0,0,0.08);
}
#ptab-videos.is-open .ptab-arrow    { border-color: rgba(14,165,233,0.5); color: #0EA5E9; background: rgba(14,165,233,0.08); }
#ptab-community.is-open .ptab-arrow { border-color: rgba(255,215,0,0.5);  color: #FFD700; background: rgba(255,215,0,0.08); }
#ptab-indumentaria.is-open .ptab-arrow { border-color: rgba(139,92,246,0.5); color: #8B5CF6; background: rgba(139,92,246,0.08); }"""

content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

# HTML REPLACEMENT
html_pattern = r'(<span class="ptab-arrow">↓</span>\s*)(</div>)'
new_html = r'\1<div class="ptab-hd-bg"></div>\n      \2'
content = re.sub(html_pattern, new_html, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Update complete.")
