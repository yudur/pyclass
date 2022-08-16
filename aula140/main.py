import re


regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~]).{12,}'
    r'$',
    flags=re.MULTILINE
)

texto = """
VÁLIDAS
mkU390E]It}]  
l;258VQUgz:^  
,3iXD3-Rz7w}  
d{mY}7[P9nL0  
>Aiz86V`*h9K  

SEM MINÚSCULAS
I+0]829B|{MN  
Q3PG}8}'S75{  
R7}<2 W30~CI
6>5S[DL00X>(
{Q"80P@C8&6I

SEM MINÚSCULAS E NÚMEROS
NN~N`_Z){GD]
^'Z[T~{BOOE>
O@TG?S]|B~@B
"~"K{OFE:MM@
CZ;|_~SCK:D.

SEM NÚMEROS CARACTERES E MINÚSCULAS
GIINSEEPKTLT
MVHMFEEVKYFN
UDWISRVXQZLW
AFERTPZXELFV
TCGETQZXDDOC

QUANTIDADE INVÁLIDA (6)
5rbT&6
a)95hQ
ie6Y1+
0?5mDd
v59>eC
"""

print(regexp.findall(texto))