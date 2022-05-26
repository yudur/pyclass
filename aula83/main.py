"""
Classes Abstratas — Python Orientado a Objetos
"""
from conta_poupanca import ContaPoupanca
from classses.conta_corrente import ContaCorrente

cp = ContaPoupanca('Banco do Brasil', 'Conta Poupança', 0)
cp.depositar(899)
cp.depositar(154.50)

cp.sacar(100.45)
cp.sacar(1000)

print('#' * 50)

cc = ContaCorrente('PayPal', 'Conta Corrente', 0)
cc.depositar(100)

cc.sacar(150)
cc.sacar(100)

cc.depositar(322.65)
