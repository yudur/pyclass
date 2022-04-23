"""
Split, join, Enumerate em python
* Split - Dividir uma string # str
* join - juntar uma lista # str
* Enumerate - Enumerar elementos da listas # list
"""
string = 'O Brasil é o país do futebol. o Brasil é penta'

lista_1 = string.split(' ')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print('a palavra que apareceu mais vezes foi {} {}x'.format(palavra, contagem))
