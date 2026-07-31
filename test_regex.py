import re
html = open('app.html', 'r', encoding='utf-8').read()

m2 = re.search(r'(<div id="view-kit" class="view">.*?<div class="kit-sec-title">📊 Mi Impacto</div>)', html, re.DOTALL)
print('m2 found:', bool(m2))

if not m2:
    print("Why not found?")
    # Let's search for view-kit
    v = html.find('id="view-kit"')
    print('view-kit index:', v)
    if v != -1:
        print('Content around view-kit:', html[v-50:v+300])
    
    s = html.find('Mi Impacto')
    print('Mi Impacto index:', s)
