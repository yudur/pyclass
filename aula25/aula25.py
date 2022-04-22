"""
Split, join, Enumerate em python
* Split - Dividir uma string # str
* join - juntar uma lista # str
* Enumerate - Enumerar elementos da listas # list
"""
string = 'O Brasil é o país do futebol. O Brasil é penta'

lista_1 = string.split(' ')
lista_2 = string.split('.')

for valor in lista_1:
    print('a palavra {} apareceu {}x na frase'.format(valor, lista_1.count(valor)))
