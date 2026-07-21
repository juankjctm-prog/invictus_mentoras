import codecs
import re

sb_cdn = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\n</head>'
sb_creds = """
        const supabaseUrl = 'https://unbaagnuwdhavqkajory.supabase.co';
        const supabaseKey = 'sb_publishable_8G_qiAoStdmRsEwPfvaa0g__2XlfLjV';
        const supabase = supabase.createClient(supabaseUrl, supabaseKey);
"""

# Patch diagnostico_mentora.html
with codecs.open('diagnostico_mentora.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

if 'supabase-js' not in text:
    text = text.replace('</head>', sb_cdn)

finish_func_old = r'function finish\(\)\s*\{\s*window\.location\.href\s*=\s*\'[^\']+\';\s*\}'
finish_func_new = """async function finish() {
            try {
                const userPin = localStorage.getItem('user_pin');
                if(!userPin) {
                    window.location.href = 'index.html';
                    return;
                }
                const data = JSON.parse(localStorage.getItem('mm_diag_mentora') || '{}');
                
                const { error } = await supabase
                    .from('user_diagnostics')
                    .insert([{
                        user_pin: userPin,
                        role: 'mentora',
                        lectura_ppm: data.lectura ? data.lectura.ppm : null,
                        lectura_comprension_pct: data.lectura ? data.lectura.comprension : null,
                        mentoria_score: data.mentoria ? data.mentoria.total : null,
                        brechas: data.brechas || {}
                    }]);
                
                if (error) console.error("Error guardando diagnostico:", error);
            } catch(e) {
                console.error(e);
            }
            window.location.href = 'app.html?pin=' + localStorage.getItem('user_pin');
        }"""

if sb_creds not in text:
    text = text.replace('// DIAGNOSTICO MENTORA - LOGICA', '// DIAGNOSTICO MENTORA - LOGICA\n' + sb_creds)

text = re.sub(finish_func_old, finish_func_new, text)

with codecs.open('diagnostico_mentora.html', 'w', 'utf-8') as f:
    f.write(text)


# Patch diagnostico_mentoreada.html
with codecs.open('diagnostico_mentoreada.html', 'r', 'utf-8', errors='ignore') as f:
    text2 = f.read()

if 'supabase-js' not in text2:
    text2 = text2.replace('</head>', sb_cdn)

finish_func_new_mentoreada = """async function finish() {
            try {
                const userPin = localStorage.getItem('user_pin');
                if(!userPin) {
                    window.location.href = 'index.html';
                    return;
                }
                const data = JSON.parse(localStorage.getItem('mm_diag_mentoreada') || '{}');
                
                const { error } = await supabase
                    .from('user_diagnostics')
                    .insert([{
                        user_pin: userPin,
                        role: 'mentoreada',
                        lectura_ppm: data.lectura ? data.lectura.ppm : null,
                        lectura_comprension_pct: data.lectura ? data.lectura.comprension : null,
                        mentoria_score: null,
                        brechas: data.brechas || {}
                    }]);
                
                if (error) console.error("Error guardando diagnostico:", error);
            } catch(e) {
                console.error(e);
            }
            window.location.href = 'app.html?pin=' + localStorage.getItem('user_pin');
        }"""

if sb_creds not in text2:
    text2 = text2.replace('// DIAGNOSTICO MENTOREADA - LOGICA', '// DIAGNOSTICO MENTOREADA - LOGICA\n' + sb_creds)
    if 'DIAGNOSTICO MENTOREADA - LOGICA' not in text2:
        # fallback
        text2 = text2.replace('let currentStep = 0;', sb_creds + '\n        let currentStep = 0;')

text2 = re.sub(finish_func_old, finish_func_new_mentoreada, text2)

with codecs.open('diagnostico_mentoreada.html', 'w', 'utf-8') as f:
    f.write(text2)

print("Diagnostics patched!")
