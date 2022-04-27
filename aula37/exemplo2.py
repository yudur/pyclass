product_list = [
    ['smartphone', 3200.00],
    ['smartwatch', 145.00],
    ['tesla car', 46900.00],
    ['yamaha motorcycle', 33319.00],
    ['video game', 4499.90]
]
while True:
    print()
    print('0 - sair do programa')
    print('1 - exibir os preços padrão')
    print('2 - exibir preços do mais barato ao mais caro ')
    print('3 - exibir preços do mais caro ao mais barato ')
    print()

    display_order = (input('digite algum número: '))

    if display_order == '0':
        exit()

    elif display_order == '1':
        print(product_list)

    elif display_order == '2':
        print(sorted(product_list, key=lambda value: value[1]))

    elif display_order == '3':
        print(sorted(product_list, key=lambda value: value[1], reverse=True))

    else:
        print('por favor digite apenas (0, 1, 2, 3) ')
