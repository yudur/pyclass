pessoas = ['João', 'Alon', 'Lara', 'Yudi']
existe_L = False

for valor in pessoas:
    if valor.startswith('L'):
        existe_L = True

if existe_L:
    print('existe alguém com "L" no grupo!')
else:
    print('não existe ninguém com "L" no grupo')
