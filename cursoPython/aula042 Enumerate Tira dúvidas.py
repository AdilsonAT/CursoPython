
lista = [['aa', 'bb', 'cc'], ['dd', 'ee', 'ff'], ['gg', 'hh', 'ii']]
print(lista)
print(lista[1][2])
enumerada = list(enumerate(lista))
print(enumerada)
print(enumerada[1])
print(enumerada[1][1])
print(enumerada[1][1][2])

for v1, v2 in enumerada:
    print(v1, v2)
for v1, v2 in enumerate(lista, 53):
    print(v1, v2)
for v1 in enumerada:
    print(v1)
    valor_enumerado, minha_lista = v1
    cel_1, cel_2, cel_3 = minha_lista
    print(cel_1, cel_2, cel_3)

"""
[ <--- enumerate

    tuplas
    0   1
    (0, ['aa', 'bb', 'cc'])
    (1, ['dd', 'ee', 'ff'])
    (2, ['gg', 'hh', 'ii'])
]
"""