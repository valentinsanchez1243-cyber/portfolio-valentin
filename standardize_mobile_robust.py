import os
import re

files = [
    "index.html",
    "curriculum.html",
    "agency.html",
    "energia.html",
    "home.html",
    "kord3.html",
    "mfsports.html",
    "natan.html",
    "otros.html"
]

# Robust mobile CSS that covers Index, Curriculum and Project subpages
mobile_css = """
    /* --- ULTIMATE ROBUST MOBILE OVERHAUL --- */
    @media (max-width: 768px) {
      body {
        cursor: auto !important;
        overflow-x: hidden !important;
      }
      #cursor, .trail, .trp, #cd, #cr, #hero-dust, .nav-p {
        display: none !important;
      }

      nav {
        display: flex !important;
        justify-content: space-between !important;
        padding: 15px 20px !important;
        background: rgba(8, 8, 8, .98) !important;
        position: fixed !important;
        top: 0 !important;
        width: 100% !important;
        z-index: 5000 !important;
      }

      .nls {
        display: none !important;
      }

      .mtog {
        display: block !important;
        position: fixed !important;
        top: 20px !important;
        right: 20px !important;
        z-index: 6000 !important;
      }

      .back-btn {
        position: fixed !important;
        top: 80px !important;
        left: 20px !important;
        padding: 8px 14px !important;
        font-size: 0.8rem !important;
        display: inline-block !important;
        z-index: 4999 !important;
      }

      /* Hero Sections (Both Index and Project Pages) */
      #hero, .hero-banner {
        height: auto !important;
        min-height: 400px !important;
        padding: 100px 20px 40px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
      }

      .hero-cutout {
        display: none !important; /* Hide complex cutout on mobile */
      }

      .hero-banner-content, .hc {
        position: relative !important;
        width: 100% !important;
        bottom: 0 !important;
        left: 0 !important;
        transform: none !important;
        display: block !important;
      }

      .hero-title, .hn, .cv-title, .hero-banner .hero-title {
        font-size: 3.2rem !important;
        line-height: 1 !important;
        margin-top: 10px !important;
        display: block !important;
      }

      .hero-sub, .hro, .hsub, .hs {
        font-size: 0.85rem !important;
        margin-top: 12px !important;
        display: block !important;
        color: #ddd !important;
        max-width: 100% !important;
      }

      /* Sections and Titles */
      section {
        padding: 60px 20px !important;
      }

      .section-title, .st, .ht {
        font-size: 2rem !important;
        line-height: 1.1 !important;
      }

      /* Grids and Layouts */
      .sb { grid-template-columns: repeat(2, 1fr) !important; padding: 40px 20px !important; }
      .eg, .pg, .cg, .cv-grid, .cvw, .prg, .lgg { grid-template-columns: 1fr !important; gap: 20px !important; }

      /* Timeline / Experience for Index and CV */
      .exi {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
        padding: 24px 0 !important;
        padding-left: 15px !important;
        border-left: 2px solid var(--r) !important;
      }

      .exp {
        font-size: 0.8rem !important;
        margin-bottom: 5px !important;
      }

      .exro { font-size: 1.4rem !important; }

      /* Modals */
      .md2 {
        max-width: 95% !important;
        padding: 0 !important;
      }
      .mh, .mb { padding: 25px 20px !important; }
      
      /* Footer */
      footer {
        flex-direction: column !important;
        gap: 15px !important;
        text-align: center !important;
      /* Footer */
      footer {
        flex-direction: column !important;
        gap: 15px !important;
        text-align: center !important;
        padding: 30px 20px !important;
      }
    }

    /* --- GLOBAL PARTICLES --- */
    #bg-particles {
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1; /* Above body background, below content */
      pointer-events: none;
    }

    /* Standard content sections should be ABOVE particles */
    section, .sb, .mw, .mo, #hero, .hero-banner {
      position: relative;
      z-index: 2; 
    }
    
    /* Hero specific layers for Index and Projects */
    .hg, .hgl { z-index: 1; }
    .hero-cutout { z-index: 5 !important; position: absolute !important; }
    .hc, .hero-banner-content { z-index: 6 !important; position: relative !important; }

    /* Custom Cursor & Nav MUST maintain their original position/z-index */
    nav { z-index: 5000 !important; }
    #cd, #cr, #cursor, .trail, .trp { z-index: 9999 !important; }
"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Look for existing media queries for max-width 768px, 800px, 1000px and comment them out
        pattern = r'@media\s*\(\s*max-width\s*:\s*(768|800|1000)px\s*\)\s*\{'
        
        def find_closing_brace(text, start_index):
            count = 0
            for i in range(start_index, len(text)):
                if text[i] == '{':
                    count += 1
                elif text[i] == '}':
                    count -= 1
                    if count == 0:
                        return i
            return -1

        temp_content = content
        matches = list(re.finditer(pattern, temp_content))
        # Process matches in reverse
        for match in reversed(matches):
            start = match.start()
            end = find_closing_brace(temp_content, start)
            if end != -1:
                temp_content = temp_content[:start] + "/* OLD MOBILE BLOCKED */ " + temp_content[end+1:]

        # 2. Append our new robust CSS before the closing </style> tag
        if '</style>' in temp_content:
            parts = temp_content.split('</style>')
            # Take the last closing style tag to catch the main block
            final_parts = ['</style>'.join(parts[:-1]), parts[-1]]
            temp_content = final_parts[0] + "\n" + mobile_css + "\n</style>" + final_parts[1]

        # 3. Inject Global Particles JS before closing </body>
        particles_js = """
  <script>
    (function initGlobalParticles() {
      if (document.getElementById('bg-particles')) return;
      const canvas = document.createElement('canvas');
      canvas.id = 'bg-particles';
      document.body.prepend(canvas);
      function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
      resize(); window.addEventListener('resize', resize);
      const ctx = canvas.getContext('2d');
      const particles = Array.from({ length: 80 }, () => ({
        x: Math.random() * window.innerWidth, y: Math.random() * window.innerHeight,
        vx: (Math.random() - 0.5) * 0.3, vy: -(Math.random() * 0.4 + 0.1),
        r: Math.random() * 1.5 + 0.5, op: Math.random() * 0.3 + 0.1, life: Math.random()
      }));
      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
          p.x += p.vx; p.y += p.vy; p.life -= 0.002;
          if (p.y < -10 || p.life <= 0) { p.y = canvas.height + 10; p.x = Math.random() * canvas.width; p.life = 1; }
          ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255,0,0,${(p.op * p.life).toFixed(3)})`; ctx.fill();
        });
        requestAnimationFrame(draw);
      }
      draw();
    })();
  </script>
"""
        # If already has initGlobalParticles, remove it and re-inject (or just don't re-inject if preferred)
        # To be safe, we'll replace the existing block or append if missing
        if 'initGlobalParticles' in temp_content:
            # Simple way: find the script block and replace it
            temp_content = re.sub(r'\n\s*<script>\s*\(function initGlobalParticles\(\).*?<\/script>', '', temp_content, flags=re.DOTALL)
        
        if '</body>' in temp_content:
            temp_content = temp_content.replace('</body>', particles_js + '\n</body>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(temp_content)
        print(f"Updated {filename}")
