def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    print()
    numero = converte_numero(input('digite um número: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('isso não é um número')
