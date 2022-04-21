from aula080Map  import produtos, pessoas, lista

nova_lista = filter(lambda x: x>5, lista)
print(nova_lista)   # retorna um iterator
print(list(nova_lista))

nova_lista_2 = [x for x in lista if x > 5]
print(nova_lista_2)

nova_lista_3 = filter(lambda p: p['preco'] > 50, produtos)  # precos maiores que 10 da lista retornando preco
print (nova_lista_3)    # iterator
for produto in nova_lista_3:
    print(produto)

def filtra(produto):
    if produto['preco'] > 50:
       produto['e_caro'] = True
    return True

nova_lista_4 = filter(filtra, produtos)
for produto in nova_lista_4:
    print(produto)







