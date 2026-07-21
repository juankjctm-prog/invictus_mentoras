import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

nav = re.search(r'<nav class="bottom-nav">(.*?)</nav>', text, re.IGNORECASE | re.DOTALL)
if nav:
    print(nav.group(1).encode('ascii', 'backslashreplace').decode('ascii'))
else:
    print('Not found')
