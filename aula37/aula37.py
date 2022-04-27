"""
Expressões lambda (funções anônimas) em python
"""


def function(fun1, fun2):
    return fun1 * fun2


var = function(5, 4)
print(var)

anonymous_function = lambda x, y: x * y
print(anonymous_function(8, 8))
