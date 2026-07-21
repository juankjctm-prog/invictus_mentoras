import codecs
import json

file_path = 'mujeresMentorasData.js'

with codecs.open(file_path, 'r', 'utf-8', errors='ignore') as f:
    content = f.read()

# Extract JSON
start_idx = content.find('[')
end_idx = content.rfind(']') + 1

json_str = content[start_idx:end_idx]

# Parse
data = json.loads(json_str)
day1 = data[0]

texto_lectura = """El verdadero liderazgo no empieza cuando diriges a otros, sino cuando logras gobernarte a ti misma frente al caos. Durante años, la narrativa tradicional ha condicionado a las mujeres a liderar desde la complacencia, buscando consenso antes que impacto, y pidiendo permiso antes de tomar espacio. Esto crea el 'Síndrome de la Impostora', no porque seas incapaz, sino porque estás operando con un software caduco.

Para quebrar el techo de cristal, primero debes destruir las barreras de titanio en tu propia mente. La asertividad no es agresión; es claridad. La ambición no es egoísmo; es visión. Cuando una mujer asume su poder sin pedir disculpas, reconfigura automáticamente las dinámicas de la sala. Este programa no está diseñado para enseñarte a encajar en el molde corporativo, sino para darte las herramientas tácticas que te permitirán forjar el tuyo propio.

Tu primera misión es auditar tus disculpas. A partir de hoy, elimina el 'perdón por la interrupción' o 'solo quería decir'. Reemplázalo por silencios tácticos y declaraciones firmes. Tu voz tiene peso. Empieza a usarla como tal."""

day1["fase2_lectura"]["texto"] = texto_lectura

day1["fase2_lectura"]["comprension"] = {
    "q": "¿Cuál es el objetivo principal de reprogramar tu identidad de liderazgo en este primer bloque?",
    "options": [
        "Aprender a delegar tareas operativas a mi equipo.",
        "Destruir la falsa narrativa de insuficiencia y asumir el control de mis decisiones.",
        "Memorizar técnicas de lectura rápida para leer más libros."
    ],
    "answer": 1
}

day1["fase4_recall"] = [
    {
        "type": "Literal",
        "q": "¿Cuáles son las dos principales narrativas limitantes que menciona el texto sobre el liderazgo femenino?"
    },
    {
        "type": "Inferencial",
        "q": "Según lo leído, ¿por qué crees que el sistema tradicional penaliza la asertividad en las mujeres?"
    },
    {
        "type": "Conexión personal",
        "q": "Relata un momento reciente donde sentiste el Síndrome del Impostor. ¿Cómo lo replantearías hoy?"
    }
]

# Save back
new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_content = "const mujeresMentorasData = " + new_json_str + ";\n\nwindow.mujeresMentorasData = mujeresMentorasData;\n"

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(final_content)

print("Data fixed properly via JSON parsing!")
