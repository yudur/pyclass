# https://docs.python.org/3/library/functions.html
# criando, lendo, escrevendo e apagando arquivos

file = open('poesia.txt', 'w+')
file.write('Olho em redor do bar em que escrevo estas linhas.\n')
file.write('Aquele homem ali no balcão, caninha após caninha,\n')
file.write('nem desconfia que se acha conosco desde o início\n')
file.write('das eras. Pensa que está somente afogando problemas\n')
file.write('dele, João Silva... Ele está é bebendo a milenar\n')
file.write('inquietação do mundo!\n')


file.seek(0, 0)
print('lendo arquivos: \n')
print(file.read())
print('#'*100)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#'*100)

file.seek(0, 0)
for line in file.readlines():
    print(line, end='')

file.close()
