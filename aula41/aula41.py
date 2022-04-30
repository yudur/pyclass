"""
add (adiciona), update (atualizar), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois “sets”)
difference - (elementos apenas no “set” da esquerda)
symmetric_difference ^ (Elementos que estão nos dois “sets”, mas não em ambos)
"""
s1 = set()

s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)
print(s1)

s1.discard(5)
print(s1)

s2 = set()
s2.update('python')
print(s2)

l1 = [1, 2, 6, 2, 3, 4, 2, 2, 2, 4, 4, 5, 6, 6, 7, 7, 6, 8, 7, 8, 9, 9, 'YUDI', 'YUDI']
l1 = set(l1)
l1 = list(l1)
print(l1)
