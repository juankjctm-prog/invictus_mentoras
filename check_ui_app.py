import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

kit = re.search(r'<div[^>]*id="view-kit".*?(?=<div[^>]*id="view-libreta")', text, re.IGNORECASE | re.DOTALL)
if kit: print('KIT HTML:\n', kit.group(0).encode('ascii', 'ignore').decode('ascii')[:1000])

libreta = re.search(r'<div[^>]*id="view-libreta".*?(?=<div[^>]*id="view-mentada")', text, re.IGNORECASE | re.DOTALL)
if libreta: print('LIBRETA HTML:\n', libreta.group(0).encode('ascii', 'ignore').decode('ascii')[:1000])
