import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'<div[^>]*id="view-libreta".*?(?=<div[^>]*id="view-kit")', text, re.IGNORECASE | re.DOTALL)
if m:
    libreta = m.group(0)
    for line in libreta.split('\n'):
        if 'select' in line.lower() or 'dropdown' in line.lower() or 'dia' in line.lower() or 'día' in line.lower() or 'day' in line.lower():
            print(line.strip().encode('ascii', 'ignore').decode('ascii'))
