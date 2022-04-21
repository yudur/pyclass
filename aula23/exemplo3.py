secreto = 'motoqueiro'
digitadas = []

while True:
    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('ahh isso não vale, digite apenas uma letra')
        continue

    elif not letra.isalpha():
        print('ahh isso não vale, digite só uma letra')
        continue

    digitadas.append(letra)

    print(digitadas)
