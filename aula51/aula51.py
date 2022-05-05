"""
count - itertools
"""

from itertools import count

contador = count(start=1)
lista = ['José', 'Maria', 'Marlon', 'Joana']

lista = zip(contador, lista)
print(list(lista))
