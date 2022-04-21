
import aula088package.aula088a
print(aula088package.aula088a.aumento(50,10,True))
print(aula088package.aula088a.aumento(valor=50,percentagem=10,formata=True))


from aula088package import aula088a
print(aula088a.aumento(50,10))
print(aula088a.aumento(valor=50,percentagem=10))


from aula088package.aula088a import aumento, reducao
print(aumento(50,10))
print(aumento(valor=50,percentagem=10))