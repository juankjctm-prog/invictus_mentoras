lines = open('index.html', encoding='utf-8').readlines()
with open('debug_dashboard.txt', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines):
        if 'MI PERFIL' in line or 'view-dashboard' in line or 'view-perfil' in line:
            f.write(f'{i}: {line.strip()[:200]}\n')
