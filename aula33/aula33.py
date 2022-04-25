"""
Funções — def em python
"""


def saudacao(msg='HELLO', nome='usuário'):
    msg = msg.replace('e', '3')
    nome = nome.replace('e', '3')
    print(msg, nome)
    return f'{msg}  {nome}'


print(saudacao())
