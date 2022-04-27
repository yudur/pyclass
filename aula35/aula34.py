"""
Funções  (def) em python - *args **kwarg
"""


def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    
    if nome and idade:
        print(f'olá {nome}! Quer dizer que você ja tem {idade} anos')
    elif nome:
        print(f'olá {nome}')
    else:
        print(f'quer dizer que você ja tem {idade}')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40]

func(*lista, *lista2, nome='Yudi', idade=13)
