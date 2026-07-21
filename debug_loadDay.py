lines = open('index.html', encoding='utf-8').readlines()
with open('debug_loadDay.txt', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines):
        if 'load' in line.lower() or 'day' in line.lower() or 'dia' in line.lower():
            f.write(f'{i}: {line.strip()[:200]}\n')
