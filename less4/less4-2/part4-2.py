tup = ('a', 'b', 'c')
print(tup[1])

for i in tup:
    print(i)

print(tup[1::-1])
tup1 = ('d', 'e', 'f')
print(tup + tup1)

mul_tup = (('wu', 'sun', 'le'), ('liu', 'wang'),('a', 'b', 'c'))
print(mul_tup[2][0])
name, age, gender = ('lee', 21, False)
print(name, age, gender)
tup1, *tup2 = (1, 2, 3, 4)
print(tup1, tup2)
# 元组不可修改 可内置数组

s1 = 'hello'
tup1 = tuple(s1)
print(tup1)
li1 = [1, 2, 3, 4]
print(tuple(li1))
print(tup1.index('e'))
print(tup1.count('l'))

for i in tup1:
    print(i)
user_info = (('n', 1), ('s', 2), ('f', 3))
for f, l in user_info:
    print(f, l)

s = 'i am %s %s' % ('lee', 'qun')
print(s)
