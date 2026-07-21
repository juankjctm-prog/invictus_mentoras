import codecs
import re

with codecs.open('app.html', 'r', 'utf-8', errors='ignore') as f:
    text = f.read()

# Let's find auth-overlay
match = re.search(r'<div id="auth-overlay".*?</div>', text, re.IGNORECASE | re.DOTALL)
if match:
    print('AUTH OVERLAY FOUND')
else:
    print('NO AUTH OVERLAY')

# Let's find any login function
match2 = re.search(r'function .*?login.*?\{', text, re.IGNORECASE)
if match2:
    print('LOGIN FUNC:', match2.group(0))

match3 = re.search(r'localStorage\.setItem\([\'\"]user_pin[\'\"]', text, re.IGNORECASE)
if match3:
    print('USER_PIN SET IN APP.HTML')
