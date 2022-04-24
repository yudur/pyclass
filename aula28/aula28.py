"""
Operador ternário em python
"""
logged_user = True
msg1 = 'usuário logado' if logged_user else 'usuário precisa logar'


print(msg1)

print()

while True:
    idade = input('digite a sua idade: ')

    if not idade.isnumeric():
        print('por favor digite só números')
        print()
        continue

    msg2 = 'você pode acessar' if int(idade) >= 18 else 'não pode acessar'

    print(msg2)
    exit()
