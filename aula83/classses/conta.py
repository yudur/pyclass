from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('saldo precisa ser numérico')

        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('valor do deposito precisa ser numérico')

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'agencia: {self.agencia}', end='   ')
        print(f'conta: {self.conta}', end='   ')
        print(f'saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
