"""
Groupby - Agrupando valores
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Yudi', 'nota': 'A'},
    {'nome': 'Isabella', 'nota': 'B'},
    {'nome': 'Icaro', 'nota': 'B'},
    {'nome': 'Israel', 'nota': 'C'},
    {'nome': 'Marlon', 'nota': 'A'},
    {'nome': 'Miguel', 'nota': 'C'},
    {'nome': 'Arthur', 'nota': 'D'},
    {'nome': 'Marlon', 'nota': 'D'},
    {'nome': 'Heitor', 'nota': 'A'},
    {'nome': 'Marlon', 'nota': 'B'},
    {'nome': 'Alice', 'nota': 'D'},
    {'nome': 'Theo', 'nota': 'B'},
    {'nome': 'Davi', 'nota': 'A'},
    {'nome': 'Laura', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'C'},
    {'nome': 'Sophia', 'nota': 'A'},
    {'nome': 'Maria Clara', 'nota': 'C'},
    {'nome': 'Maria Júlia', 'nota': 'C'},
    {'nome': 'Lorena', 'nota': 'C'},
    {'nome': 'Benício', 'nota': 'B'},
]


def ordenar():
    ordenar = lambda item: item['nota']
    return ordenar


alunos.sort(key=ordenar())
alunos_agrupados = groupby(alunos, ordenar())

for agrupados, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'alunos com nota {agrupados}:')

    for alunos in va1:
        print(f'\t{alunos}')

    print()
    print(f'\t{len(list(va2))} alunos tiraram {agrupados}')

    print()
