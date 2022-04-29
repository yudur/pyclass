customers = {

    'client 1': {

        'nome': 'Joana',
        'sobrenome': 'Silva'
    },

    'client 2': {

        'nome': 'Mario',
        'sobrenome': 'Andrade'
    },

    'client 3': {

        'nome': 'Yudi',
        'sobrenome': 'Duarte'
    },

    'client 4': {

        'nome': 'Icaro',
        'sobrenome': 'Dantas'
    },

    'client 5': {

        'nome': 'Maria',
        'sobrenome': 'Braga'
    }
}

print('–––––––––––––customer data–––––––––––––')

for client_k, client_v in customers.items():
    print(f'customer {client_k}')

    for client_data_k, client_data_v in client_v.items():
        print(f'{client_data_k}: {client_data_v}')

    print()

print('–––––––––––––––––––––––––––––––––––––––')
