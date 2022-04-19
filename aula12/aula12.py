"""
operadores lógicos
and, or, not
"""

And1 = 12 == 12
And2 = 12 <= 12

print(And1 and And2)


idade = int(input('digite sua idade: '))

if idade >= 18 and idade <= 60:
    print('pode pegar')
else:
    print('não pode pegar')
print()

OR1 = 133 <= 200
OR2 = 5 == 10

print(OR1 or OR2)
