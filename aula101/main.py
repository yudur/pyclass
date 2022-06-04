"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets),
base de dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)]


with open('cliente2.csv', 'w') as file:
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
