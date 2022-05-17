from random import randint

# Métodos estáticos -  Python Orientado a Objetos

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def calcula_idade(self):
        print(self.ano_atual - int(self.idade))
        return

    @classmethod
    def por_ano_de_nacimento(cls, nome, ano_nacimento):
        idade = cls.ano_atual - ano_nacimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(0000000000, 9999999999)
        return rand


p1 = Pessoa.por_ano_de_nacimento('Yudi', 2009)
print(p1)
print(p1.nome, p1.idade)
p1.calcula_idade()

print(Pessoa.gera_id())
print(p1.gera_id())
