while True:
    num1 = input('digite um número: ')
    num2 = input('digite outro número: ')
    operador = input('digite um operador (+ - x %): ')

    num_1 = int(num1)
    num_2 = int(num2)

    if operador == '+':
        print('{} + {} = {}'.format(num_1, num_2, num_1 + num_2))
    elif operador == '-':
        print('{} - {} = {}'.format(num_1, num_2, num_1 - num_2))
    elif operador == 'x':
        print('{} x {} = {}'.format(num_1, num_2, num_1 * num_2))
    else:
        print('{} % {} = {}'.format(num_1, num_2, num_1 / num_2))
