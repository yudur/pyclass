"""
1 — Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def funcao1():
    valor = 'today is a beautiful day'
    return valor


def funcao_mestre(function):
    print(function)


vrl = funcao1()
funcao_mestre(vrl)
