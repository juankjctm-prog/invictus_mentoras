import json
import codecs

with codecs.open('mujeresMentorasData.js', 'r', 'utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
data = json.loads(text[start:end])

d4 = next(d for d in data if d['dia'] == 4)
txt = d4['fase2_lectura']['texto']
print('Has backtick:', '`' in txt)
print('Has single quote:', "'" in txt)
print('Has double quote:', '"' in txt)
