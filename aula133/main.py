# Grupos e Retrovisores

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Oxi</p> <p>Qualquer frase</p> <div>1</div>
'''

cpf = '123.456.789-00'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)
pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(</.+?>)', r'\1 Mais \3 Qualquer \4', texto))

# for tag in tags:
#     print(tag[0])