
produtos = [
    {'nome': 'p01', 'preco': 13},
    {'nome': 'p02', 'preco': 55.55},
    {'nome': 'p03', 'preco': 5.59},
    {'nome': 'p04', 'preco': 22},
    {'nome': 'p05', 'preco': 81.23},
    {'nome': 'p06', 'preco': 5.7},
    {'nome': 'p07', 'preco': 10.90},
    {'nome': 'p08', 'preco': 89.82},
    {'nome': 'p09', 'preco': 12},
    {'nome': 'p10', 'preco': 2.90}
]

pessoas = [
    {'nome': 'War Doctor', 'idade': 60},
    {'nome': 'Doctor Who Nine', 'idade': 35},
    {'nome': 'Doctor Who Ten', 'idade': 30},
    {'nome': 'Doctor Who Eleven', 'idade': 25},
    {'nome': 'Doctor Who Twelve', 'idade': 60},
    {'nome': 'Doctor Who Thirteen', 'idade': 25},
    {'nome': 'River Song', 'idade': 35},
    {'nome': 'Rose Tyler', 'idade': 20},
    {'nome': 'Amy Pond', 'idade': 20},
    {'nome': 'Dona Noble', 'idade': 30}
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from aula080Map import produtos, pessoas, lista

"""""
nova_lista = map(lambda x: x*2, lista)
print(list(nova_lista))
nova_lista = [x*2 for x in lista]
print(list(nova_lista))

for produto in produtos:
    print(produto)
"""""
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

for pessoa in pessoas:
    print(pessoa)

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)
nomes = map(lambda p: p['idade'], pessoas)
for pessoa in nomes:
    print(pessoa)
