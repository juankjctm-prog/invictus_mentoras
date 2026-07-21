import codecs

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

if 'select option {' not in text:
    css = "        select option { background-color: #1a1a1c; color: #fff; }\n"
    text = text.replace('</style>', css + '</style>')
    
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print('CSS fixed')
else:
    print('Already fixed')
