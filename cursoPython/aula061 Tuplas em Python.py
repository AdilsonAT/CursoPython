
t1 = (1,2,3,'a','b')
print(type(t1))
t2 = 1,2,3,'a','b'
print(type(t2))
t3 = 1
print(type(t3))
t4 = 1,
print(type(t4))
t5 = t1 + t2
print(type(t5))
n1, n2, n3, *_, n10 = t5
t6 = (1,2,3,'a','b')  * 10
l1 = list(t1)