"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""
from classes import *

c1 = Cliente('Yudi', 34)
print(c1.nome)
print(c1.idade)
c1.comprar()
print()

a1 = Aluno('Jonathan', 13)
print(a1.nome)
print(a1.idade)
a1.falar()
a1.estudar()
