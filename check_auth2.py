import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

match = re.search(r'<div id="auth-overlay".*?</script>', text, re.IGNORECASE | re.DOTALL)
if match:
    print('AUTH LOGIC:\n', match.group(0).encode('ascii', 'ignore').decode('ascii'))
