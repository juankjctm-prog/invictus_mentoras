import re
with open('app.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Phase 9
html = re.sub(
    r'<!-- F9 -->\s*<div class="phase" style="display: \$\{showFeynman \? \'block\' : \'none\'\}">',
    '''<!-- F9 -->
        <div class="phase active">''',
    html
)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(html)
