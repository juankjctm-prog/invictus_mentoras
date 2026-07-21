import codecs
import re
with codecs.open(r'..\Mentadas\app.html', 'r', 'utf-8') as f:
    text = f.read()
nav = re.search(r'<nav class="bottom-nav">.*?</nav>', text, re.IGNORECASE | re.DOTALL)
if nav:
    print(nav.group(0).encode('ascii', 'ignore').decode('ascii'))
