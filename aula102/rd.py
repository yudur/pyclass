import random
import string

# Gera um número inteiro de A e B
inteiro = random.randint(0, 100)

# Gerar um número aleatorio usando a função range()
inteiro1 = random.randrange(0, 101, 10)

# Gera um número de ponto flutuante aleatorio de A e B
flutuante = random.uniform(0, 100)

# Gera um número de ponto flutuante entre 0 e 1
flutuante1 = random.random()


lista = ['Danilo', 'Felipe', 'João', 'José', 'Daniel', 'Matheus', 'Joana']
# Ele seleciona aleatóriamente valores de uma lista
sorteio = random.choice(lista)
sorteio1 = random.choices(lista, k=2)
sorteio2 = random.sample(lista, 2)

# Embaralha a lista
random.shuffle(lista)

# gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteris = '!@#$%&*()_.'
geral = letras + digitos + caracteris
senha = ''.join(random.choices(geral, k=20))
print(senha)
