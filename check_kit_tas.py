import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

kit = re.search(r'<div[^>]*id="view-kit".*?(?=<div[^>]*id="view-libreta")', text, re.IGNORECASE | re.DOTALL)
if kit:
    tas = re.findall(r'<textarea.*?>', kit.group(0), re.IGNORECASE)
    print('Textareas in KIT:', len(tas))
    for ta in tas: print(ta)
