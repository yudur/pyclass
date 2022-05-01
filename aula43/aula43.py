# List Comprehension em python

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['João', 'Maria', 'Karla']
ex4 = [v.replace('a', 'A') for v in l2]

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
    ('chave4', 'valor4')
)
ex5 = [(y, x) for x, y in tupla]
ex5 = tuple(ex5)

l3 = list(range(1, 101))
ex6 = [v for v in l3 if v % 2 == 0]

ex7 = [v if v % 5 == 0 or v % 8 == 0 else 'x' for v in l3]

print(ex7)
