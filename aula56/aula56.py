"""
Try, Except — Tratando exceções em python
"""

try:
    a = []
except NameError as erro:
    print('erro:', erro)
except Exception as erro:
    print('erro inesperado', erro)
else:
    print(a)
finally:
    print('finalmente 😁😁😁')
