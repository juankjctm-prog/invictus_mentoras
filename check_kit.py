import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

kit = re.search(r'<div[^>]*id="view-kit".*?(?=<div[^>]*id="view-library")', text, re.IGNORECASE | re.DOTALL)
if kit:
    html = kit.group(0)[:3000].encode('ascii', 'ignore').decode('ascii')
    print(html)
