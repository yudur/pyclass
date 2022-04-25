"""
gerando CPFs em python
"""

from random import randint

while True:
    numero = str(randint(100000000, 999999999))

    novo_cpf = numero

    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    print(novo_cpf)

    continuar = input('deseja gerar outro CPF (S/N): ')

    if continuar[0].upper() == 'S':
        continue

    if continuar[0].upper() == 'N':
        exit()
