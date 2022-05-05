"""
Combinations, Permutations e Product — itertools
Combinação — Ordem não importa
Permutação — Ordem importa
Produto — Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Letícia', 'Manoel', 'Yudi']

print('Ordem não importa')
for grupo in combinations(pessoas, 2):
    print(grupo)

print()

print('Ordem importa')
for grupo in permutations(pessoas, 2):
    print(grupo)

print()

print('Ordem importa e repete valores únicos')
for grupo in product(pessoas, repeat=2):
    print(grupo)
