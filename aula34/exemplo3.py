"""
3 — Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def aumento(valor, porcentagem):
    return valor * (porcentagem / 100) + valor


print(aumento(100, 60))

print(aumento(800, 50))

print(aumento(500, 50))
