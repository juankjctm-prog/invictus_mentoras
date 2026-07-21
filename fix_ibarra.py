import codecs

with codecs.open('app.html', 'r', 'utf-8') as f:
    text = f.read()

# Replace hardcoded Ibarra references
text = text.replace('Resume la teoría de Ibarra en 1 frase para tu mentoreada...', 'Resume la idea principal en 1 frase para tu mentoreada...')

with codecs.open('app.html', 'w', 'utf-8') as f:
    f.write(text)

print("Fixed Ibarra reference")
