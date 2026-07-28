import os
import re

dir_path = r"d:\Documents\Negocios\ASSINT\app\Invictus\invictus-web\Mapa espiritual\Mujeres mentoras"

files_to_patch = [f for f in os.listdir(dir_path) if f.endswith('.html') and not f.endswith('_fixed.html')]

for f in files_to_patch:
    file_path = os.path.join(dir_path, f)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # We want to replace the previous injection with a centered vertical stack
    # Previous:
    # <div style="display: flex; align-items: center; gap: 12px;">
    #     <img src="mindjump-logo.png" alt="MindJump Logo" style="height: 32px; object-fit: contain; border-radius: 6px;">
    #     <div class="header-greeting">
    #     ...
    # </div>
    # </div>
    
    pattern = re.compile(
        r'<div style="display: flex; align-items: center; gap: 12px;">\s*<img src="mindjump-logo.png" alt="MindJump Logo" style="height: 32px; object-fit: contain; border-radius: 6px;">\s*(<div class="header-greeting">.*?</div>)\s*</div>', 
        re.DOTALL | re.IGNORECASE
    )
    
    replacement = r'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 2px;">
                <img src="mindjump-logo.png" alt="MindJump Logo" style="height: 50px; object-fit: contain;">
                \1
            </div>'''
            
    if pattern.search(content):
        content = pattern.sub(replacement, content)
        modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
