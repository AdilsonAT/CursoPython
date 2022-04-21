"""
Formatando valores com modificadores

:s - texto (strings)
:d - inteiros
:f - ponto flutuante
:.(numero)f - casas decimais
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d, f)
> esquerda < direita ^ centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_1 = 1
print(f'{num_1:0>10}')
num_1 = 1234
print(f'{num_1:0^10}')
print(f'{num_1:0>10.2f}')
nome = 'Doctor Who'
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
nome_formatado = '{n} é um {n:-^30}'.format(n=nome)
print(nome_formatado)
nome_formatado = '{1}'.format('Doctor', 'Who')
print(nome_formatado)
