d1 = {
    'chave1': 'num0',
    'chave2': 'num1',
    'chave3': 'num2',
    'chave4': 'num3'
}

for k in d1:
    print(k)

print()

for v in d1.values():
    print(v)

print()

for k, v in d1.items():
    print(f'{k}: {v}')
