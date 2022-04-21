
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l2 + l1
print(l1)
print(l2)
print(l3)
l2.insert(0, 'banana')
l2.pop(2)
print(l2)

l4 = [1,2,3,4,5,6,7,8,9]
print(max(l4))
print(list(range(1,10)))
print(list(range(1,100,8)))

l5 = ['String', True, 10, -20.5]
for elem in l5:
    print(f'O tipo de {elem} é {type(elem)}')
