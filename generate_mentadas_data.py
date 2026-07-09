import re
import json
import copy

input_file = "mujeresMentorasData.js"
output_file = "mentadasData.js"

with open(input_file, "r", encoding="utf-8") as f:
    js_content = f.read()

# Extract JSON from JS
json_str = js_content.replace("const mujeresMentorasData = ", "").replace(";\n\nwindow.mujeresMentorasData = mujeresMentorasData;", "").strip()
data = json.loads(json_str)

mentadas_data = copy.deepcopy(data)

# Mentada transformations
def replace_text(text):
    if not isinstance(text, str):
        return text
    # Simple replacements for Mentada perspective
    text = text.replace("tu mentoreada", "ti misma")
    text = text.replace("la mentoreada", "ti")
    text = text.replace("como mentora", "como líder en ascenso")
    text = text.replace("la mentora", "la líder")
    text = text.replace("guiar a otra mujer", "desarrollar tu carrera")
    text = text.replace("tu protegida", "tu propio crecimiento")
    return text

for day in mentadas_data:
    # Modify phases 4, 8, 10, 11, 12
    for r in day['fase4_recall']:
        if r['type'] == 'Conexión personal':
            if day['dia'] == 1:
                r['q'] = "¿En qué decisión reciente de tu vida profesional dudaste de tu propia capacidad? ¿Qué cambiaría si empezaras a actuar con la identidad de la líder que ya eres?"
            elif day['dia'] == 2:
                r['q'] = "¿Qué patrón de respuesta automática reconoces en ti que te frena en reuniones importantes? ¿Cómo podrías desactivarlo hoy?"
            else:
                r['q'] = replace_text(r['q'])

    if day['dia'] == 1:
        day['fase8_ejercicio'] = "Escribe en tu Cuaderno Invictus cómo te presentarás en tu próxima reunión asumiendo total agencia."
        day['fase10_metacognicion'] = "¿Qué te genera más miedo de asumir tu identidad de liderazgo?"
        day['fase11_ensayo'] = "Obsérvate a ti misma tomando una decisión compleja con absoluta certeza y presencia ejecutiva."
        day['fase12_sueno'] = {
            "afirmacion1": "Soy la protagonista de mi trayectoria profesional.",
            "afirmacion2": "Reclamo mis logros sin culpa ni justificación.",
            "afirmacion3": "Mi voz ejecutiva es firme y necesaria."
        }
    elif day['dia'] == 2:
        day['fase8_ejercicio'] = "Escribe en tu Cuaderno Invictus un límite claro que establecerás hoy para proteger tu energía mental."
        day['fase10_metacognicion'] = "¿Dónde sientes físicamente la resistencia cuando tienes que defender una idea tuya?"
        day['fase11_ensayo'] = "Obsérvate a ti misma entrando a una sala de alto nivel y sintiéndote biológicamente segura."
        day['fase12_sueno'] = {
            "afirmacion1": "Mis patrones pasados no definen mi capacidad ejecutiva futura.",
            "afirmacion2": "Transformo mi estrés en poder de acción.",
            "afirmacion3": "Estoy construyendo una nueva biología de éxito."
        }
    else:
        # Generic fallback replacements for other days
        day['fase8_ejercicio'] = replace_text(day['fase8_ejercicio'])
        day['fase10_metacognicion'] = replace_text(day['fase10_metacognicion'])
        day['fase11_ensayo'] = replace_text(day['fase11_ensayo'])
        if isinstance(day['fase12_sueno'], dict):
            for k in day['fase12_sueno']:
                day['fase12_sueno'][k] = replace_text(day['fase12_sueno'][k])

out_js = "const mentadasData = " + json.dumps(mentadas_data, indent=2, ensure_ascii=False) + ";\n\nwindow.mentadasData = mentadasData;"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(out_js)

print(f"Generated mentadasData.js with {len(mentadas_data)} days.")
