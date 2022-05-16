from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, genero, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} ainda está falando')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        print(f'{self.nome} falou: {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando nada')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def ano_de_nacimento(self):
        return self.ano_atual - int(self.idade)
