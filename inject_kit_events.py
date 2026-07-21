import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

# Add ID and onblur to all textareas in kit that don't have an ID
def add_id_to_ta(match):
    ta = match.group(0)
    if 'id=' not in ta:
        # generate a random id
        import random
        id = f"ta_{random.randint(1000, 9999)}"
        ta = ta.replace('<textarea', f'<textarea id="{id}" onblur="guardarKit(\'{id}\')"')
    elif 'onblur' not in ta and 'onchange' not in ta:
        # extract id
        id_match = re.search(r'id=["\']([^"\']+)["\']', ta)
        if id_match:
            id = id_match.group(1)
            ta = ta.replace('<textarea', f'<textarea onblur="guardarKit(\'{id}\')"')
    return ta

kit = re.search(r'<div[^>]*id="view-kit".*?(?=<div[^>]*id="view-library")', text, re.IGNORECASE | re.DOTALL)
if kit:
    new_kit = re.sub(r'<textarea.*?>', add_id_to_ta, kit.group(0), flags=re.IGNORECASE)
    text = text.replace(kit.group(0), new_kit)
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Injected onblur and IDs into kit textareas!")
else:
    print("Kit not found.")
