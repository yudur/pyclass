"""
Dictionary Comprehension em python
"""
lista = [
    ('key1', 'value1'),
    ('key2', 'value2'),
]
dictionary1 = {key.upper(): value.upper() for key, value in lista}

dictionary2 = {f'chave_{x}': x ** 2 for x in range(1, 6)}

print(dictionary2, type(dictionary2))
