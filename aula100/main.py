"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs
"""
from dados import *
import json

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)
print(type(dados_json))

dicionario = json.loads(clientes_json)
print(dicionario)

with open('clientes.json', 'w') as clientes:
    json.dump(clientes_dicionario, clientes, indent=4)

with open('clientes.json', 'r') as clientes:
    dados = json.load(clientes)

print()
for key, value in dados.items():
    print(key)
    print(value)
