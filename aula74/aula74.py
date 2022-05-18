class A:
    n = 12345

    def __init__(self):
        self.n = 54321

a1 = A()
a2 = A()

a1.n = 54321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
print()

print(a1.n)
print(a2.n)
print(A.n)
