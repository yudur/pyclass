class TaEradoError(Exception): pass


def testar():
    raise TaEradoError('Ta errado!')


try:
    testar()
except TaEradoError as error:
    print(f'Error: {error}')
