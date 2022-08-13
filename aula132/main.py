# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ?  0 ou 1
# {n}
# {min, max}

import re

texto = '''
<p>Frase 1</p> <p>Oxi</p> <p>Qualquer frase</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
