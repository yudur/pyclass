from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.ndc = numero_da_conta
        self.saldo = saldo

    def depositar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('O sistema aceita apenas valores numéricos')
            return
        self.saldo += quantia

    def detalhes(self):
        print(f'Agencia: {self.agencia}', end='    ')
        print(f'Número da conta: {self.ndc}', end='    ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, quantia):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite=100):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('O sistema aceita apenas valores numéricos')
            return

        if quantia > (self.saldo + self.limite):
            print('o limite foi ultrapassado')
            return

        self.saldo -= quantia


class ContaPoupanca(Conta):
    def sacar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('O sistema aceita apenas valores numéricos')
            return

        if quantia > self.saldo:
            print('o seu saldo é insuficiente para sacar essa quantia')
            return

        self.saldo -= quantia
