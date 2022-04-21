
l1 = [1,2,3,4,5]
l2 = [v*2 for v in l1]
print(l2)

lista = [('chave', 'valor'), ('chave2', 'valor2'),]
d1 = {x: y for x, y in lista}
print(d1)
d1 = {x: y*2 for x, y in lista}
print(d1)
d1={x: y for x, y in enumerate(range(5))}
print(d1)
d1 = {x for x in range(5)}
print(d1, type(d1))
d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))