from copy import deepcopy

d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Yudi', 'Matheus']}
v = deepcopy(d1)

v[1] = 'Yudi'
v[4][1] = 'Joãozinho'

print(d1)
print(v)
print(v[4][1])

print()

lista = [
    ['c1', 1],
    ('c2', 2),
    ['c3', 3],
    ['c4', 4],
]


d2 = dict(lista)

d3 = {
    1: 2,
    3: 4,
    4: 5
}

d2.pop('c4')
print(d2)

d2.update(d3)
print(d2)