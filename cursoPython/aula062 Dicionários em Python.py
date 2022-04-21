
import copy

d1 = {'chave': 'valor da chave'}
d1['nova chave'] = 'Valor da nova chave'
print(d1)

d2 = dict(chave1='Valor da chave1', chave2='Valor da chave2')
d2['nova chave'] = 'Valor da nova chave'
print(d2)
print(d2['chave1'])

d3 = {'chave': 'valor1', 'chave': 'valor2', 'chave': 'valor3'}
print(d3)

d4 = {'str': 'str', 123: 'int', (1,2,3): 'tupla'}
print(d4)
print(d4[(1,2,3)])
if 'naoexiste' in d4:
    print('chave não existe')
print(d4.get('naoexiste'))

del d4['str']
print(d4)
print('str' in d4, 'str' in d4.keys(), 'int' in d4.values())
print(len(d4))

clientes = {'cliente1': {'nome': 'Doctor Who', 'sobrenome': 'Nine'},
            'cliente2': {'nome': 'Doctor Who', 'sobrenome': 'Ten'}}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d5 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Doctor', 'Who']}
v = copy.deepcopy(d5)
print(d5)
v[1] = 'War'
print(v)
print(v['d'][0])