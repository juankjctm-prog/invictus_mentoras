import re

with open('bloque1_parsed.txt', 'r', encoding='utf-8') as f:
    text = f.read()

days = re.split(r'(?i)DÍA (\d+)\s+', text)
output_lines = ["GUIONES PARA LOS AUDIOS DE LA FASE 12 (Días 1 al 10)\n", "="*55 + "\n"]

for i in range(1, len(days), 2):
    day_num = int(days[i])
    day_content = days[i+1]
    
    match = re.search(r'(?i)FASE 12.*?MODO SUEÑO.*?\n(.*?)(?:DÍA \d+|$)', day_content, re.DOTALL)
    if match:
        f12_text = match.group(1).strip()
        output_lines.append(f"--- DÍA {day_num} ---")
        output_lines.append(f12_text)
        output_lines.append("\n" + "-"*30 + "\n")

with open('guiones_audios_fase12.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(output_lines))

print("Extraction complete.")
