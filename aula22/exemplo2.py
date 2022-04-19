txt = 'python"'
nova_string = ''

# continue — pula para o próximo laço
# break — termina o laço

for letra in txt:
    if letra == 'p':
        nova_string += letra.upper()
    elif letra == 'y':
        nova_string += letra.upper()
    elif letra == 'n':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
