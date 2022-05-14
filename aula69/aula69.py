from random import randint
from aula68.cnpj import val_inv
from colorama import Fore

print(Fore.YELLOW + '...Gerador de cnpj valido... \n')

while True:
    parte1 = str(randint(00, 99))
    parte2 = str(randint(100, 999))
    parte3 = str(randint(100, 999))
    parte4 = str(randint(10, 99))
    gerador_cnpj = parte1 + parte2 + parte3 + '0001' + parte4

    if val_inv(gerador_cnpj):
        print(Fore.GREEN + gerador_cnpj)
        print(f'{gerador_cnpj[0:2]}.{gerador_cnpj[2:5]}.{gerador_cnpj[5:8]}'
              f'/{gerador_cnpj[8:12]}-{gerador_cnpj[12:14]}')
        print()
    else:
        continue

    continuar = input(Fore.BLUE + 'deseja gerar outro cnpj [SIM/NÃO]: ')

    try:
        if continuar[0].upper() == 'S':
            continue
        elif continuar[0].upper() == 'N' or continuar[0].upper() != 'S':
            break

    except IndexError:
        print(Fore.RED + 'ERROR')
        break
