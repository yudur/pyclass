"""
Context Manager - Criando e Usando gerenciadores de contexto - Python Orientado a Objetos
"""
from contextlib import contextmanager


class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()


with Arquivo("abc.txt", 'w') as arquivo:
    arquivo.write('alguma coisa')

print()


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando arquivo')
        arquivo.close()


with abrir('ABCD.txt', 'w') as arq:
    arq.write('linha 1\n')
    arq.write('linha 2\n')
    arq.write('linha 3\n')
    arq.write('linha 4\n')
    arq.write('linha 5\n')
