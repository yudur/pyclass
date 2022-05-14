def val_inv(CNPJ):
    novo_cnpj = CNPJ[:-2]

    index = 0
    x = 5
    total = 0

    for i in range(12):
        if i < 4:
            i += x
            total += int(CNPJ[index]) * i
            index += 1
            x -= 2
            continue

        if i == 4:
            x = 5

        if i < 12:
            i += x
            total += int(CNPJ[index]) * i
            index += 1
            x -= 2

            d = 11 - (total % 11)

            if d > 9:
                d = 0

    novo_cnpj += str(d)

    x = 6
    total = 0
    index = 0
    for i_ in range(13):
        if i_ < 5:
            i_ += x
            total += int(CNPJ[index]) * i_
            index += 1
            x -= 2

            continue

        if i_ == 5:
            x = 4

        if i_ < 14:

            i_ += x
            total += int(CNPJ[index]) * i_
            index += 1
            x -= 2

            d = 11 - (total % 11)

            if d > 9:
                d = 0
    novo_cnpj += str(d)

    if CNPJ == novo_cnpj:
        return True
    else:
        return False


if __name__ == "__main__":
    cnpj = '04252011000110'
    if val_inv(cnpj):
        print(f'{cnpj} valido')
    else:
        print(f'{cnpj} invalido')
