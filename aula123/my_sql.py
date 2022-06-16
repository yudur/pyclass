import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE
@contextmanager
def conect():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


# INSERI UM REGISTRO NA BASE DE DADOS
"""
with conect() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('Baki', 'Hamma', 19, 50))
        conexao.commit()
"""

# INSERI VÁRIOS REGISTROS NA BASE DE DADOS
"""
with conect() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        dados = [
            ('Muriel', 'Santos', 90, 76.44),
            ('José', 'Reis', 12, 30.63),
            ('Yudi', 'Duarte', 70, 60.20),
            ('Eliza', 'Santos', 45, 43.55)
        ]

        cursor.executemany(sql, dados)
        conexao.commit()
"""

# DELETA UM REGISTRO DA BASE DE DADOS
"""
with conect() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id=%s'
        cursor.execute(sql,(9,))
        cursor.execute(sql,(10,))
        cursor.execute(sql,(4,))
        conexao.commit()
"""

# ATUALIZA UM REGISTRO NA BASE DE DADOS
"""
with conect() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Mariana', 3))
        conexao.commit()
"""

# LISTA OS REGISTROS DA BASE DE DADOS
with conect() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
