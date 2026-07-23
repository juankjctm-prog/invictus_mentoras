import json
import re
import urllib.request
import urllib.error
import urllib.parse
import sys

SUPABASE_URL = "https://unbaagnuwdhavqkajory.supabase.co"
SUPABASE_KEY = "sb_publishable_8G_qiAoStdmRsEwPfvaa0g__2XlfLjV"
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def extract_json_from_js(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'=\s*(\[\s*\{.*\}\s*\])\s*;?', content, re.DOTALL)
        if not match:
            print(f"Could not find JSON array in {filepath}")
            return []
            
        json_str = match.group(1)
        data = json.loads(json_str)
        return data
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return []

def insert_to_supabase(role, data_list):
    if not data_list:
        print(f"No data to insert for {role}")
        return

    url = f"{SUPABASE_URL}/rest/v1/mentoras_content"
    
    payload = []
    for day_obj in data_list:
        dia = day_obj.get("dia")
        if not dia:
            continue
        payload.append({
            "role": role,
            "dia": dia,
            "content": day_obj
        })

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=HEADERS, method='POST')
    
    try:
        response = urllib.request.urlopen(req)
        print(f"Successfully inserted {len(payload)} records for {role}. Status: {response.status}")
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        print(f"HTTP Error for {role}: {e.code} - {error_msg}")
    except Exception as e:
        print(f"Error for {role}: {e}")

if __name__ == "__main__":
    mentadas = extract_json_from_js("mentadasData.js")
    insert_to_supabase("Mentada", mentadas)
    
    mentoras = extract_json_from_js("mujeresMentorasData.js")
    insert_to_supabase("Mentora", mentoras)
