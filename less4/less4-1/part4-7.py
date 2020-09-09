s1 = 'hello'
tup = tuple(s1)
print(tup)

li1 = [1, 2, 3, 4]
tp1 = tuple(li1)
print(tp1)

tp2 = (1, 2, 3)
print(tuple(tp2))

print(tp2.index(1))
print(tp2.count(1))

for name in ('tom', 'a', 'das'):
    print(name)
print(tp1[1::-1])
print(tp1 * 3)

user_info = (('zs', 10), ('ls', 11), ('ww', 12))
for name, age in user_info:
    print(name, age)

for n in enumerate(tp2):
    print(n)

msg = 'my name is %s, age is %d' % ('zs', 18)
print(msg)


def func():
    name = 'sa'
    age = 10
    return name, age


ret = func()
print(type(ret))

b = (1, 2, 3, 4, 5, 6, 7)
he = 0
i = 0
while i < len(b):
    he += b[i]
    i += 1
print(he)
