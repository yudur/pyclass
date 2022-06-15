import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Marlon', '11111-1111')
    # agenda.inserir('Rosa', '22222-2222')
    agenda.inserir('Fabricio', '33333-3333')
    # agenda.inserir('Gabriel', '44444-4444')
    agenda.inserir('Esmeralda', '55555-5555')
    # agenda.inserir('Jessica', '66666-6666')
    agenda.inserir('Luiz', '10101-1111')
    agenda.inserir('Luiz Otávio', '01234-2312')
    agenda.inserir('Luiza', '23454-1234')
    agenda.inserir('M. Luiz', '58205-7929')
    agenda.inserir('Luizinho', '54912-0401')



    agenda.editar('Francisco', '99999-9999', 19)

    # agenda.excluir(17)
    # agenda.excluir(21)
    # agenda.excluir(78)

    agenda.buscar('luiz')
