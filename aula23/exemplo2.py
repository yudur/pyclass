lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2

print(lista_1)
print(lista_2)
print(lista_3)

# extend — faz a junção de duas listas
lista_1.extend(lista_2)
print(lista_1)

print()

# append — adiciona um valor no final da lista
lista_1.append('abc')
print(lista_1)

print()

# insert — adiciona um valor em qualquer posição
lista_1.insert(0, 'maçã')
print(lista_1)

print()

# pop — apagar qualquer coisa da lista
lista_1.pop(0)
lista_1.pop(-1)
print(lista_1)

print()

# del — deleta um valor usando o fatiamento
del(lista_1[3:6])
print(lista_1)

print()

# max — mostra o maior valor da lista
print(max(lista_1))

print()

# min — mostra o menor valor da lista
print(min(lista_1))

# range — podemos adicionar valores a lista mais rapido
lista_1 = list(range(0, 11))
print(lista_1)

