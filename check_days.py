import re
with open('mujeresMentorasData.js', 'r', encoding='utf-8') as f:
    text = f.read()
dias = re.findall(r'"dia"\s*:\s*(\d+)', text)
print(f'Total days found: {len(dias)}')
print(f'Unique days: {sorted(list(set(map(int, dias))))}')
