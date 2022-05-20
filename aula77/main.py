# Associação — Python Orientado a Objetos

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Miguel')
caneta = Caneta('BIC')
maquina_de_escrever = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina_de_escrever.escrever()

print()

escritor.ferramenta = caneta
escritor.ferramenta.escrever(escritor.nome)

escritor.ferramenta = maquina_de_escrever
escritor.ferramenta.escrever(escritor.nome)
