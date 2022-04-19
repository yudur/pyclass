"""
while / else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 20:
    print(contador, acumulador)

    if contador == 15:
        break

    acumulador = acumulador + contador
    contador = contador + 1

else:
    print('else no laço while')

print('não finalizado ')
