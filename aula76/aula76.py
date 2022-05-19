"""
[Reforço] - Getters e Setters - parte 1

SETTER = CONFIGURANDO UM VALOR (=)
GETTER = OBTER UM VALOR (.)
"""


class Pessoa:
    def __init__(self, nome):
        self._atributo = nome

    @property
    def nome(self):
        return self._atributo

    @nome.setter
    def nome(self, nome):
        print('SETTER foi executado.')
        nome += ' sei lá '
        self._atributo = nome


p1 = Pessoa('Yudi Duarte')
p1.nome = 'Otávio'

print(p1.nome)
