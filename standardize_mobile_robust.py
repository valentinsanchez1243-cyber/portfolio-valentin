import os
import re

files = [
    "agency.html",
    "energia.html",
    "home.html",
    "kord3.html",
    "mfsports.html",
    "natan.html",
    "otros.html"
]

# Robust mobile CSS using !important to override any loose rules
mobile_css = """
    /* --- ROBUST MOBILE OVERHAUL --- */
    @media (max-width: 768px) {
      body {
        cursor: auto !important;
      }
      #cursor, .trail, .trp, #cd, #cr {
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

      .hero-banner {
        height: 380px !important;
        padding: 40px 20px !important;
        background-position: center !important;
        display: flex !important;
        align-items: flex-end !important;
        justify-content: flex-start !important;
        text-align: left !important;
      }

      .hero-banner-content {
        position: relative !important;
        width: 100% !important;
        bottom: 0 !important;
        left: 0 !important;
        transform: none !important;
      }

      .hero-banner::before {
        background: linear-gradient(to top, rgba(10, 10, 10, 1) 15%, rgba(10, 10, 10, 0.4) 100%) !important;
      }

      .hero-title {
        font-size: 3.1rem !important;
        line-height: 1 !important;
        margin-top: 10px !important;
        display: block !important;
      }

      .hero-sub {
        font-size: 0.82rem !important;
        margin-top: 10px !important;
        display: block !important;
        color: #ddd !important;
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
        
        # 1. Look for existing media queries for max-width 768px or 800px and comment them out to avoid conflicts
        # This is a bit aggressive but ensures our new CSS is the only one active for mobile.
        pattern = r'@media\s*\(\s*max-width\s*:\s*(768|800)px\s*\)\s*\{'
        
        # We find each occurrence and its matching closing brace
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

        new_content = content
        matches = list(re.finditer(pattern, new_content))
        # Process matches in reverse to not mess up indices
        for match in reversed(matches):
            start = match.start()
            end = find_closing_brace(new_content, start)
            if end != -1:
                # Comment out the old media query
                block = new_content[start:end+1]
                new_content = new_content[:start] + "/* OLD MOBILE BLOCKED */ " + new_content[end+1:]

        # 2. Append our new robust CSS before the closing </style> tag
        if '</style>' in new_content:
            parts = new_content.split('</style>')
            # Take the last closing style tag to be safe
            final_parts = ['</style>'.join(parts[:-1]), parts[-1]]
            new_content = final_parts[0] + "\n" + mobile_css + "\n</style>" + final_parts[1]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Purged and updated {filename}")
