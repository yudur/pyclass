#  len

usuario = input('digite seu nome de usuário: ')
quant = len(usuario)

if quant < 10:
    print('seu texto a menos de 10 caracteres')
else:
    print('seu texto tem mais de 10 caracteres')
print()

algo1 = input('digite algo: ')
algo2 = input('digite outra coisa: ')

print('{} + {} tem {} caracteres ao total'.format(algo1, algo2, len(algo1) + len(algo2)))
