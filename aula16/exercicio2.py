#  exercicio 2

hora = input('digite a hora: ')
print()

if not hora.isnumeric():
    print('por favor digite um número')

elif 0 <= int(hora) <= 11:
    print('BOM DIA')

elif 12 <= int(hora) <= 17:
    print('BOA TARDE')

elif 18 <= int(hora) <= 24:
    print('BOA NOITE')

else:
    print('um dia só tem 24h vc é burro kslkslskslks')
