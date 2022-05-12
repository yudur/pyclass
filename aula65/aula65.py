# Funções decoradoras e decoradores

def master(function):
    def slaver(*args, **kwargs):
        print('agora estou decorada.')
        function(*args, **kwargs)

    return slaver


@master
def falo_oi():
    print('falei oi')


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('eu sou o Yudi')
