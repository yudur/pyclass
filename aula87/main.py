"""
Métodos mágicos - Python Orientado a Objetos
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_existe'):
            cls._existe = object.__new__(cls)

        return cls._existe

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        resultado = 1
        for i in args:
            if not isinstance(i, (int, float)):
                continue
            resultado *= i

        for ii in kwargs.values():
            if not isinstance(ii, (int, float)):
                continue
            resultado *= ii
        return resultado

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Não pode!!!'
        else:
            self.__dict__[key] = value

    def __str__(self):
        return "<class A> usada para testes"

    def __len__(self):
        return 55555


a = A()
b = A()
print(a == b)

print(a(1, 2, 3, 'fala', 4, 5, 'oi', mul=2, plv='yudi'))

print()

a.nome = 'Yudi'
a.idade = 13

print(a.nome, a.idade)
print(a)

print(len(a))
