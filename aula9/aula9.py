# entrada de dados

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
naceu = 2022 - int(idade)
print()
print('usuário: {} é do tipo {}'.format(nome, type(nome)))
print('tem {} e nasceu em {}'.format(idade, naceu))
print()
num1 = int(input('digite um número: '))
num2 = int(input('digite um número: '))
print(num1 ** num2)
