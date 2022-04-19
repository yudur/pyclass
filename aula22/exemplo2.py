txt = ''
nova_string = ''

for letra in txt:
    if letra == '':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
