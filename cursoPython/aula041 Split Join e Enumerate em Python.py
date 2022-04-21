
string = "Doctor Who conta a historia de um sujeito que viaja no tempo e no espaço"
lista_1 = string.split(' ')
lista_2 = string.split(',')
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
lista_3 = ','.join(string)
print(lista_3)

for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])

lista_4 = [[1,2], [3,4], [5,6]]
print(lista_4)
for v in lista_4:
    print(v, v[0])
for v1, v2 in lista_4:
    print(v1,v2)