# Geradores, Iteradores e Iteráveis em Python

def gera():
    variavel = 'valor1'
    yield variavel

    variavel = 'valor2'
    yield variavel

    variavel = 'valor3'
    yield variavel


g = gera()

for v in g:
    print(v)
