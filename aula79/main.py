from classes import *

cliente1 = Cliente('Matheus', 21)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome, cliente1.idade)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 60)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio De Janeiro', 'RJ')
print(cliente2.nome, cliente2.idade)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 18)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome, cliente3.idade)
cliente3.lista_enderecos()
