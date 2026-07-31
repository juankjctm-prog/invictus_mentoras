import re

with open('dashboard_diagnostico.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_content_pattern = re.compile(r'(<div class="container">.*?)(<script src="https://cdn.jsdelivr.net)', re.DOTALL)
m2 = body_content_pattern.search(content)

if m2:
    body_html = m2.group(1)
    
    # Split into the two existing containers
    c1_end = body_html.find('Avance en el Ecosistema')
    if c1_end != -1:
        # Find the <header with style
        header2_idx = body_html.rfind('<header style', 0, c1_end)
        if header2_idx == -1:
            header2_idx = body_html.rfind('<header', 0, c1_end)
            
        if header2_idx != -1:
            tab_a = body_html[:header2_idx]
            tab_c = body_html[header2_idx:]
            
            # Clean up the Avance header since we have tabs now
            tab_c = re.sub(r'<header.*?</header>', '', tab_c, flags=re.DOTALL)
            
            tab_b = """
            <div class="container" style="margin-bottom: 60px;">
                <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--border-subtle); border-radius: 20px; padding: 30px; text-align: center;">
                    <h3 style="font-family:'Outfit'; color:var(--accent-fire); margin-bottom: 20px; font-size:1.5rem;">Crecimiento de Mentoras</h3>
                    
                    <div style="display:flex; justify-content:center; margin-bottom:30px;">
                        <select id="mentora-select" class="filter-select" style="width:100%; max-width:400px;" onchange="renderMentoraTab()">
                            <option value="">Selecciona una Mentora...</option>
                        </select>
                    </div>

                    <div id="mentora-tab-content" style="display:none; text-align:left;">
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom:30px;">
                            <div class="semaforo-box" style="margin-bottom:0;">
                                <h4 style="color:var(--accent-water); margin-bottom:10px; font-family:'Outfit';">Estilo de Mentoría Revelado</h4>
                                <p id="m-estilo" style="color:white; font-size:1.1rem; font-weight:bold;">--</p>
                                <p id="m-estilo-desc" style="color:var(--text-secondary); font-size:0.85rem; margin-top:8px;">--</p>
                            </div>
                            <div class="semaforo-box" style="margin-bottom:0;">
                                <h4 style="color:var(--accent-jefe); margin-bottom:10px; font-family:'Outfit';">Impacto sobre su Mentada</h4>
                                <p id="m-impacto" style="color:white; font-size:1.1rem; font-weight:bold;">--</p>
                                <p id="m-impacto-desc" style="color:var(--text-secondary); font-size:0.85rem; margin-top:8px;">--</p>
                            </div>
                        </div>

                        <h4 style="color:white; margin-bottom:15px; font-family:'Outfit';">Comparativa: Autoevaluación Inicial vs Día 78</h4>
                        <div style="background:rgba(0,0,0,0.4); border-radius:12px; padding:20px; border: 1px solid var(--border-subtle);">
                            <table class="comp-table">
                                <thead>
                                    <tr>
                                        <th>Competencia</th>
                                        <th>Inicial</th>
                                        <th>Día 78 (Actual)</th>
                                        <th>Crecimiento</th>
                                    </tr>
                                </thead>
                                <tbody id="m-crecimiento-body">
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            """
            
            new_body = f"""
            <div id="tab-parejas" class="tab-content active">
                {tab_a}
            </div>
            <div id="tab-mentoras" class="tab-content">
                {tab_b}
            </div>
            <div id="tab-avance" class="tab-content">
                {tab_c}
            </div>
            """
            content = content[:m2.start()] + new_body + m2.group(2) + content[m2.end():]
            
            with open('dashboard_diagnostico.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Tabs structure injected successfully.")
        else:
            print("header2_idx not found.")
    else:
        print("c1_end not found.")
else:
    print("m2 pattern not found.")
