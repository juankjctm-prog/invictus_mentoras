import codecs
import re
with codecs.open(r'..\implementaciones\Mujeres mentoras\Bloque1_Premium.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()
m = re.search(r'<nav class="bottom-nav">.*?</nav>', text, re.IGNORECASE | re.DOTALL)
if m:
    with codecs.open('temp_nav.txt', 'w', 'utf-8') as fw:
        fw.write(m.group(0))
    print('Found nav')
else:
    print('Not found')
