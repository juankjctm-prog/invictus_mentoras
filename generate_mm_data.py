import re
import json

with open("Bloque1.md", "r", encoding="utf-8") as f:
    content = f.read()

days = re.split(r'DÍA (\d+)\s+([^\n]+)', content)[1:]
# days is a list like ['1', 'TITLE', 'content...', '2', 'TITLE2', 'content...']

json_data = []

for i in range(0, len(days), 3):
    day_num = int(days[i])
    title = days[i+1].strip()
    day_content = days[i+2]
    
    # Extract sections
    # FASE 2
    f2_match = re.search(r'📚\s*FASE 2 — LECTURA CRONOMETRADA.*?\n(.*?)\n\n📖\s*FASE 3', day_content, re.DOTALL)
    f2_text = f2_match.group(1).strip() if f2_match else ""
    
    # Clean F2 text (remove instructions like "Activa el cronómetro...")
    f2_text = re.sub(r'^Activa el cronómetro[^\n]*\n+', '', f2_text).strip()
    f2_text = re.sub(r'^Cronómetro activo[^\n]*\n+', '', f2_text).strip()
    
    # Comprension lectora extra for Fase 2
    comprension = {
        "q": "¿Cuál es la idea principal de este texto?",
        "options": ["Opción A (Incorrecta)", "Opción B (Correcta)", "Opción C (Incorrecta)"],
        "answer": 1
    }
    
    # FASE 4 (Recall)
    f4_match = re.search(r'🔍\s*FASE 4 — RECALL ACTIVO.*?\n(.*?)🧠\s*FASE 5', day_content, re.DOTALL)
    f4_text = f4_match.group(1).strip() if f4_match else ""
    
    recall_list = []
    # parse literal
    lit_m = re.search(r'\[Literal\]\n(.*?)\n_', f4_text)
    if lit_m:
        recall_list.append({"type": "Literal", "q": lit_m.group(1).strip()})
        
    inf_m = re.search(r'\[Inferencial\]\n(.*?)\n_', f4_text)
    if inf_m:
        recall_list.append({"type": "Inferencial", "q": inf_m.group(1).strip()})
        
    mul_m = re.search(r'\[Opción múltiple\]\n(.*?)\n\n', f4_text + "\n\n")
    if mul_m:
        # Extract q and options (simplified)
        q_text = mul_m.group(1).strip()
        recall_list.append({"type": "Opción múltiple", "q": q_text})
        
    con_m = re.search(r'\[Conexión personal\]\n(.*?)\n_', f4_text)
    if con_m:
        recall_list.append({"type": "Conexión personal", "q": con_m.group(1).strip()})
    
    day_obj = {
        "dia": day_num,
        "bloque": "Bloque 1: El Espejo y la Raíz",
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

print(f"Generated data for {len(json_data)} days.")
