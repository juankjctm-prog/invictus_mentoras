import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

target = r'(// Success\s*currentUser = user;)'
injection = r'''\1

                // --- DIAGNOSTIC CHECK ---
                try {
                    let { data: diagData, error: diagError } = await _supabase
                        .from('user_diagnostics')
                        .select('*')
                        .eq('user_pin', currentPin);

                    // Only redirect if there's no error and array is empty
                    if (!diagError && (!diagData || diagData.length === 0)) {
                        localStorage.setItem('user_pin', currentPin);
                        if (user.role === 'mentora') {
                            window.location.href = 'diagnostico_mentora.html';
                        } else {
                            window.location.href = 'diagnostico_mentoreada.html';
                        }
                        return; // Stop further execution
                    }
                } catch(e) { console.error("Diag check error:", e); }
                // --- END DIAGNOSTIC CHECK ---
'''

if 'DIAGNOSTIC CHECK' not in text:
    text = re.sub(target, injection, text, flags=re.IGNORECASE)
    with codecs.open('app.html', 'w', 'utf-8') as f:
        f.write(text)
    print("Injected diagnostic check!")
else:
    print("Already injected or target not found.")
