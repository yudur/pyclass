"""
Encapsulamento - Python Orientado a Objetos

_ private/protected (public _)
__ private (_NOMECLASSE__ATRIBUTO)
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for key, value in self.__dados['clientes'].items():
            print(f'{key}: {value}')

    def apagar_cliente(self, id):
        try:
            del self.__dados['clientes'][id]
        except KeyError:
            print('não ha valores para apagar')
            return


bd = BaseDeDados()

bd.inserir_cliente(1, 'Yudi')
bd.inserir_cliente(2, 'Debora')
bd.inserir_cliente(3, 'Ana')
bd.inserir_cliente(4, 'Jessica')
bd.inserir_cliente(5, 'Mario')

bd.apagar_cliente(5)
bd.apagar_cliente(4)
bd.lista_clientes()

bd.lista_clientes()
print(bd.dados)