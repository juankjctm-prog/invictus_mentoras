import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

# Add a version tag
if 'v1.5' not in text:
    text = text.replace('<body>', '<body>\n<div id="version-tag" style="position:fixed; top:10px; left:10px; color:#FF5E00; z-index:9999; font-weight:bold; font-family:sans-serif;">v1.5 KIT FIX</div>')
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print('Version tag added')
else:
    print('Already has version tag')
