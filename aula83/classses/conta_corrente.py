from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('valor do saque precisa ser numérico')

        if valor > (self.saldo + self.limite):
            print('seu limite foi atingido')
            return

        self.saldo -= valor
        self.detalhes()
