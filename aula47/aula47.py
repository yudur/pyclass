"""
Comportamento de geradores e iteradores
"""

# listas, tuplas, str -> sequencias -> iteráveis
name = 'Yudi Mendes Duarte'
iterador = iter(name)
gerador = (Letter for Letter in name)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:
    print(letra)


try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))


except:
    pass

print('CADE OS VALORES?')
for valuer in iterador:
    print(valuer)
