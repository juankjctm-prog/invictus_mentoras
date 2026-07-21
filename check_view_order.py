import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

for match in re.finditer(r'<div[^>]*id="([^"]+)"[^>]*class="[^"]*view', text):
    print(match.group(1))
