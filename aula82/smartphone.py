from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'O {self._nome} está desligado'
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f'O {self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return

        info = f'O {self._nome} foi conectado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'O {self._nome} já está desconectado'
            print(error)
            self.log_error(error)
            return

        info = f'O {self._nome} foi desconectado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False
