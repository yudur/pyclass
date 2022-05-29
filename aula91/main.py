from cliente import Cliente
from contas import ContaCorrente, ContaPoupanca
from banco import Banco

c1 = Cliente('Maria', 32)
c2 = Cliente('Joana', 18)
c3 = Cliente('Marcos', 21)

conta1 = ContaCorrente('bxc', 123, 0)
conta2 = ContaPoupanca('2231', 321, 12)
conta3 = ContaCorrente('bxc', 12345, 1000)

c1.inserir_conta(conta1)
c2.inserir_conta(conta2)
c3.inserir_conta(conta3)

banco = Banco()

banco.adicionar_cliente(c1)
banco.adicionar_cliente(c2)
banco.adicionar_cliente(c3)

banco.inserir_conta(conta1)
banco.inserir_conta(conta2)
banco.inserir_conta(conta3)


if banco.autentificar_cliente(c1):
    c1.conta.depositar(200)
    c1.conta.depositar(10)
else:
    print('não autentificado')

if banco.autentificar_cliente(c2):
    c2.conta.sacar(70)
else:
    print('não autentificado')

if banco.autentificar_cliente(c3):
    c3.conta.depositar(500)
    c3.conta.sacar(320)
    c3.conta.sacar(1230)
else:
    print('não autentificado')

print()

c1.conta.detalhes()
c2.conta.detalhes()
c3.conta.detalhes()
