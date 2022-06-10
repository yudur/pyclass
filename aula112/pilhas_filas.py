from collections import deque

# pilha (stack)
livros = []
livros.append('livro 1')
livros.append('livro 2')
livros.append('livro 3')
livros.append('livro 4')
livros.append('livro 5')

livro_removido = livros.pop()
livro_removido = livros.pop()
livro_removido = livros.pop()

print(livros)
print(livro_removido)

print()

# fila (deque)
fila = deque(maxlen=5)

fila.append('João')
fila.append('Marcos')
fila.append('Alice')
fila.append('Sara')
fila.append('Taina')
fila.append('Ana')


fila2 = deque(maxlen=10)

fila2.extend([1, 2, 3, 4, 5, 6])
fila2.insert(4, 'Marmelada')
print(fila2)
