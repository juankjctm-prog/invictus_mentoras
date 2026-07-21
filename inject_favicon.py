import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace or insert favicon
favicon_tag = '<link rel="icon" type="image/png" href="favicon.png">\n    <title>'
if '<link rel="icon"' in content:
    content = re.sub(r'<link rel="icon"[^>]*>', '<link rel="icon" type="image/png" href="favicon.png">', content)
else:
    content = content.replace('<title>', favicon_tag)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Favicon updated.')
