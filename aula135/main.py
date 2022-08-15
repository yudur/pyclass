# \w == [a-zA-Z0-9Á-ú_]
# \w == [a-zA-Z0-9_] == re.A re.ASCII

# \W == [^a-zA-Z0-9Á-ú_]
# \W == [^a-zA-Z0-9_] == re.A re.ASCII

# \d == [0-9]
# \D == [^0-9]

# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]

# \b -> borda
# \B -> não borda

# re.I == re.IGNORECASE
# re.A == re.ASCII
# re.M == re.MULTILINE == ^ $   
# re.S == re.DOTALL

import re


texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[a-zA-Z0-9Á-ú]{1,}', texto))
print(re.findall(r'\w{1,}', texto))

# print(re.findall(r'[^a-zA-Z0-9Á-ú]{1,}', texto))
print(re.findall(r'\W{1,}', texto))

# print(re.findall(r'[0-9]{1,}', texto))
print(re.findall(r'\d{1,}', texto))

# print(re.findall(r'[^0-9]{1,}', texto))
print(re.findall(r'\D{1,}', texto))

# print(re.findall(r'[ \r\n\f\n\t]+', texto))
print(re.findall(r'\s+', texto))

# print(re.findall(r'[^ \r\n\f\n\t]+', texto))
print(re.findall(r'\S+', texto))

print(re.findall(r'\be\w+', texto, flags=re.I))

print(re.findall(r'\Be\w+', texto, flags=re.I))


print()

texto2 = '''
131.768.460-53 ABC
055.123.060-50
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto2, flags=re.M))

texto3 = '''O João gosta de folia 
E adora ser amado'''

print(re.findall(r'^o.*o$', texto3, flags=re.I | re.S))