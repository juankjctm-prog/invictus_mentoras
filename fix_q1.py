import json
import codecs

for js_file in ['mujeresMentorasData.js', 'mentadasData.js']:
    with codecs.open(js_file, 'r', 'utf-8') as f:
        content = f.read()

    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])

    for day in data:
        comp = day.get('fase2_lectura', {}).get('comprension')
        if isinstance(comp, list) and len(comp) > 0:
            if "Opción A (Incorrecta)" in comp[0].get('options', []) or "Opcin A (Incorrecta)" in comp[0].get('options', []):
                
                # Replace with a better contextual question
                comp[0] = {
                    "q": "¿Cuál es la idea principal o el hallazgo central presentado en esta lectura?",
                    "options": [
                        "Los patrones y sesgos estructurales son imposibles de modificar.",
                        "Nuestras creencias, entorno y acciones pueden transformar nuestra estructura neurobiológica y resultados corporativos.",
                        "El liderazgo efectivo depende únicamente de la competencia técnica."
                    ],
                    "answer": 1
                }

    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    var_name = 'mujeresMentorasData' if 'mujeres' in js_file.lower() else 'mentadasData'
    final_content = f"const {var_name} = " + new_json + f";\n\nwindow.{var_name} = {var_name};\n"

    with codecs.open(js_file, 'w', 'utf-8') as f:
        f.write(final_content)

print("Placeholder Question 1 replaced successfully.")
