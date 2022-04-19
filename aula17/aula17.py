"""
formando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de pontos flutuantes (float)
:. (NÚMERO)f - quantidade de casas decimais (float)
: (CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)

> Esquerda
< Direita
^ Centro
"""

num1 = 10
num2 = 3
divisao = 10 / 3
print('{:.2f}'.format(divisao))
print()

nome = '.yudi mendes duarte.'
print('{:s}'.format(nome))
print()

num_1 = 1234
print('{:0<10}'.format(num_1))
print('{:0>10}'.format(num_1))
print('{:0^10}'.format(num_1))
print('{:0>10.6f}'.format(num_1))
print('{:!^40}'.format(nome))
