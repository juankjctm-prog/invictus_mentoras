import codecs
import re
with codecs.open(r'..\implementaciones\Mujeres mentoras\Bloque1_Premium.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

kit = re.search(r'<div id="view-kit".*?<!-- FIN VIEW KIT -->', text, re.IGNORECASE | re.DOTALL)
if kit: print('KIT HTML:\n', kit.group(0).encode('ascii', 'ignore').decode('ascii')[:1500])

libreta = re.search(r'<div id="view-libreta".*?<!-- FIN VIEW LIBRETA -->', text, re.IGNORECASE | re.DOTALL)
if libreta: print('LIBRETA HTML:\n', libreta.group(0).encode('ascii', 'ignore').decode('ascii')[:1500])
