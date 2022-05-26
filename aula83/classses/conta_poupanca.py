from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('valor do saque precisa ser numérico')

        if valor > self.saldo:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
