"""
Levantando exceções em Python (raise)
https://docs.python.org/3/library/exceptions.html
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro)
        raise


try:
    print(divide(10, 0))
except:
    print('erro')
