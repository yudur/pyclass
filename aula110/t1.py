"""
Threads - Executando processamentos em paralelo
"""
from threading import Thread
from time import sleep


class MeuThread(Thread):
    def __init__(self, tempo, texto):
        self.tempo = tempo
        self.texto = texto

        Thread.__init__(self)

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread(5, 'Thread 1')
t1.start()

t2 = MeuThread(10, 'Thread 2')
t2.start()

t3 = MeuThread(15, 'Thread 3')
t3.start()
for i in range(20):
    print(i)
    sleep(1)
