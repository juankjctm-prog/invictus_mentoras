html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

inject_str = '<script>window.onerror = function(msg, url, line, col, error) { alert("Error: " + msg + " (Line " + line + ")"); }; window.onunhandledrejection = function(e) { alert("Promise Error: " + (e.reason ? (e.reason.message || e.reason) : "Unknown Promise Error")); };</script>'

if "window.onerror = function" not in content:
    content = content.replace("<head>", "<head>\\n" + inject_str)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected error alert.")
else:
    print("Already injected.")
