"""
 operadores relacionais

== igualdade

> maior que

< menor que

>= maior ou igual a

<= menor ou igual a

!= diferente
"""

num1 = 10
num2 = 10
print('quando usamos "=" nós estamos comparando ele por '
      'exemplo: {} é igual a {}: {}'.format(num1, num2, num1 == num2))
print()

print('quando usamos ">" nós estamos perguntando se ele "é maior que" '
      'por exemplo: {} é maior que {}: {}'.format(num1, num2, num1 > num2))
print()

print('quando usamos "<" nós estamos perguntando se ele "é menor que" '
      'por exemplo: {} é menor que {}: {}'.format(num1, num2, num1 < num2))
print()

print('quando usamos ">=" nós estamos perguntando se ele "é maior que ou igual a" '
      'por exemplo: {} é maior que ou igual a {}: {}'.format(num1, num2, num1 >= num2))
print()

print('quando usamos "<=" nós estamos perguntando se ele "é menor que ou igual a" '
      'por exemplo: {} é menor que ou igual a {}: {}'.format(num1, num2, num1 <= num2))
print()

print('quando usamos "!=" nós estamos perguntando se ele "é diferente de" '
      'por exemplo: {} é diferente de {}: {}'.format(num1, num2, num1 != num2))
print()

nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

#  verificador de empréstimo
if 18 <= idade <= 50:
    print('olá senhor {}, você pode fazer um empréstimo.'.format(nome))

else:
    print('me desculpe você não pode fazer um empréstimo')
