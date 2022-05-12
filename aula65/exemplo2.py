from time import time, sleep


def velocidade(function):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = function(*args, **kwargs)
        end_time = time()
        tempo = end_time - start_time
        print(f'a função "{function.__name__}" levou {tempo:.2f}s para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(11):
        print(i)
        sleep(1)


demora()
