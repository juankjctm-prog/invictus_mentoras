import codecs
import re
import os

source_path = os.path.join('..', 'implementaciones', 'Mujeres mentoras', 'Bloque1_Premium.html')
with codecs.open(source_path, 'r', 'utf-8', errors='ignore') as f:
    premium_html = f.read()

# Extract view-kit
kit_match = re.search(r'(<div id="view-kit" class="view kit-view">.*?)<div id="view-library"', premium_html, re.IGNORECASE | re.DOTALL)
if kit_match:
    view_kit = kit_match.group(1).strip()
    
    with codecs.open('app.html', 'r', 'utf-8') as f:
        app_html = f.read()
        
    if 'id="view-kit"' not in app_html:
        app_html = app_html.replace('<div id="view-libreta"', view_kit + '\n\n            <div id="view-libreta"')
        
        with codecs.open('app.html', 'w', 'utf-8') as f:
            f.write(app_html)
        print("Injected view-kit HTML into app.html!")
    else:
        print("view-kit already exists in app.html")
else:
    print("Could not extract view-kit from prototype.")
