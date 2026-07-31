import codecs

with codecs.open('dashboard_diagnostico.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

content = content.replace('<span title="Al da" style="color:#10B981;">YY</span>', '<span title="Al día" style="color:#10B981;">🟢</span>')
content = content.replace('<span title="Racha Activa">Y"</span>', '<span title="Racha Activa">🔥</span>')
content = content.replace('<span title="Atrǭs" style="color:#F59E0B;">s?</span>', '<span title="Atrás" style="color:#F59E0B;">⚠️</span>')
content = content.replace('<span title="Inactivo" style="color:#EF4444;">Y"</span>', '<span title="Inactivo" style="color:#EF4444;">🔴</span>')
content = content.replace('<span title="Sin Iniciar" style="color:var(--text-secondary);">s</span>', '<span title="Sin Iniciar" style="color:var(--text-secondary);">⚫</span>')

with codecs.open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
    f.write(content)
