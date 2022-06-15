import sqlite3

conexao = sqlite3.connect("base_de_dados.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('maria', 80.55))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'José', 'peso': 39.33})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
               {'id': None, 'nome': 'José', 'peso': 39.33})
conexao.commit()

cursor.execute('UPDATE  clientes SET nome=:nome WHERE id=:id', {'nome': 'Marlon', 'id': 4})
conexao.commit()

cursor.execute('DELETE FROM clientes Where id=:id', {'id': 2})

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()
