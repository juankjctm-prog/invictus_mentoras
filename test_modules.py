import os
import re

print("Iniciando prueba de validacion de modulos Premium...")
base_path = "c:/Users/mcastro/Documents/Claude/Projects/Mapa espiritual/Mujeres mentoras/"
files = [f"Bloque{i}_Premium.html" for i in range(1, 9)]

all_passed = True
total_days = 0

for file in files:
    full_path = os.path.join(base_path, file)
    print(f"\n--- Probando {file} ---")
    
    # 1. Existence check
    if not os.path.exists(full_path):
        print(f"ERROR: El archivo {file} no existe.")
        all_passed = False
        continue
    else:
        print("OK: Archivo existe.")
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 2. Structure check (daysData)
    match = re.search(r'const daysData = \[\s*\{([\s\S]+?)\];', content)
    if not match:
        print(f"ERROR: 'daysData' array no encontrado en {file}.")
        all_passed = False
    else:
        print("OK: Estructura 'daysData' encontrada.")
        
        # 3. Count days
        days_data_str = match.group(0)
        ids = re.findall(r'id:\s*(\d+)', days_data_str)
        print(f"OK: Se encontraron {len(ids)} dias configurados: {ids}")
        total_days += len(ids)
        
    # 4. Patch check (data.recall)
    if "data.recall.forEach" in content:
        if "if (data.recall)" in content:
            print("OK: Parche de 'data.recall' aplicado correctamente (seguro contra crashes).")
        else:
            missing_recall = False
            for day_id in ids:
                day_block = re.search(r'id:\s*' + day_id + r'[\s\S]*?(?=id:\s*\d+|$)', days_data_str)
                if day_block and "recall:" not in day_block.group(0):
                    missing_recall = True
            if missing_recall:
                print("ERROR: El archivo tiene dias sin 'recall' y no tiene el parche de seguridad en el JS.")
                all_passed = False
            else:
                print("OK: Los dias incluyen 'recall' explicito, el JS es seguro.")
    else:
        print("OK: No usa forEach en recall o tiene una logica diferente valida.")

print("\n==============================================")
if all_passed:
    print(f"PRUEBA EXITOSA: Todos los modulos ({len(files)}) son validos y contienen un total de {total_days} dias.")
else:
    print("PRUEBA FALLIDA: Se encontraron errores en algunos modulos.")
