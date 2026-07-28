import re

def main():
    try:
        with open('old_diag.js', 'r', encoding='utf-16le') as f:
            old_content = f.read()
    except:
        with open('old_diag.js', 'r', encoding='utf-8') as f:
            old_content = f.read()

    match = re.search(r'mentoría:\s*\[.*?\}\s*\],\s*brechas:', old_content, flags=re.DOTALL)
    if not match:
        print("mentoría block not found!")
        return

    block = match.group(0).replace(',\n    brechas:', '')

    with open('diagnostico_data.js', 'r', encoding='utf-8') as f:
        current = f.read()

    if 'mentoría:' in current:
        print("already present!")
        return

    current = current.replace('brechas: [', block + ',\n    brechas: [')
    
    with open('diagnostico_data.js', 'w', encoding='utf-8') as f:
        f.write(current)
    print("RESTORED mentoría block!")

main()
