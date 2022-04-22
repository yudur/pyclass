"""
For / Else em python
"""
pessoas = ['Yudi', 'Yure', 'Yasmin', 'Alan', 'Abel']

for valores in pessoas:
    if valores.startswith('A'):
        print('{} começa com "A"'.format(valores))
    else:
        print('{} não começa com "A"'.format(valores))
