import codecs

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    if "localStorage.setItem('user_pin'" in line or 'localStorage.setItem("user_pin"' in line:
        start = max(0, i-10)
        end = min(len(lines), i+15)
        print(f'=== MATCH at {i} ===')
        for j in range(start, end):
            print(f'{j}: {lines[j]}')
