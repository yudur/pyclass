import json

dictionary = {
    'Pessoa 1': {
        'nome': 'Yudi',
        'idade': 13
    },
    'Pessoa 2': {
        'nome': 'Alan',
        'idade': 24
    },
}

dictionary_jason = json.dumps(dictionary, indent=True)

with open('js.json', 'w+') as file:
    file.write(dictionary_jason)
