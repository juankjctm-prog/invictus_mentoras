import codecs

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

if 'color-scheme: dark;' not in text:
    css = "        input, textarea, select { color-scheme: dark; }\n"
    text = text.replace('</style>', css + '</style>')
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print('Color-scheme dark added')
else:
    print('Already has color-scheme')
