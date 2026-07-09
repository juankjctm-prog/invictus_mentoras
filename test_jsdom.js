const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('Invictus_Mentoras.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (err) => {
  console.error("JSDOM Error:", err.message || err);
});
virtualConsole.on("jsdomError", (err) => {
  console.error("JSDOM jsdomError:", err.message);
  console.error(err.detail);
});

// Mock Supabase to simulate a successful login
const mockScript = `
    const supabase = {
        createClient: () => ({
            from: (table) => ({
                select: () => ({
                    eq: () => ({
                        single: async () => {
                            if(table === 'mentoras_users') {
                                return { data: { id: 'mock-id', role: 'Mentada' }, error: null };
                            } else if (table === 'mentoras_progress') {
                                return { data: null, error: null };
                            }
                        }
                    })
                }),
                delete: () => ({ eq: async () => ({}) })
            }),
            channel: () => ({
                on: () => ({ subscribe: () => {} })
            })
        })
    };
`;

const dom = new JSDOM(mockScript + html, { 
    runScripts: "dangerously",
    virtualConsole,
    url: "http://localhost"
});

setTimeout(() => {
    console.log("Calling login()");
    try {
        dom.window.document.getElementById('pin-input').value = '1234';
        dom.window.login().then(() => {
            console.log("Login finished");
            console.log("Current Day in DOM:", dom.window.document.querySelector('.session-hero h2').innerText);
        }).catch(err => {
            console.error("Login Promise Error:", err);
        });
    } catch(e) {
        console.error("Login call error:", e);
    }
}, 1000);
