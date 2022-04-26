"""
4 — Fizz Buzz — Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def fizzbuzz(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return 'fizz buzz'
    elif valor % 3 == 0:
        return 'fizz'
    elif valor % 5 == 0:
        return 'buzz'
    return valor


print(fizzbuzz(15))

print(fizzbuzz(10))

print(fizzbuzz(9))

print(fizzbuzz(2))
