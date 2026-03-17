import os

files = [
    "agency.html",
    "energia.html",
    "home.html",
    "kord3.html",
    "mfsports.html",
    "natan.html",
    "otros.html"
]

mobile_css = """
    /* --- ULTIMATE MOBILE OVERHAUL --- */
    @media (max-width: 768px) {
      body {
        cursor: auto !important;
      }
      #cursor, .trail {
        display: none !important;
      }

      nav {
        padding: 15px 20px !important;
        background: rgba(8, 8, 8, .98) !important;
      }

      .back-btn {
        top: 75px !important;
        left: 20px !important;
        padding: 8px 14px !important;
        font-size: 0.8rem !important;
      }

      .hero-banner {
        height: 350px !important;
        padding: 40px 20px !important;
        background-position: center !important;
      }

      .hero-banner::before {
        background: linear-gradient(to top, rgba(10, 10, 10, 1) 10%, rgba(10, 10, 10, 0.4) 100%) !important;
      }

      .hero-title {
        font-size: 3.2rem !important;
        line-height: 1 !important;
      }

      .hero-sub {
        font-size: 0.85rem !important;
        margin-top: 8px !important;
      }

      section {
        padding: 60px 20px !important;
      }

      .section-title {
        font-size: 1.8rem !important;
      }
    }
"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for the end of the mobile system block or end of style
        if '</style>' in content:
            # We append our ultimate overhaul before the closing style tag to ensure it overrides
            parts = content.split('</style>')
            new_content = parts[0] + "\n" + mobile_css + "\n</style>" + parts[1]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
