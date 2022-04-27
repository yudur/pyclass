"""
2 — Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def funcao1():
    valor = 'The power of imagination makes us infinite. '
    return valor


def funcao2():
    valor2 = 'Never give up!'
    return valor2


def funcao_mestre(function, function1):
    print(function)
    print(function1)


vlr1, vlr2 = funcao1(), funcao2()

funcao_mestre(vlr1, vlr2)
