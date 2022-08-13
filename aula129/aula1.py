# introdução a expressões regulares
import re

# findall search sub
# compile

string = 'Este é um teste de expressões regulares. teste'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'XXXXXX', string))

print()

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('Trocou',string))