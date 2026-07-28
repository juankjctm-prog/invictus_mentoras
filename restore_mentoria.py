import subprocess
import re

def restore_mentoria():
    # Read the original file from git (HEAD~3)
    # The file is utf-8 in git
    result = subprocess.run(['git', 'show', 'HEAD~3:diagnostico_data.js'], capture_output=True, text=True, encoding='utf-8')
    old_content = result.stdout
    
    # Extract the mentoria array
    match = re.search(r'mentoria:\s*\[\s*\{.*?\}\s*\],\s*brechas:', old_content, flags=re.DOTALL)
    if not match:
        print("Could not find mentoria array in HEAD~3")
        return
        
    mentoria_block = match.group(0).replace(',\n    brechas:', '')
    print("Found mentoria block, length:", len(mentoria_block))
    
    # Read current file
    with open('diagnostico_data.js', 'r', encoding='utf-8') as f:
        current = f.read()
        
    # See if mentoría is already there
    if 'mentoria:' in current or 'mentoría:' in current:
        print("Mentoria is already present in current file!")
    
    # Re-insert before brechas: [
    if 'brechas: [' in current:
        current = current.replace('brechas: [', mentoria_block + ',\n    brechas: [')
        with open('diagnostico_data.js', 'w', encoding='utf-8') as f:
            f.write(current)
        print("Successfully restored mentoria to diagnostico_data.js")
    else:
        print("Could not find brechas: [ in current file to insert before")

restore_mentoria()
