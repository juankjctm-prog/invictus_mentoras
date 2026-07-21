import codecs
import re

def rebrand_file(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        content = f.read()

    # Replacements for index.html
    if 'index.html' in filename:
        content = content.replace('<title>Invictus Master Track | Liderazgo Femenino</title>', '<title>MindJump Master Track | Liderazgo Femenino</title>')
        content = content.replace('<span class="logo-text">Invictus</span>', '<span class="logo-text">MindJump</span>')
        content = content.replace('Postula a Invictus', 'Postula a MindJump')
        content = content.replace('Invictus Mentoras', 'MindJump Mentoras')
        content = content.replace('Una inteligencia artificial de bolsillo entrenada bajo la doctrina Invictus.', 'Una inteligencia artificial de bolsillo entrenada bajo la doctrina MindJump.')
        
    # Replacements for app.html
    if 'app.html' in filename:
        content = content.replace('<title>Invictus Mind Premium</title>', '<title>MindJump Premium</title>')
        content = content.replace('<span class="logo-text">Invictus</span>', '<span class="logo-text">MindJump</span>')
        content = content.replace('Asistente IA de Invictus', 'Asistente IA de MindJump')
        # Rename Cuaderno Invictus
        content = content.replace('Cuaderno Invictus', 'Libreta MindJump')
        content = content.replace('Cuaderno Físico Invictus', 'Libreta MindJump')

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(content)

rebrand_file('index.html')
rebrand_file('app.html')
print('Rebranding complete.')
