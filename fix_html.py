import codecs

with codecs.open('dashboard_diagnostico.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

content = content.replace("let rachaHtml = '<span title=Racha Activa>??</span>';", "let rachaHtml = '<span title=\"Racha Activa\">🔥</span>';")
content = content.replace("let semaforoHtml = '<span title=Al d?a style=color:#10B981;>??</span>';", "let semaforoHtml = '<span title=\"Al día\" style=\"color:#10B981;\">🟢</span>';")

with codecs.open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
    f.write(content)
