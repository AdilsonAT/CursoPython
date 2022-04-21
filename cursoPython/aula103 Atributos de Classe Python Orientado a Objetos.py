
class A:
    vc = 123    #Variavel de classe

    def __init__(self):
        self.vc = 456

a1 = A()
a2 = A()
print(a1.vc)
print(a2.vc)
print(A.vc)

a1.vc = 321
print(a1.vc)
print(a2.vc)
print(A.vc)
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
