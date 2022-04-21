from aula080Map import produtos, pessoas, lista

from functools import reduce    # <==============

acumula = 0
for item in lista:
    acumula += item
print (acumula)

soma_lista = reduce(lambda ac, i: i+ac, lista, 0) #
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco']+ac, produtos, 0)
print(soma_precos)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, i: i['idade']+ac, pessoas, 0)
print(soma_idades, soma_idades / len(pessoas))