# ^ == começa com 
# $ == termina com
# [^a-z] == negação 

import re


cpf = '123.456.789-55'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))
