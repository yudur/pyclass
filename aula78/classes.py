class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, *produtos):
        for produto in produtos:
            self.produtos.append(produto)

    def lista_produtos(self):
        for produtos in self.produtos:
            print(produtos.nome, 'R$:', produtos.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor