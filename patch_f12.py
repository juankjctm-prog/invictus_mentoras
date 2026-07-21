import re
import json
import os

print("Processing guiones_audios_fase12.txt...")
with open("guiones_audios_fase12.txt", "r", encoding="utf-8") as f:
    content = f.read()

blocks = re.split(r'--- DÍA \d+ ---', content)
blocks = [b.strip() for b in blocks if b.strip() and "Resumen:" in b]

parsed_days = []
for i, block in enumerate(blocks[:10]):
    resumen = re.search(r'Resumen:(.*?)(?=Conceptos del día:|$)', block, re.DOTALL)
    conceptos = re.search(r'Conceptos del día:(.*?)(?=Afirmación:|$)', block, re.DOTALL)
    afirmacion = re.search(r'Afirmación:(.*?)(?=Binaural|$)', block, re.DOTALL)
    binaural = re.search(r'Binaural(.*?)$', block, re.DOTALL)
    
    parsed_days.append({
        "resumen": resumen.group(1).strip() if resumen else "",
        "conceptos": conceptos.group(1).strip() if conceptos else "",
        "afirmacion": afirmacion.group(1).strip() if afirmacion else "",
        "binaural": "Binaural" + (binaural.group(1).strip() if binaural else "")
    })

print(f"Parsed {len(parsed_days)} days.")

def patch_js(filepath):
    if not os.path.exists(filepath):
        print(f"{filepath} not found.")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        js_content = f.read()

    match = re.search(r'const (mujeresMentorasData|mentadasData) = (\[.*\]);', js_content, re.DOTALL)
    if match:
        var_name = match.group(1)
        data_json = match.group(2)
        try:
            data = json.loads(data_json)
            for i, day in enumerate(parsed_days):
                if i < len(data):
                    data[i]["fase12_sueno"] = day
            
            new_json = json.dumps(data, indent=2, ensure_ascii=False)
            new_content = js_content[:match.start(2)] + new_json + js_content[match.end(2):]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated JSON inside {filepath}")
        except Exception as e:
            print(f"Error parsing json in {filepath}: {e}")

patch_js("mujeresMentorasData.js")
patch_js("mentadasData.js")

# Now let's update inject_pin_logic.py
with open("inject_pin_logic.py", "r", encoding="utf-8") as f:
    inject_content = f.read()

# Add logic for F12 if not present
f12_logic = """
    if (phases[10]) { const desc = phases[10].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase11_ensayo; }
    
    // F12: Modo Sueño
    if (phases[11] && data.fase12_sueno && data.fase12_sueno.resumen) {
        const desc = phases[11].querySelector('.phase-desc');
        const audioTitle = phases[11].querySelector('.audio-pill span');
        if(desc) desc.innerHTML = `<strong>Resumen de la Sesión:</strong> ${data.fase12_sueno.resumen}<br><br><strong>Conceptos Integrados:</strong> ${data.fase12_sueno.conceptos}<br><br><strong>Afirmación:</strong> <em>${data.fase12_sueno.afirmacion}</em>`;
        if(audioTitle) audioTitle.innerText = data.fase12_sueno.binaural;
    }
"""

if "data.fase12_sueno.resumen" not in inject_content:
    inject_content = inject_content.replace(
        "if (phases[10]) { const desc = phases[10].querySelector('.phase-desc'); if(desc) desc.innerText = data.fase11_ensayo; }",
        f12_logic
    )
    with open("inject_pin_logic.py", "w", encoding="utf-8") as f:
        f.write(inject_content)
    print("Updated inject_pin_logic.py with F12 UI logic.")

print("Patch complete.")
