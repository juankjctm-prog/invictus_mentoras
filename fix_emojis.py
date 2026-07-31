import codecs
import re

with codecs.open('dashboard_diagnostico.html', 'r', encoding='latin-1', errors='ignore') as f:
    content = f.read()

# Replace the mangled blocks with valid unicode emojis
content = re.sub(r"semaforoHtml = '<span title=\"Al d.*?style=\"color:#10B981;\">.*?</span>';", "semaforoHtml = '<span title=\"Al día\" style=\"color:#10B981;\">🟢</span>';", content)
content = re.sub(r"rachaHtml = '<span title=\"Racha Activa\">.*?</span>';", "rachaHtml = '<span title=\"Racha Activa\">🔥</span>';", content)
content = re.sub(r"semaforoHtml = '<span title=\"Atr.*?style=\"color:#F59E0B;\">.*?</span>';", "semaforoHtml = '<span title=\"Atrás\" style=\"color:#F59E0B;\">⚠️</span>';", content)
content = re.sub(r"semaforoHtml = '<span title=\"Inactivo\" style=\"color:#EF4444;\">.*?</span>';", "semaforoHtml = '<span title=\"Inactivo\" style=\"color:#EF4444;\">🔴</span>';", content)
content = re.sub(r"semaforoHtml = '<span title=\"Sin Iniciar\" style=\"color:var\(--text-secondary\);\"><.*?>.*?</span>';", "semaforoHtml = '<span title=\"Sin Iniciar\" style=\"color:var(--text-secondary);\">⚫</span>';", content)

with codecs.open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
    f.write(content)
