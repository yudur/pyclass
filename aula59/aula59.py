# Módulos padrão do python:
# Módulos são arquivos .py (que contém código python) e serve para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do python em:
# https://docs.python.org/3/py-modindex.html

from sys import getsizeof, platform

print(platform)

x = [v for v in range(1000)]
print(getsizeof(x))
