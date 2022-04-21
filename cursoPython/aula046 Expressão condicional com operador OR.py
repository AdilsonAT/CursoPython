
nome = input('Qual nome? ')
print(nome or 'Nada digitado!')
print(nome or Nome or False or 0 or 'Nada digitado!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'xpto'
variavel = a or b or c or d or e or f or g
print (variavel)