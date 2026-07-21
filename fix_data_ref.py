import json
import codecs
import re

for js_file in ['mujeresMentorasData.js', 'mentadasData.js']:
    with codecs.open(js_file, 'r', 'utf-8') as f:
        content = f.read()

    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])

    for day in data:
        # 1. Strip 'Conteo exacto'
        texto = day.get('fase2_lectura', {}).get('texto', '')
        texto = re.sub(r'Conteo exacto.*', '', texto, flags=re.IGNORECASE | re.DOTALL).strip()
        day['fase2_lectura']['texto'] = texto

        # 2. Add extra questions if not already an array
        comp = day.get('fase2_lectura', {}).get('comprension', None)
        if isinstance(comp, dict):
            new_comp = [comp]
            
            # Add Q2
            new_comp.append({
                "q": "¿Cómo se traduce este concepto en tu práctica de liderazgo activo?",
                "options": [
                    "Manteniendo la neutralidad pasiva.",
                    "Implementándolo proactivamente en conversaciones difíciles.",
                    "Esperando que el equipo lo deduzca por sí mismo."
                ],
                "answer": 1
            })
            
            # Add Q3
            new_comp.append({
                "q": "El objetivo principal de interiorizar esta información es:",
                "options": [
                    "Acumular teoría académica.",
                    "Minimizar la responsabilidad de la mentoreada.",
                    "Desarrollar agencia y combatir la inseguridad estructural."
                ],
                "answer": 2
            })
            
            day['fase2_lectura']['comprension'] = new_comp

    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    var_name = 'mujeresMentorasData' if 'mujeres' in js_file.lower() else 'mentadasData'
    final_content = f"const {var_name} = " + new_json + f";\n\nwindow.{var_name} = {var_name};\n"

    with codecs.open(js_file, 'w', 'utf-8') as f:
        f.write(final_content)

print("Removed 'Conteo exacto' and added extra comprehension questions to all days.")
