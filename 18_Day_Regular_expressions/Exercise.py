import re

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match) 

