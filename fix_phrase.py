import codecs

with codecs.open('app.html', 'r', 'utf-8') as f:
    text = f.read()

# Replace text
text = text.replace('Velocidad a Dinero:', 'Velocidad de comprensión:')

with codecs.open('app.html', 'w', 'utf-8') as f:
    f.write(text)

print("Text replaced successfully")
