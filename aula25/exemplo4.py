"""
Tirando duvidadas
* Enumerate — Enumerar elementos da lista # list
"""
#       0      1       2
lista = [
    ['Edu', 'João', 'Luiz'],  # 0
    ['Ana', 'Mariana', 'Joana'],  # 1
    ['Eloisa', 'Marcia', 'Leonardo']  # 2
]

print(lista[0], '    ', lista[1], '    ', lista[2])
print(lista[0][0])
print(lista[1][1])
print(lista[2][2])

print()

for v1 in enumerate(lista, 1):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)
