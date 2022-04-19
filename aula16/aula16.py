#  exercício 1

num = input('digite um número: ')
print()

if not num.isnumeric():
    print('por favor digite um número inteiro')

elif int(num) % 2:
    print('o número {} é impar'.format(num))

else:
    print('o número {} é par'.format(num))
