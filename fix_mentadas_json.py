import codecs
import json

file_path = 'mentadasData.js'

with codecs.open(file_path, 'r', 'utf-8', errors='ignore') as f:
    content = f.read()

# Extract JSON
start_idx = content.find('[')
end_idx = content.rfind(']') + 1

json_str = content[start_idx:end_idx]

data = json.loads(json_str)
day1 = data[0]

texto_lectura = """En el mundo actual, el éxito no solo depende de tu capacidad intelectual, sino de tu resiliencia emocional. Como mentoreada, estás dando el primer paso hacia una transformación que exige valentía: la disposición a desaprender lo que creías saber sobre tus propios límites.

A menudo, la sociedad nos enseña a ser perfectas antes de ser valientes. Esperamos estar 100% listas antes de levantar la mano, postular a un ascenso o iniciar un proyecto. Pero la verdadera innovación personal ocurre en la zona de incomodidad. El Síndrome del Impostor no es una señal de que no perteneces; es simplemente la prueba de que estás creciendo fuera de tu zona de confort.

Tu tarea en esta primera etapa es observar tus patrones de autocrítica. Cuando tu mente te diga "no estoy lista", traduce ese pensamiento a "estoy aprendiendo cómo hacerlo". El liderazgo personal comienza cuando dejas de pedirle permiso al miedo."""

day1["fase2_lectura"]["texto"] = texto_lectura

day1["fase2_lectura"]["comprension"] = {
    "q": "¿Qué significa realmente sentir el Síndrome del Impostor según el texto?",
    "options": [
        "Que eres incapaz de realizar la tarea asignada.",
        "Que estás experimentando crecimiento y saliendo de tu zona de confort.",
        "Que debes esperar a estar 100% lista antes de actuar."
    ],
    "answer": 1
}

day1["fase4_recall"] = [
    {
        "type": "Literal",
        "q": "¿Qué nos enseña habitualmente la sociedad sobre actuar frente a oportunidades?"
    },
    {
        "type": "Inferencial",
        "q": "¿Por qué crees que cambiar el enfoque de 'perfección' a 'valentía' acelera el crecimiento profesional?"
    },
    {
        "type": "Conexión personal",
        "q": "Identifica una oportunidad reciente en la que no participaste por esperar estar '100% lista'. ¿Qué harías diferente hoy?"
    }
]

# Save back
new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_content = "const mentadasData = " + new_json_str + ";\n\nwindow.mentadasData = mentadasData;\n"

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(final_content)

print("Mentadas Data fixed!")
