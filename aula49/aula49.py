"""
Zip - Unindo iteráveis
Zip_longest - itertools
"""

from itertools import count

index = count(1)
City = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Monte Belo']
state = ['SP', 'MG', 'BA']

cities_and_states = zip(index, state, City)

for index, state, City in cities_and_states:
    print(index, state, City)
