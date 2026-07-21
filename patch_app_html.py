import codecs
import re
import os

source_path = os.path.join('..', 'implementaciones', 'Mujeres mentoras', 'Bloque1_Premium.html')
with codecs.open(source_path, 'r', 'utf-8', errors='ignore') as f:
    premium_html = f.read()

# Extract view-kit
kit_match = re.search(r'(<div[^>]*id="view-kit"[^>]*>.*?)<!-- FIN VIEW KIT -->', premium_html, re.IGNORECASE | re.DOTALL)
if not kit_match:
    kit_match = re.search(r'(<div[^>]*id="view-kit"[^>]*>.*?)(?:<div[^>]*id="view-libreta"|<nav)', premium_html, re.IGNORECASE | re.DOTALL)
view_kit = kit_match.group(1) if kit_match else ""

# Extract view-libreta
libreta_match = re.search(r'(<div[^>]*id="view-libreta"[^>]*>.*?)<!-- FIN VIEW LIBRETA -->', premium_html, re.IGNORECASE | re.DOTALL)
if not libreta_match:
    libreta_match = re.search(r'(<div[^>]*id="view-libreta"[^>]*>.*?)(?:<nav class="bottom-nav"|</body>)', premium_html, re.IGNORECASE | re.DOTALL)
new_libreta = libreta_match.group(1) if libreta_match else ""

# Extract new CSS classes
css_match = re.search(r'<style>(.*?)</style>', premium_html, re.IGNORECASE | re.DOTALL)
css_premium = css_match.group(1) if css_match else ""
kit_styles = []
for block in re.split(r'}', css_premium):
    if ('.kit-' in block or '.crisis-' in block or '.mirror-' in block or '.input-premium' in block) and 'webkit' not in block:
        kit_styles.append(block.strip() + " }")
kit_css = "\n".join(kit_styles)


# Read target (app.html)
with codecs.open('app.html', 'r', 'utf-8') as f:
    app_html = f.read()

# Replace libreta
if new_libreta:
    app_html = re.sub(r'<div id="view-libreta".*?(?:<div id="view-mentada"|<div id="view-conexion"|<nav class="bottom-nav")', new_libreta + '\n            <div id="view-mentada"', app_html, flags=re.IGNORECASE | re.DOTALL)

# Insert kit before libreta
if view_kit and 'id="view-kit"' not in app_html:
    app_html = app_html.replace('<div id="view-libreta"', view_kit + '\n\n            <div id="view-libreta"')

# Add kit to nav
nav_button = '            <div class="nav-item" onclick="switchTab(\'view-kit\', this)"><div class="nav-icon"></div><span class="nav-label">MI KIT</span></div>\n'
if 'view-kit' not in app_html.split('<nav class="bottom-nav">')[1]:
    app_html = app_html.replace('<nav class="bottom-nav">', '<nav class="bottom-nav">\n' + nav_button)

# Add kit css
if kit_css and '.kit-view' not in app_html:
    app_html = app_html.replace('</style>', kit_css + '\n    </style>')

with codecs.open('app.html', 'w', 'utf-8') as f:
    f.write(app_html)

print("app.html (Mentoras) patched with kit and playbook UI!")
