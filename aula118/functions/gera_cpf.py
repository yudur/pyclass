from random import randint

def gera_cpf():
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

    return novo_cpf


if __name__ == '__main__':
    print(gera_cpf())
