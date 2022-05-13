# Mutável: listas, strings
# Imutáveis: tuplas, strings, números, True, False, None


def customer_list(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


primeira_lista = ['Pedro', 'Ana']
clientes1 = customer_list(['João', 'Maria', 'Jose', 'Marcos', 'Luan', 'Manoel'])
clientes2 = customer_list(['Alan', 'Eduardo', 'Yudi'], primeira_lista)
clientes3 = customer_list(['Jessica', 'Miguel'], ['John', 'Isabella'])

print(clientes1)
print(clientes2)
print(clientes3)
