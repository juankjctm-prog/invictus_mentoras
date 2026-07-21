import codecs
import re
with codecs.open('index.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

nav = re.search(r'<nav class="bottom-nav">(.*?)</nav>', text, re.IGNORECASE | re.DOTALL)
if nav:
    print(nav.group(1).encode('ascii', 'ignore').decode('ascii'))
else:
    print('No bottom-nav found in index.html')
