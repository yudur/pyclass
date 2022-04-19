nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
print()

if not nome and not idade:
    print('por favor volte e digite seu nome e a sua idade')
elif not nome:
    print('volte e digite o seu nome')
elif not idade:
    print('por favor volte e digite a sua idade')
else:
    print('parabéns você foi aceito ')
