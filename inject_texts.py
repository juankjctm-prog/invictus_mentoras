import json
import codecs
import re

# 1. Read parsed docx
with open('bloque1_parsed.txt', 'r', encoding='utf-8') as f:
    text = f.read()

days = re.split(r'(?i)DÍA (\d+)\s+', text)
day_texts = {}

for i in range(1, len(days), 2):
    day_num = int(days[i])
    day_content = days[i+1]
    
    f2_match = re.search(r'FASE 2.*?LECTURA CRONOMETRADA.*?\n?(.*?)(?:FASE 3|FASE 4|📖)', day_content, re.DOTALL | re.IGNORECASE)
    
    if f2_match:
        f2_text = f2_match.group(1).strip()
        f2_text = re.sub(r'^[^\n]*Cronómetro activo[^\n]*\n+', '', f2_text, flags=re.IGNORECASE).strip()
        f2_text = re.sub(r'^[^\n]*PPM = [^\n]*\n+', '', f2_text, flags=re.IGNORECASE).strip()
        if len(f2_text) > 100:
            # We want to replace newlines with proper HTML paragraphs, or just \n
            # The parsed text has \n. We'll leave them as \n.
            day_texts[day_num] = f2_text

print(f"Found texts for days: {list(day_texts.keys())}")

# 2. Inject into JS files
for js_file in ['mujeresMentorasData.js', 'mentadasData.js']:
    with codecs.open(js_file, 'r', 'utf-8') as f:
        content = f.read()
    
    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])
    
    # 2.1 Update missing texts
    for day_obj in data:
        d = day_obj['dia']
        if d in day_texts:
            day_obj['fase2_lectura']['texto'] = day_texts[d]
            
    # 2.2 Remove Tecna references
    def remove_tecna(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str):
                    v = re.sub(r'\bTecna\b', 'la organización', v, flags=re.IGNORECASE)
                    v = re.sub(r'\ben Tecna\b', 'en la corporación', v, flags=re.IGNORECASE)
                    obj[k] = v
                else:
                    remove_tecna(v)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str):
                    item = re.sub(r'\bTecna\b', 'la organización', item, flags=re.IGNORECASE)
                    item = re.sub(r'\ben Tecna\b', 'en la corporación', item, flags=re.IGNORECASE)
                    obj[i] = item
                else:
                    remove_tecna(item)

    remove_tecna(data)
    
    # Write back
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    var_name = 'mujeresMentorasData' if 'mujeres' in js_file.lower() else 'mentadasData'
    final_content = f"const {var_name} = " + new_json + f";\n\nwindow.{var_name} = {var_name};\n"
    
    with codecs.open(js_file, 'w', 'utf-8') as f:
        f.write(final_content)

print("Texts injected and Tecna removed.")
