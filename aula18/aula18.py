"""
Manipulando Strings
* String indices
* Fatiamentos de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos [0 1 2 3 4 5 6]
texto = 'yudi S2'
print(texto[5])

print()

# negativos -[16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1]
url = 'www.github.com/'
print(url[:-1])

print()

# fatiamento
print(texto[0:4])

print(url[4:11])

print(url[-12:-5])

print(url[0::5])
