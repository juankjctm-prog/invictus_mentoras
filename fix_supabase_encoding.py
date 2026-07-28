import json
import re
import urllib.request
import urllib.error
import subprocess
import sys

SUPABASE_URL = "https://unbaagnuwdhavqkajory.supabase.co"
SUPABASE_KEY = "sb_publishable_8G_qiAoStdmRsEwPfvaa0g__2XlfLjV"

def get_git_content(filepath):
    # Retrieve file from git before it was deleted
    out = subprocess.check_output(['git', 'show', f'c993be6^:{filepath}'])
    content = out.decode('utf-8')
    match = re.search(r'=\s*(\[\s*\{.*\}\s*\])\s*;?', content, re.DOTALL)
    if not match:
        print(f"Could not find JSON array in {filepath}")
        return []
    return json.loads(match.group(1))

def update_supabase(role, data_list):
    # Update via PATCH using role and dia
    success = 0
    for day_obj in data_list:
        dia = day_obj.get("dia")
        if not dia:
            continue
        
        # PATCH /rest/v1/mentoras_content?role=eq.{role}&dia=eq.{dia}
        url = f"{SUPABASE_URL}/rest/v1/mentoras_content?role=eq.{role}&dia=eq.{dia}"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json; charset=utf-8",
            "Prefer": "return=minimal"
        }
        
        payload = {
            "content": day_obj
        }
        
        data_bytes = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data_bytes, headers=headers, method='PATCH')
        
        try:
            response = urllib.request.urlopen(req)
            success += 1
        except Exception as e:
            print(f"Error updating {role} dia {dia}: {e}")
            
    print(f"Updated {success} records for {role}.")

if __name__ == "__main__":
    mentadas = get_git_content("mentadasData.js")
    update_supabase("Mentada", mentadas)
    
    mentoras = get_git_content("mujeresMentorasData.js")
    update_supabase("Mentora", mentoras)
