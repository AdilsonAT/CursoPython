
a = 'aaa'
b = 'bbb'
c = 111.222
d = True

print('a', a, 'b', b, 'c', c, 'd', d)
print(f'a {a} b {b} c {c:.2f} d {d}')
print('a {} b {} c {:.2f} d {}'.format(a, b, c, d))
print('a {3} b {0} c {2:.2f} d {1}'.format(a, b, c, d))