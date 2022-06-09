from threading import Thread
from threading import Lock
from time import sleep


class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('estoque insuficiente')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'você comprou {quantidade} de ingresso(s), '
              f'ainda temos {self.estoque} em estoque')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingresso(10)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    execultando = True
    while execultando:
        execultando = False

        for t in threads:
            if t.is_alive():
                execultando = True
                break

    print(ingressos.estoque)
