import sys

lista = [v for v in range(100000)]

print(type(lista))
print(f'números de bytes da lista: {sys.getsizeof(lista)}')

print()

gerador = (v for v in range(100000))

print(type(gerador))
print(f'números de bytes do gerador: {sys.getsizeof(gerador)}')

for g in gerador:
    print(g)

    if g == 20:
        break

