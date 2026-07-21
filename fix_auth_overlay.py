import re

html_file = 'app.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Change auth-overlay to fixed and higher z-index to cover fixed navs
old_auth = '.auth-overlay { position: absolute; inset: 0; z-index: 1000;'
new_auth = '.auth-overlay { position: fixed; inset: 0; z-index: 9999;'
content = content.replace(old_auth, new_auth)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed auth-overlay visibility.")
