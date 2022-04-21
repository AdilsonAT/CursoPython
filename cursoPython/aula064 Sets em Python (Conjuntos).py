
s1 = {1,2,3,4,5,6}
print(s1)
for v in s1:
    print(v)

s1.add(7)
s1.discard(3)
print(s1)
s1.update('Python')
print(s1)
l1 = [1,1,1,2,2,3,3,3,3,4,4,5,6,7,8,8,'Doctor','Doctor','Doctor Who']
s2 = set(l1)
print(s2)
l1 = list(s2)

s3 = {1,2,3,4,5,7}
s4 = {1,2,3,4,5,6}
print(s3 | s4)
print(s3 & s4)
print(s3 - s4)
print(s4 - s3)
print(s3 ^ s4)