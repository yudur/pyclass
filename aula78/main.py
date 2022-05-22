# Agregação — Python Orientado a Objetos
from classes import CarrinhoDeCompras
from classes import Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('carne', 32.55)
p2 = Produto('camisa', 50)
p3 = Produto('maquina de lavar', 399.99)
p4 = Produto('iphone', 12000)

carrinho.inserir_produto(p1, p2, p3, p4)

carrinho.lista_produtos()
print(carrinho.soma_total())
