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

    def falar(self):
        print('estou em CLIENTE.')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.name_class} está estudando...')


class ClienteVIP(Cliente):
    def __init__(self, nome, sobrenome, idade):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando')
