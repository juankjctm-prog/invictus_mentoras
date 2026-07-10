file = 'index.html'
content = open(file, encoding='utf-8').read()
content = content.replace(r'<head>\n<script>window.onerror = function(msg, url, line, col, error) { alert("Error: " + msg + " (Line " + line + ")"); }; window.onunhandledrejection = function(e) { alert("Promise Error: " + (e.reason ? (e.reason.message || e.reason) : "Unknown Promise Error")); };</script>', '<head>')
with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
