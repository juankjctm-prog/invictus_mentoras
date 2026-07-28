import urllib.request
import json

SUPABASE_URL = "https://unbaagnuwdhavqkajory.supabase.co"
SUPABASE_KEY = "sb_publishable_8G_qiAoStdmRsEwPfvaa0g__2XlfLjV"

correct_users = {
    'usr_02': {'name': 'Eliana', 'full_name': 'Eliana Villagómez'},
    'usr_07': {'name': 'Stephany', 'full_name': 'Stephany Simbaña'},
    'usr_08': {'name': 'Anahí', 'full_name': 'Anahí Freire'},
    'usr_09': {'name': 'Noemí', 'full_name': 'Noemí Palacios'},
    'usr_10': {'name': 'Lorena', 'full_name': 'Lorena Chávez'},
    'usr_11': {'name': 'Lourdes', 'full_name': 'Lourdes Sánchez'}
}

for usr_id, data in correct_users.items():
    url = f"{SUPABASE_URL}/rest/v1/mentoras_users?id=eq.{usr_id}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json; charset=utf-8",
        "Prefer": "return=minimal"
    }
    
    payload = {
        "name": data['name'],
        "full_name": data['full_name']
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PATCH')
    try:
        response = urllib.request.urlopen(req)
        print(f"Updated {usr_id} to {data['full_name']}")
    except Exception as e:
        print(f"Error updating {usr_id}: {e}")
