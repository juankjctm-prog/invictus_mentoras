import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

nav_bar_match = re.search(r'<nav class="bottom-nav">.*?</nav>', text, re.IGNORECASE | re.DOTALL)
if nav_bar_match:
    print('APP NAV BAR:\n', nav_bar_match.group(0).encode('ascii', 'ignore').decode('ascii'))

libreta_match = re.search(r'<div id="view-libreta".*?(?:<nav class="bottom-nav"|</body>)', text, re.IGNORECASE | re.DOTALL)
if libreta_match:
    print('APP LIBRETA LEN:', len(libreta_match.group(0)))
