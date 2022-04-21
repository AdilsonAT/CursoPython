
a = lambda x, y: x * y

print(a(2,2))

lista =[ ['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8] ]
def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)
lista.sort(key=lambda item: item[1])
print(lista)
print(sorted(lista, key=lambda item: item[0], reverse=True))