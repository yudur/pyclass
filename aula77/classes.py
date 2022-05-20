class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self, *args, **kwargs):
        if args:
            print(f'{args[0]} está escrevendo com a caneta...')
        if kwargs:
            for values in kwargs.values():
                print(f'{values} está escrevendo com a máquina...')
                break
        if not args and not kwargs:
            print('estou escrevendo com a caneta...')


class MaquinaDeEscrever:
    def escrever(self, *args, **kwargs):
        if args:
            print(f'{args[0]} está escrevendo com a máquina...')
        if kwargs:
            for value in kwargs.values():
                print(f'{value} está escrevendo com a máquina...')
                break
        if not kwargs and not args:
            print('estou digitando com a máquina...')
