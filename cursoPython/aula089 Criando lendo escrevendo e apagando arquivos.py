# https://docs.python.org/3/library/functions.html#open

file = open('abc.txt', 'w+')    # leitura e escrita
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())
print('-------------------------------------------------------------------------------------------')

file.seek(0, 0)
print(file.readline())
print(file.readline())
print('-------------------------------------------------------------------------------------------')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print('-------------------------------------------------------------------------------------------')

file.seek(0, 0)
print(file.readlines())
print('-------------------------------------------------------------------------------------------')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()

print('===========================================================================================')

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0, 0)
    print(file.read())

with open('abc.txt', 'r') as file:
    print(file.read())

with open('abc.txt', 'a+') as file:
    file.write('Linha 4\n')
    file.write('Linha 5\n')
    file.write('Linha 6\n')
    file.seek(0, 0)
    print(file.read())

import os
os.remove('abc.txt')

print('===========================================================================================')

import json
d1 = {
    'Pessoa 1': {
        'nome': 'Doctor Who',
        'idade': 35,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 20,
    },
}
print(d1)
d1_json = json.dumps(d1)
print(d1_json)
d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

import json
with open('abc.json', 'r') as file:
    d1_json = file.read()
    print(d1_json)
    d1_json = json.loads(d1_json)
    print(d1_json)
for k, v in d1_json.items():
    print(k, v)
for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)