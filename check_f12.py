import json
import codecs

with codecs.open('mujeresMentorasData.js', 'r', 'utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
data = json.loads(text[start:end])

for d in data[:5]:
    print(f"Day {d['dia']} - Fase 12:", d.get('fase12_sueno'))
