"""
Dicionários em python
"""
d1 = {
    'str': 'valor da str',
    1: 1234,
    2: 'num2',
    3: 'num3'
}

del d1['str']

print('str' in d1)
print(1 in d1.keys())
print('num2' in d1.values())

print(len(d1))
