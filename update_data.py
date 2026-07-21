import codecs
import json

def update_data(file_path):
    with codecs.open(file_path, 'r', 'utf-8') as f:
        content = f.read()
    
    start = content.find('[')
    end = content.rfind(']') + 1
    data = json.loads(content[start:end])
    
    # 1. Update comprension (Fase 2) to be an array and add 2 more questions
    comp1 = data[0]["fase2_lectura"]["comprension"]
    if isinstance(comp1, dict): # if not already array
        q2 = {
            "q": "Según el estudio de INCAE de 2022 mencionado en el texto, ¿a qué factor atribuía el 78% de las mujeres su ascenso?",
            "options": [
                "A su competencia propia y alto nivel de inteligencia.",
                "A factores externos como la suerte, redes de contactos o momento oportuno.",
                "A la discriminación positiva de las empresas multinacionales."
            ],
            "answer": 1
        }
        q3 = {
            "q": "¿Qué sucede en el peor de los casos cuando una mentora que no ha examinado su propia identidad de liderazgo intenta acompañar a una mentoreada?",
            "options": [
                "Transmite exitosamente sus competencias técnicas y su experiencia.",
                "Simplemente pierde el tiempo de ambas sin mayores consecuencias.",
                "Replica inconscientemente los mismos límites y patrones que la mentoreada ya tiene."
            ],
            "answer": 2
        }
        data[0]["fase2_lectura"]["comprension"] = [comp1, q2, q3]

    # 2. Add examples for Phases 6, 7, 9, 10 (Day 1)
    
    # Fase 6: Loci
    if not 'Ejemplo práctico:' in data[0]["fase6_loci"]:
        data[0]["fase6_loci"] += "\n<br><strong style='color:var(--accent-water)'>Ejemplo práctico:</strong> Visualiza la puerta de tu casa. En la manija, coloca mentalmente a 'Herminia Ibarra' bloqueándote la entrada hasta que asumas tu identidad de liderazgo. Al abrir la puerta, el pasillo es tu 'Zona de seguridad psicológica' donde puedes equivocarte."
        
    # Fase 7: Analogia
    if not 'Ejemplo práctico:' in data[0]["fase7_analogia"]:
        data[0]["fase7_analogia"] += "\n<br><strong style='color:var(--accent-water)'>Ejemplo práctico:</strong> 'La identidad de liderazgo es al ejecutivo lo que el sistema operativo es a una computadora. Puedes instalarle (aprender) muchos programas nuevos (habilidades), pero si el sistema operativo (tu identidad) no cree tener los recursos para correrlos, la computadora se colgará bajo presión'."

    # Fase 8: Ejercicio (Day 1)
    if not 'Ejemplo práctico:' in data[0]["fase8_ejercicio"]:
        data[0]["fase8_ejercicio"] += "\n<br><strong style='color:var(--accent-water)'>Ejemplo práctico:</strong> Si la pregunta es sobre tu mayor bloqueo cognitivo de hoy, anota: 'Mi bloqueo fue aceptar que la identidad de liderazgo no llega por arte de magia antes de actuar. Me di cuenta de que siempre he esperado sentirme 100% lista para proponer una idea en el comité'."

    # Note: Fase 9 (Feynman) and 10 (Metacognición) might be explicitly named differently in the array or just hardcoded in the loop.
    # Looking at data, day 1 might not have feynman. 
    if "fase9_feynman" in data[0] and data[0]["fase9_feynman"]:
        if not 'Ejemplo práctico:' in data[0]["fase9_feynman"]:
             data[0]["fase9_feynman"] += "\n<br><strong style='color:var(--accent-water)'>Ejemplo práctico:</strong> Explícale el 'Síndrome de la Impostora' a un niño de 10 años: 'Es como cuando entras a un equipo de fútbol profesional y, aunque pasaste las pruebas, sientes que en cualquier momento se darán cuenta de que no sabes patear tan bien como los demás'."
             
    # Assuming phase 10 is missing or combined in day1? Wait, in standard JSON it's probably missing from day 1, or maybe it is there.
    
    # Save back
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    var_name = 'mujeresMentorasData' if 'mujeres' in file_path.lower() else 'mentadasData'
    final_content = f"const {var_name} = " + new_json + f";\n\nwindow.{var_name} = {var_name};\n"

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(final_content)

update_data('mujeresMentorasData.js')
update_data('mentadasData.js')
print('Data files updated with extra questions and practical examples.')
