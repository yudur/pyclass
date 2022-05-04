"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [1, 2.50, 7.90, 4]

values = zip(list_1, list_2)

sum_of_lists = [(L + R) for L, R in values]

print(sum_of_lists)
