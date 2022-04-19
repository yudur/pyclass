nome = 'Yudi Duarte'
idade = 13
altura = 1.69
maior = idade > 18
peso = 60
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos e seu imc é de', imc)
print(f'{nome} tem {idade} anos e seu imc é de {imc:.2f}')
print('{} tem {} anos e seu imc é de {}'.format(nome, idade, imc))
