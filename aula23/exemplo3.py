secreto = 'motoqueiro'
digitadas = []
chances = 5

while True:
    if chances < 1:
        print('VOCÊ PERDEU!!!')
        break

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

    if secreto_temp == secreto:
        print('PARABÉNS VOCÊ GANHOU!!!')
        break
    else:
        print(secreto_temp)

    if letra not in secreto:
        chances -= 1

    print('você ainda tem {} chances.'.format(chances))
    print()
