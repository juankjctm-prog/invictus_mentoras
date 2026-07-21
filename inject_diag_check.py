import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

target = "localStorage.setItem('user_name', user.name);"
injection = """localStorage.setItem('user_name', user.name);
                
                // Check if diagnosis is complete
                try {
                    let { data: diagData, error: diagError } = await supabase
                        .from('user_diagnostics')
                        .select('*')
                        .eq('user_pin', pin);

                    if (!diagError && (!diagData || diagData.length === 0)) {
                        if (user.role === 'mentora') {
                            window.location.href = 'diagnostico_mentora.html';
                        } else {
                            window.location.href = 'diagnostico_mentoreada.html';
                        }
                        return;
                    }
                } catch(e) { console.error("Diagnostic check failed:", e); }
"""

if target in text and 'user_diagnostics' not in text:
    text = text.replace(target, injection)
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Injected diagnostic check into app.html successfully.")
else:
    print("Could not find target or already injected.")
