secreto = 'motor'
digitadas = []

while True:
    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('ahh isso não vale, digite apenas uma letra.')
        continue

    elif not letra.isalpha():
        print('ahh isso não vale, digite só uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('hehe a letra "{}" existe na palavra secreta.  :) '.format(letra))

    else:
        print('aff a letra "{}" não existe na palavra secreta  :( '.format(letra))
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    print(secreto_temp)
