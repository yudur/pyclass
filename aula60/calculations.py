# Criando módulos em python

import math

PI = math.pi


def double_the_list(lista):
    return [l * 2 for l in lista]


def multiply_list(lista):
    r = 1
    for l in lista:
        r *= l
    return r


lista = [2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
    print(double_the_list(lista))
    print(multiply_list(lista))
    print(PI)
