
from itertools import combinations, permutations, product
pessoas = ['Pessoa01', 'Pessoa02', 'Pessoa03','Pessoa04', 'Pessoa05', 'Pessoa06']

for grupo in combinations(pessoas, 2):
    print(grupo)

print('='*20)

for grupo in permutations(pessoas, 2):
    print(grupo)

print('='*20)

for grupo in product(pessoas, repeat=2):
    print(grupo)
