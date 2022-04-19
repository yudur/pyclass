n0 = input('digite um número: ')
print()

if not n0.isnumeric():
    print('por favor volte e digite um número inteiro')
else:
    print('-'*20)
    print('{} x  1 = {}'.format(n0, int(n0) * 1))
    print('{} x  2 = {}'.format(n0, int(n0) * 2))
    print('{} x  3 = {}'.format(n0, int(n0) * 3))
    print('{} x  4 = {}'.format(n0, int(n0) * 4))
    print('{} x  5 = {}'.format(n0, int(n0) * 5))
    print('{} x  6 = {}'.format(n0, int(n0) * 6))
    print('{} x  7 = {}'.format(n0, int(n0) * 7))
    print('{} x  8 = {}'.format(n0, int(n0) * 8))
    print('{} x  9 = {}'.format(n0, int(n0) * 9))
    print('{} x 10 = {}'.format(n0, int(n0) * 10))
    print('-'*20)
