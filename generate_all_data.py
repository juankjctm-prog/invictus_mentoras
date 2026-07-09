import re
import json
import os

json_data = []

bloque_names = {
    1: "Bloque 1: El Espejo y la Raíz",
    2: "Bloque 2: Comunicación y Liderazgo",
    3: "Bloque 3: Inteligencia Emocional",
    4: "Bloque 4: Pensamiento Estratégico",
    5: "Bloque 5: Poder Personal",
    6: "Bloque 6: Innovación y Adaptabilidad",
    7: "Bloque 7: Sostenibilidad y Legado",
    8: "Bloque 8: Cierre y Expansión"
}

for i in range(1, 9):
    file = f"Bloque{i}.md"
    if not os.path.exists(file): continue
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    days = re.split(r'DÍA (\d+)\s+([^\n]+)', content)[1:]
    
    for j in range(0, len(days), 3):
        day_num = int(days[j])
        title = days[j+1].strip()
        day_content = days[j+2]
        
        # FASE 2
        f2_match = re.search(r'FASE 2 — LECTURA CRONOMETRADA.*?\n(.*?)\n\n.*?FASE 3', day_content, re.DOTALL | re.IGNORECASE)
        f2_text = f2_match.group(1).strip() if f2_match else "Contenido de lectura pendiente..."
        
        # Clean F2 text
        f2_text = re.sub(r'^Activa el cronómetro[^\n]*\n+', '', f2_text, flags=re.IGNORECASE).strip()
        f2_text = re.sub(r'^Cronómetro activo[^\n]*\n+', '', f2_text, flags=re.IGNORECASE).strip()
        
        comprension = {
            "q": "¿Cuál es la idea principal de este texto?",
            "options": ["Opción A (Incorrecta)", "Opción B (Correcta)", "Opción C (Incorrecta)"],
            "answer": 1
        }
        
        # FASE 4 (Recall)
        f4_match = re.search(r'FASE 4 — RECALL ACTIVO.*?\n(.*?)FASE 5', day_content, re.DOTALL | re.IGNORECASE)
        f4_text = f4_match.group(1).strip() if f4_match else ""
        
        recall_list = []
        lit_m = re.search(r'\[Literal\]\n(.*?)\n_', f4_text)
        if lit_m:
            recall_list.append({"type": "Literal", "q": lit_m.group(1).strip()})
        else:
            recall_list.append({"type": "Literal", "q": "¿Pregunta literal pendiente?"})
            
        inf_m = re.search(r'\[Inferencial\]\n(.*?)\n_', f4_text)
        if inf_m:
            recall_list.append({"type": "Inferencial", "q": inf_m.group(1).strip()})
        else:
            recall_list.append({"type": "Inferencial", "q": "¿Pregunta inferencial pendiente?"})
            
        mul_m = re.search(r'\[Opción múltiple\]\n(.*?)\n\n', f4_text + "\n\n")
        if mul_m:
            recall_list.append({"type": "Opción múltiple", "q": mul_m.group(1).strip()})
        else:
            recall_list.append({"type": "Opción múltiple", "q": "¿Pregunta de opción múltiple pendiente?"})
            
        con_m = re.search(r'\[Conexión personal\]\n(.*?)(?:\n_|$)', f4_text)
        if con_m:
            recall_list.append({"type": "Conexión personal", "q": con_m.group(1).strip()})
        else:
            recall_list.append({"type": "Conexión personal", "q": "¿Pregunta de conexión personal pendiente?"})
        
        day_obj = {
            "dia": day_num,
            "bloque": bloque_names.get(i, f"Bloque {i}"),
            "titulo": title,
            "fase1_ancla": "Inhala profundo y prepárate mentalmente para la sesión.",
            "fase2_lectura": {
                "texto": f2_text,
                "comprension": comprension
            },
            "fase3_vocabulario": [
                {"palabra": "Concepto Clave", "definicion": "Definición deducida del texto."}
            ],
            "fase4_recall": recall_list,
            "fase5_codificacion_dual": "Visualiza el concepto principal del día de hoy como una imagen clara en tu mente.",
            "fase6_loci": "Ubica esa imagen en un lugar específico de la sala donde te encuentras.",
            "fase7_analogia": "Este concepto es como construir los cimientos de un edificio antes de levantar las paredes.",
            "fase8_ejercicio": "En tu Cuaderno Físico Invictus, escribe cómo aplicarás esto hoy.",
            "fase9_feynman": day_num % 7 == 0,
            "fase10_metacognicion": "¿Qué parte de la lectura de hoy te generó más resistencia?",
            "fase11_ensayo": "Obsérvate a ti misma liderando con seguridad utilizando el conocimiento adquirido hoy.",
            "fase12_sueno": {
                "afirmacion1": "Soy una líder en constante evolución.",
                "afirmacion2": "Mi identidad se fortalece con cada acción que tomo.",
                "afirmacion3": "Uso mi conocimiento para empoderar a otras mujeres."
            }
        }
        
        json_data.append(day_obj)

js_content = "const mujeresMentorasData = " + json.dumps(json_data, indent=2, ensure_ascii=False) + ";\n\nwindow.mujeresMentorasData = mujeresMentorasData;"

with open("mujeresMentorasData.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated mujeresMentorasData.js for {len(json_data)} days.")
