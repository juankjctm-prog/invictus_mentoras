import os
import re

dir_path = r"d:\Documents\Negocios\ASSINT\app\Invictus\invictus-web\Mapa espiritual\Mujeres mentoras"

files_to_patch = [f for f in os.listdir(dir_path) if f.endswith('.html') and not f.endswith('_fixed.html')]

for f in files_to_patch:
    file_path = os.path.join(dir_path, f)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    app_header_pattern = re.compile(r'(<header class="app-header"[^>]*>\s*)(<div class="header-greeting">.*?</div>)', re.DOTALL | re.IGNORECASE)
    
    def replace_header(match):
        greeting_html = match.group(2)
        return match.group(1) + f'<div style="display: flex; align-items: center; gap: 12px;">\n                <img src="mindjump-logo.png" alt="MindJump Logo" style="height: 32px; object-fit: contain; border-radius: 6px;">\n                {greeting_html}\n            </div>'

    if app_header_pattern.search(content):
        if "mindjump-logo.png" not in content:
            content = app_header_pattern.sub(replace_header, content)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
