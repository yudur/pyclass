"""
Metaclasses — Python Orientado a Objetos

EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é um Metaclasses (!!!???)
"""


class Meta(type):
    def __new__(mcs, nome, bases, namespace):
        if nome == 'A':
            return type.__new__(mcs, nome, bases, namespace)

        if not "b_fala" in namespace:
            print(f'você precisa criar o método "b_fala" em {nome} para não gerar bugs')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método não um atributo, crie isso em {nome}')

        if 'attr_classe' in namespace:
            del namespace['attr_classe']

        return type.__new__(mcs, nome, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'valor A'

    def fala(self):
        self.b_fala()


class B(A):
    attr_classe = 'valor B'

    def b_fala(self):
        pass

b = B()
print(b.attr_classe)

C = type('C', (), {'attr':'olá mundo!'})

print(C.attr)
