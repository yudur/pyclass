pessoas = ['João', 'Alon', 'Lara', 'Yudi']

for valor in pessoas:
    if valor.lower().startswith('l'):
        print('existe alguém com "L" no grupo!')
        break
else:
    print('não existe ninguém com "L" no grupo')
