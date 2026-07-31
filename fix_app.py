import codecs

with codecs.open('app.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

content = content.replace("const ppmKey = 'mm_b' + blockNum + '_d' + currentDay + '_ppm';", "const ppmKey = 'mm_b' + blockNum + '_d' + dayId + '_ppm';")
content = content.replace("localStorage.setItem('mm_b' + blockNum + '_d' + currentDay + '_score', score.toString());", "localStorage.setItem('mm_b' + blockNum + '_d' + dayId + '_score', score.toString());")
content = content.replace("localStorage.setItem('mm_b' + blockNum + '_d' + currentDay, '1');", "localStorage.setItem('mm_b' + blockNum + '_d' + dayId, '1');")
content = content.replace("const box = document.getElementById('quiz-result-' + currentDay);", "const box = document.getElementById('quiz-result-' + dayId);")

with codecs.open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)
