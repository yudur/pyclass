secreto = 'motoqueiro'
digitadas = []

while True:
    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('ahh isso não vale, digite apenas uma letra')
        continue

    elif letra.isnumeric():
        print('ahh isso não vale, {} não é uma letra'.format(letra))
        continue

    elif letra.isspace():
        print('ahh isso não vale, digite apenas letras')
        continue

    digitadas.append(letra)

    print(digitadas)
