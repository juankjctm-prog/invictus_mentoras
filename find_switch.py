lines = open('Invictus_Mentoras.html', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if 'switchTab' in line:
        print(f'{i+1}: {line.strip().encode("ascii", "ignore").decode()}')
