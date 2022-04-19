#  exercicio3

nome = input('digite seu primeiro nome: ')
print()

if len(nome) <= 4:
    print('seu nome é pequeno :(')

elif 5 <= len(nome) <= 6:
    print('seu nome é normal')

else:
    print('seu nome é grande')
