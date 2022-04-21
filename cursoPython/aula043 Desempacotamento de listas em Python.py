
lista = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH']
a1, a2, *outra_lista, ultimo_lista = lista
print(a1, a2, outra_lista, ultimo_lista)
*outra_lista, a1, a2, ultimo_lista = lista
print(a1, a2, outra_lista, ultimo_lista)
a1, a2, *_ = lista
print(a1, a2)