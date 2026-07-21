import codecs, re
with codecs.open('mujeresMentorasData.js', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'titulo:\s*"[^"]*impostor[^"]*"', text, re.IGNORECASE)
if m:
    start = m.start()
    print('Found Day 4 at', start)
    print(text[start:start+500])
else:
    print('Not found')
