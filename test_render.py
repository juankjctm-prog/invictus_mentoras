import json
import codecs

with codecs.open('mujeresMentorasData.js', 'r', 'utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
data = json.loads(text[start:end])

d3 = next(d for d in data if d['dia'] == 3)

html = []
html.append('<h4 style="color: white;">' + d3['titulo'] + '</h4>')
for p in d3['fase2_lectura']['texto'].split('\n'):
    if p.strip():
        html.append('<p class="reader-p">' + p + '</p>')

final_html = ''.join(html)
print('SUCCESS, length:', len(final_html))
if '<p class="reader-p">' not in final_html:
    print('NO P TAGS!')
