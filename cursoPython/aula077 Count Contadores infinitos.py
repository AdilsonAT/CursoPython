
from types import GeneratorType
variavel = zip('Alo', 'Alo')
print(variavel)
print(isinstance(variavel, GeneratorType))
variavel = ((x,y) for x,y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))

from itertools import count

contador = count(start=5, step=2)      # contador é um iterador
print(next(contador))
print(next(contador))

for valor in contador:
    print(valor)
    if valor >= 10:
        break

contador = count()
lista = ['item1', 'item2', 'item3', 'item4']
lista = zip(contador, lista)
print(list(lista))


