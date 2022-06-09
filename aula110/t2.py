from threading import Thread
from time import sleep


def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


tf1 = Thread(target=vai_demorar, args=(5, 'thread com função'))
tf1.start()

while tf1.is_alive():
    print('esperando a thread')
    sleep(1)

print('thread acabou')
