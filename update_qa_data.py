import os
import re
import json

def parse_multiple_choice(text):
    questions = []
    # Split by numbers followed by dot
    blocks = re.split(r'\n(\d+)\.\s+', "\n" + text.strip())
    # blocks[0] is empty or intro text. blocks[1] is '1', blocks[2] is question+options
    for i in range(1, len(blocks), 2):
        block = blocks[i+1].strip()
        # Extract question (everything before a) )
        q_match = re.search(r'^(.*?)\n\s*a\)', block, re.DOTALL)
        if not q_match:
            continue
        q_text = q_match.group(1).strip().replace('\n', ' ')
        q_text = re.sub(r'\s+', ' ', q_text)
        
        options = []
        answer_idx = 0
        
        # Find all options
        opt_matches = re.finditer(r'\b([a-e])\)\s*(.*?)(?=\n\s*[a-e]\)|\Z)', block, re.DOTALL)
        for idx, match in enumerate(opt_matches):
            opt_letter = match.group(1)
            opt_text = match.group(2).strip().replace('\n', ' ')
            opt_text = re.sub(r'\s+', ' ', opt_text)
            
            if '✅' in opt_text or 'CORRECTA' in opt_text:
                answer_idx = idx
                opt_text = opt_text.replace('✅', '').replace('CORRECTA', '').strip()
            
            options.append(opt_text)
            
        questions.append({
            "q": q_text,
            "options": options,
            "answer": answer_idx
        })
    return questions

def parse_recall(text):
    questions = []
    # Find all blocks starting with [Type]
    matches = re.finditer(r'\[(.*?)\]\s*\n(.*?)(?=\n\n\[|\n\[|==========|\Z)', text, re.DOTALL)
    for match in matches:
        q_type = match.group(1).strip()
        if 'incluida en el texto' in q_type.lower():
            q_type = q_type.split('—')[0].strip()
            
        block_text = match.group(2).strip()
        
        # Separate question and RESPUESTA MODELO or NOTA PARA QUIEN FACILITA
        q_text = block_text
        modelo = ""
        
        mod_match = re.search(r'\n\s*(?:RESPUESTA MODELO|NOTA PARA QUIEN FACILITA):\s*(.*)', block_text, re.DOTALL | re.IGNORECASE)
        if mod_match:
            modelo = mod_match.group(1).strip().replace('\n', ' ')
            modelo = re.sub(r'\s+', ' ', modelo)
            q_text = block_text[:mod_match.start()].strip()
            
        q_text = q_text.replace('\n', ' ')
        q_text = re.sub(r'\s+', ' ', q_text)
        
        questions.append({
            "type": q_type,
            "q": q_text,
            "respuesta_modelo": modelo
        })
    return questions

def update_data_file(js_path, qa_dir, array_name):
    print(f"Updating {js_path} from {qa_dir}...")
    if not os.path.exists(js_path):
        print(f"File not found: {js_path}")
        return
        
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()
        
    match = re.search(fr'const {array_name} = (\[.*\]);', js_content, re.DOTALL)
    if not match:
        print(f"Could not find array {array_name} in {js_path}")
        return
        
    data_json = match.group(1)
    try:
        data = json.loads(data_json)
    except Exception as e:
        print(f"JSON parsing error in {js_path}: {e}")
        return
        
    for day_idx in range(1, 10):
        day_str = f"Dia{day_idx}"
        
        # Parse main text
        main_txt_path = os.path.join(qa_dir, "Textos", f"Texto_{day_str}.txt")
        if os.path.exists(main_txt_path):
            with open(main_txt_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            text_match = re.search(r'--- TEXTO DE LECTURA ---\n(.*?)(?=\n={10,}|\n--- FIN TEXTO|\Z)', content, re.DOTALL)
            if text_match:
                if (day_idx - 1) < len(data):
                    if 'fase2_lectura' not in data[day_idx - 1]:
                        data[day_idx - 1]['fase2_lectura'] = {}
                    
                    orig_text = data[day_idx - 1].get('fase2_lectura', {}).get('texto', '')
                    prefix = ""
                    if orig_text.startswith("(12 min)"):
                        prefix_match = re.match(r'(\(\d+ min\).*?PPM[^\n]*\n)', orig_text, re.DOTALL)
                        if prefix_match:
                            prefix = prefix_match.group(1)
                    
                    new_text = text_match.group(1).strip()
                    data[day_idx - 1]['fase2_lectura']['texto'] = prefix + new_text
            else:
                print(f"Warning: Could not extract text from {main_txt_path}")
        else:
            print(f"Warning: Text file not found: {main_txt_path}")
        
        # Parse Q&A
        # Find the question file for this day (might have dynamic name)
        qa_dir_preguntas = os.path.join(qa_dir, "Preguntas")
        qa_path = None
        if os.path.exists(qa_dir_preguntas):
            for file in os.listdir(qa_dir_preguntas):
                if file.startswith(f"{day_str}_Preguntas"):
                    qa_path = os.path.join(qa_dir_preguntas, file)
                    break
                    
        if qa_path and os.path.exists(qa_path):
            with open(qa_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            quiz_match = re.search(r'--- QUIZ INTERACTIVO.*?---\n(.*?)(?=\n--- RECALL ACTIVO|$)', content, re.DOTALL)
            if quiz_match:
                comprension = parse_multiple_choice(quiz_match.group(1))
                if (day_idx - 1) < len(data) and comprension:
                    if 'fase2_lectura' not in data[day_idx - 1]:
                        data[day_idx - 1]['fase2_lectura'] = {}
                    data[day_idx - 1]['fase2_lectura']['comprension'] = comprension
            
            recall_match = re.search(r'--- RECALL ACTIVO.*?---\n(.*)', content, re.DOTALL)
            if recall_match:
                recall = parse_recall(recall_match.group(1))
                if (day_idx - 1) < len(data) and recall:
                    data[day_idx - 1]['fase4_recall'] = recall
        else:
            print(f"Warning: Questions file not found for {day_str} in {qa_dir}")

    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = js_content[:match.start(1)] + new_json + js_content[match.end(1):]
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Successfully updated {js_path}")

base_dir = r"D:\Documents\Negocios\ASSINT\app\Invictus\invictus-web\Mapa espiritual"
mentadas_js = os.path.join(base_dir, "Mujeres mentoras", "mentadasData.js")
mentoras_js = os.path.join(base_dir, "Mujeres mentoras", "mujeresMentorasData.js")

mentadas_qa = os.path.join(base_dir, "QA_TXT_Mentadas")
mentoras_qa = os.path.join(base_dir, "QA_TXT_Mentora")

update_data_file(mentadas_js, mentadas_qa, "mentadasData")
update_data_file(mentoras_js, mentoras_qa, "mujeresMentorasData")
