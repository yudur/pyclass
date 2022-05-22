class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.name_class = self.__class__.__name__

    def falar(self):
        print(f'{self.name_class} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.name_class} está comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.name_class} está estudando...')
