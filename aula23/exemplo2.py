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

# append — adiciona um carácter no final da lista
lista_1.append('abc')
print(lista_1)

print()

# insert — adiciona um carácter em qualquer posição
lista_1.insert(0, 'maçã')
print(lista_1)

print()

# pop — apagar qualquer coisa da lista
lista_1.pop(0)
lista_1.pop(-1)
print(lista_1)
