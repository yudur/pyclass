"""
Implementando um iterator
"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, item):
        return self.__items[item]

    def __setitem__(self, index, valor):
        try:
            self.__items[index] = valor
        except IndexError:
            self.__items.append(valor)

    def __delitem__(self, key):
        try:
            del self.__items[key]
        except IndexError:
            return

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Yudi Duarte')
    lista.add('Manoel Silva')

    lista[2] = 1234567
    del lista[3]

    print(f'{lista[0]}       {lista[1]}')
