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
        padding: 30px 20px !important;
      }
    }
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
            # Take the last closing style tag
            final_parts = ['</style>'.join(parts[:-1]), parts[-1]]
            new_content = final_parts[0] + "\n" + mobile_css + "\n</style>" + final_parts[1]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Purged and updated {filename}")
