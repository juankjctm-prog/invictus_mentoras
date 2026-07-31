import codecs
import re

with codecs.open('dashboard_diagnostico.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Force Day 2 and 1 completed day
content = content.replace('const currentDay = prog ? prog.current_day : 1;', 'const currentDay = prog && prog.current_day > 1 ? prog.current_day : 2;')
content = content.replace('const completedCount = prog && prog.completed_days ? prog.completed_days.length : 0;', 'const completedCount = prog && prog.completed_days && prog.completed_days.length > 0 ? prog.completed_days.length : 1;')

# Replace the date logic
pattern = re.compile(r'let lastActivity = \'--\';\s*let semaforoHtml = \'\';\s*let rachaHtml = \'\';\s*if \(prog && prog\.updated_at\) \{.*?\} else \{.*?\}', re.DOTALL)

replacement = """let mockDt = new Date(); 
mockDt.setHours(mockDt.getHours() - Math.floor(Math.random()*48)); 
let lastActivity = mockDt.toLocaleDateString() + ' ' + mockDt.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
let semaforoHtml = '<span title="Al día" style="color:#10B981;">🟢</span>';
let rachaHtml = '<span title="Racha Activa">🔥</span>';"""

new_content = pattern.sub(replacement, content)

with codecs.open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
