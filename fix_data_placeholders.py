import codecs

file_path = 'mujeresMentorasData.js'

with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Replace Fase 2 Comprension
old_comp = """"comprension": {
        "q": "¿Cuál es la idea principal de este texto?",
        "options": [
          "Opción A (Incorrecta)",
          "Opción B (Correcta)",
          "Opción C (Incorrecta)"
        ],
        "answer": 1
      }"""

new_comp = """"comprension": {
        "q": "¿Cuál es el objetivo principal de reprogramar tu identidad de liderazgo en este primer bloque?",
        "options": [
          "Aprender a delegar tareas operativas a mi equipo.",
          "Destruir la falsa narrativa de insuficiencia y asumir el control de mis decisiones.",
          "Memorizar técnicas de lectura rápida para leer más libros."
        ],
        "answer": 1
      }"""

content = content.replace(old_comp, new_comp)

# Replace Fase 4 Recall placeholders
old_lit = '{"type": "Literal", "q": "¿Pregunta literal pendiente?"}'
new_lit = '{"type": "Literal", "q": "¿Cuáles son las dos principales narrativas limitantes que menciona el texto sobre el liderazgo femenino?"}'

old_inf = '{"type": "Inferencial", "q": "¿Pregunta inferencial pendiente?"}'
new_inf = '{"type": "Inferencial", "q": "Según lo leído, ¿por qué crees que el sistema tradicional penaliza la asertividad en las mujeres?"}'

old_con = '{"type": "Conexión personal", "q": "¿Pregunta de conexión personal pendiente?"}'
new_con = '{"type": "Conexión personal", "q": "Relata un momento reciente donde sentiste el Síndrome del Impostor. ¿Cómo lo replantearías hoy?"}'

old_mul = '{"type": "Opción múltiple", "q": "¿Pregunta de opción múltiple pendiente?"}'
new_mul = '{"type": "Opción múltiple", "q": "Elige la definición correcta de Inteligencia Intuitiva."}'

content = content.replace(old_lit, new_lit)
content = content.replace(old_inf, new_inf)
content = content.replace(old_con, new_con)
content = content.replace(old_mul, new_mul)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Data fixed with string replace!")
