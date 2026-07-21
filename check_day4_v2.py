import codecs
with codecs.open('mujeresMentorasData.js', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = list(re.finditer(r'\"dia\":\s*4,', text))
if matches:
    start = matches[0].start()
    print(text[start:start+1000])
else:
    print('Day 4 not found.')
