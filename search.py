lines = open('Invictus_Mentoras.html', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if 'window.mentadasData' in line or 'window.mujeresMentorasData' in line:
        print(f'{i+1}: {line.strip()}')
