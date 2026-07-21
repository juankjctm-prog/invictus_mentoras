lines = open('index.html', encoding='utf-8').readlines()
with open('debug_gamification.txt', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines):
        if 'function marcarHecho' in line or 'currentPhaseProgress' in line:
            f.write(f'{i}: {line.strip()[:200]}\n')
