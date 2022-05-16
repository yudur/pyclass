# Classes - Python Orientado a Objetos

from pessoa import Pessoa

p1 = Pessoa('João', 32, 'masculino')
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('banana')
p1.parar_comer()
print()

p1.falar('hoje esta mais quente que o normal')
p1.parar_de_falar()
p1.parar_de_falar()
p1.falar('falei to leve!!!!')
p1.comer('queijo')
print()

p2 = Pessoa('Bia', 18, 'feminino')
p3 = Pessoa('Felipe', '23', 'masculino')

p2.falar('oi Felipe')
p3.falar('oi Bia')
print()

print(p1.ano_de_nacimento())
print(p2.ano_de_nacimento())
print(p3.ano_de_nacimento())
