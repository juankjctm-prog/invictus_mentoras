import codecs
import re

with codecs.open(r'..\implementaciones\Mujeres mentoras\Bloque1_Premium.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

scripts = re.findall(r'<script>(.*?)</script>', text, re.IGNORECASE | re.DOTALL)

with codecs.open('prototype_scripts.txt', 'w', 'utf-8') as f:
    for i, s in enumerate(scripts):
        f.write(f'=== SCRIPT {i} ===\n')
        f.write(s)
        f.write('\n\n')
