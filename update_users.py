import re
import json

html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update dots from 4 to 6
old_dots = '<div class="pin-dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>'
new_dots = '<div class="pin-dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>'
content = content.replace(old_dots, new_dots)

# 2. Update pinCount limit from 4 to 6
content = content.replace('if(pinCount < 4) {', 'if(pinCount < 6) {')
content = content.replace('if(pinCount === 4) {', 'if(pinCount === 6) {')

# 3. Replace authUsers array
users_str = """const authUsers = [
    { id: 'usr_01', pin: '012601', name: 'Mabel', fullName: 'Mabel Ibarra', role: 'Mentora' },
    { id: 'usr_02', pin: '012602', name: 'Eliana', fullName: 'Eliana Villagómez', role: 'Mentora' },
    { id: 'usr_03', pin: '012603', name: 'Mayra', fullName: 'Mayra Pujos', role: 'Mentora' },
    { id: 'usr_04', pin: '012604', name: 'Marjorie', fullName: 'Marjorie Castro', role: 'Mentora' },
    { id: 'usr_05', pin: '012605', name: 'Carla', fullName: 'Carla Godoy', role: 'Mentora' },
    { id: 'usr_06', pin: '012606', name: 'Giovanna', fullName: 'Giovanna Coimbra', role: 'Mentora' },
    { id: 'usr_07', pin: '022601', name: 'Stephany', fullName: 'Stephany Simbaña', role: 'Mentada' },
    { id: 'usr_08', pin: '022602', name: 'Anahí', fullName: 'Anahí Freire', role: 'Mentada' },
    { id: 'usr_09', pin: '022603', name: 'Noemí', fullName: 'Noemí Palacios', role: 'Mentada' },
    { id: 'usr_10', pin: '022604', name: 'Lorena', fullName: 'Lorena Chávez', role: 'Mentada' },
    { id: 'usr_11', pin: '022605', name: 'Lourdes', fullName: 'Lourdes Sánchez', role: 'Mentada' },
    { id: 'usr_12', pin: '022606', name: 'Valentina', fullName: 'Valentina Pardo', role: 'Mentada' }
];"""

content = re.sub(r'const authUsers = \[.*?\];', users_str, content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated users and PIN logic to 6 digits.")
