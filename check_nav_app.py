import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'<nav class="bottom-nav">(.*?)</nav>', text, re.IGNORECASE | re.DOTALL)
if m:
    print(m.group(1).encode('ascii', 'ignore').decode('ascii'))
else:
    print('Not found')
