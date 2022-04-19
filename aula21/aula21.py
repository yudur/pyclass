#        índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
frase_tamanho = len(frase)
contador = 0
nova_str = ''

letra_do_usuario = input('digite qual letra você quer maiúscula: ')

while contador < frase_tamanho:
    letra = frase[contador]
    if letra == letra_do_usuario:
        nova_str += letra_do_usuario.upper()
    else:
        nova_str += letra
    contador += 1

print(nova_str)
