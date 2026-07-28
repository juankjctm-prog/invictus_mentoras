import re
import os

file_path = "D:/Documents/Negocios/ASSINT/app/Invictus/invictus-web/Mapa espiritual/Mujeres mentoras/diagnostico_mentora.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject html2pdf
if 'html2pdf' not in content:
    content = content.replace(
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>',
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
    )

# 2. HTML Containers
if 'lectura-acciones' not in content:
    content = content.replace(
        '<div class="card stat-box">',
        '<div class="card stat-box" style="flex-wrap: wrap;">',
        1 # Only the first one (lectura)
    )
    
    content = content.replace(
        '<div class="stat"><div class="stat-value" id="res-comp">--</div><div class="stat-label">Comprensión</div></div>\n                </div>',
        '<div class="stat"><div class="stat-value" id="res-comp">--</div><div class="stat-label">Comprensión</div></div>\n                    <div id="lectura-acciones" style="width: 100%; margin-top: 16px; padding: 14px; background: rgba(255,255,255,0.03); border-left: 3px solid var(--accent); border-radius: 8px; font-size: 0.85rem; color: var(--muted); display: none; text-align: left;"></div>\n                </div>'
    )

if 'mentoria-recomendaciones' not in content:
    content = content.replace(
        '<div id="res-mentoría-dims"></div>\n                </div>',
        '<div id="res-mentoría-dims"></div>\n                    <div id="mentoria-recomendaciones" style="margin-top: 16px; padding: 14px; background: rgba(255,255,255,0.03); border-left: 3px solid var(--purple); border-radius: 8px; font-size: 0.85rem; color: var(--muted); display: none; text-align: left;"></div>\n                </div>'
    )

if 'brechas-sugerencias' not in content:
    content = content.replace(
        '<div id="res-brechas"></div>\n                </div>',
        '<div id="res-brechas"></div>\n                    <div id="brechas-sugerencias" style="margin-top: 16px; padding: 14px; background: rgba(255,255,255,0.03); border-left: 3px solid var(--warning); border-radius: 8px; font-size: 0.85rem; color: var(--muted); display: none; text-align: left;"></div>\n                </div>',
        1 # Only the mentoreada brechas, not auto
    )

# 3. Inject logic in mostrarResultados
logic_inject = """
            // Lectura recomendaciones
            const lecturaAcciones = document.getElementById('lectura-acciones');
            lecturaAcciones.style.display = 'block';
            if (r.lectura.ppm < 200 || r.lectura.comprensión < 60) {
                lecturaAcciones.innerHTML = '<strong>Táctica Recomendada:</strong> Te sugerimos repasar el Bloque 1 y utilizar la técnica de Recall Activo para mejorar la retención antes de intentar subir la velocidad.';
            } else if (r.lectura.ppm >= 400 && r.lectura.comprensión >= 80) {
                lecturaAcciones.innerHTML = '<strong>¡Excelente nivel ejecutivo!</strong> Tienes una velocidad y comprensión sobresalientes. Usa el marcapasos visual para mantener este ritmo constante sin fatigarte.';
            } else {
                lecturaAcciones.innerHTML = '<strong>Táctica Recomendada:</strong> Tienes una buena base. Aplica la técnica de saltos sacádicos para expandir tu visión periférica y aumentar tu velocidad sin perder comprensión.';
            }

            // Mentoría recomendaciones
            const mentoriaRecs = document.getElementById('mentoria-recomendaciones');
            mentoriaRecs.style.display = 'block';
            const sortedMentoria = Object.entries(r.mentoría.porDimension).sort((a, b) => a[1] - b[1]);
            const weakestMentoria = sortedMentoria[0][0];
            
            if (weakestMentoria === "Escucha") {
                mentoriaRecs.innerHTML = '<strong>Área de Oportunidad (Escucha):</strong> Te sugerimos repasar el Bloque 2. Además, el libro "Indistractable" de Nir Eyal es fundamental para dominar la atención plena en tus sesiones.';
            } else if (weakestMentoria === "Feedback" || weakestMentoria === "Candor") {
                mentoriaRecs.innerHTML = '<strong>Área de Oportunidad (' + weakestMentoria + '):</strong> Te sugerimos enfocarte en el Bloque 6. Como lectura complementaria, revisa a Kim Scott (Radical Candor) y Jocko Willink (Extreme Ownership).';
            } else {
                mentoriaRecs.innerHTML = '<strong>Área de Oportunidad (' + weakestMentoria + '):</strong> Enfoca tu atención en desarrollar esta dimensión durante las próximas semanas del programa para potenciar tu impacto como mentora.';
            }
"""

if '// Lectura recomendaciones' not in content:
    content = content.replace(
        "document.getElementById('res-mentoría-dims').innerHTML = mentorHtml;",
        "document.getElementById('res-mentoría-dims').innerHTML = mentorHtml;\n" + logic_inject
    )

brechas_logic_inject = """
            // Brechas recomendaciones
            const brechasSug = document.getElementById('brechas-sugerencias');
            brechasSug.style.display = 'block';
            if (criticas.length > 0) {
                const worstBrecha = criticas[0][0];
                if (worstBrecha.includes("Visibilidad") || worstBrecha.includes("Financiera")) {
                    brechasSug.innerHTML = '<strong>Sugerencia Táctica:</strong> Para la brecha de ' + worstBrecha + ', enséñale a traducir sus logros y proyectos a términos de P&L (Pérdidas y Ganancias) para que la directiva escuche su valor.';
                } else if (worstBrecha.includes("Liderazgo")) {
                    brechasSug.innerHTML = '<strong>Sugerencia Táctica:</strong> Para la brecha de ' + worstBrecha + ', acompáñala a aplicar "Extreme Ownership" (propiedad extrema) para que deje de victimizarse por su equipo o contexto.';
                } else if (worstBrecha.includes("Energía") || worstBrecha.includes("Tiempo")) {
                    brechasSug.innerHTML = '<strong>Sugerencia Táctica:</strong> Para la brecha de ' + worstBrecha + ', guíala hacia la delegación radical. Debe soltar tareas operativas para enfocarse en la visión estratégica.';
                } else {
                    brechasSug.innerHTML = '<strong>Sugerencia Táctica:</strong> Tu mentoreada requiere intervención directa en ' + worstBrecha + '. Dedica las próximas dos sesiones exclusivamente a diseñar un plan de acción para esta área.';
                }
            } else {
                brechasSug.innerHTML = '<strong>¡Buen perfil inicial!</strong> No se detectan brechas críticas severas. Ayúdala a llevar sus áreas medias a un nivel de maestría estratégica.';
            }
"""

if '// Brechas recomendaciones' not in content:
    content = content.replace(
        "document.getElementById('res-brechas').innerHTML = brechasHtml;",
        "document.getElementById('res-brechas').innerHTML = brechasHtml;\n" + brechas_logic_inject
    )

# 4. Replace downloadReport()
new_download = """
        function downloadReport() {
            const btns = document.querySelectorAll('.step[data-step="6"] .btn');
            btns.forEach(b => b.style.display = 'none');
            
            const element = document.querySelector('.step[data-step="6"]');
            const opt = {
                margin:       [10, 10, 10, 10],
                filename:     'Diagnostico_Mentora_Invictus.pdf',
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true, backgroundColor: '#000000' },
                jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };
            
            html2pdf().set(opt).from(element).save().then(() => {
                btns.forEach(b => b.style.display = 'block');
            });
        }
"""

content = re.sub(r'function downloadReport\(\) \{.*?(?=</script>)', new_download.strip() + '\n    ', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("diagnostico_mentora.html updated successfully!")
