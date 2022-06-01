"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError('nome precisa ser um str')
        if not isinstance(self.sobrenome, str):
            raise TypeError('sobrenome precisa ser um str')
        if not isinstance(self.idade, int):
            raise TypeError('idade precisa ser um int')

    @property
    def info(self):
        return f'nome: {self.nome} {self.sobrenome}\n' \
               f'idade: {self.idade}'


p1 = Pessoa('Yudi', 'Duarte', 13)
p2 = Pessoa('Yudi', 'Duarte', 13)

print(p1)

print(p1.nome)
print(p1.sobrenome)
print(p1.idade)

print()

print(p1 == p2)
print(p1 != p2)
print(p1 > p2)

print()

print(p1.info)

dicionario = asdict(p1)
tupla = astuple(p1)

print(dicionario)
print(tupla)
