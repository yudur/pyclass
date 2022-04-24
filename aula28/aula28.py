"""
Operador ternário em python
"""
logged_user = True
msg1 = 'usuário logado' if logged_user else 'usuário precisa logar'


print(msg1)

print()

idade = input('digite a sua idade: ')
msg2 = 'você pode acessar' if int(idade) >= 18 else 'não pode acessar'

print(msg2)
