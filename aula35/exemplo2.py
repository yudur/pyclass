variavel = 'valor'


def func():
    print(variavel)


def fun2():
    global variavel
    variavel = 'outro valor'
    print(variavel)


func()
fun2()

print(variavel)
