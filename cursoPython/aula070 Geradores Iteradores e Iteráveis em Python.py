
lista = (1,2,3,4,5)
print(hasattr(lista, '__iter__'))
lista = 123
print(hasattr(lista, '__iter__'))
lista = ('String')
print(hasattr(lista, '__iter__'))

lista = [1,2,3,4,5]
print(hasattr(lista, '__next__'))
lista = iter(lista)
print(hasattr(lista, '__next__'))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print('===============================================================================================')
import sys
import time

lista = list(range(100))
print(sys.getsizeof(lista))

def gera():
    r = []
    for n in range(100):
        r.append(n)
    return r

g = gera()
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
for v in g:
    print(v)

def gera():
    r = []
    for n in range(100):
        yield n
    return r

g = gera()
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
for v in g:
    print(v)

def gera():
    variavel = 'Valor1'
    yield variavel
    variavel = 'Valor2'
    yield variavel
    variavel = 'Valor3'
    yield variavel

g = gera()
for v in g:
    print(v)

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))
print(type(l1))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))