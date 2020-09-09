tup = ('sa', 'ffa', 'dsa')
print(tup[1])

for t in tup:
    print(t)

tup1 = (1, 2)
tup2 = (4, 5)
print(tup1 + tup2)
print(tup1 * 3)

tup3 = ((1, 2), (3, 5))
print(tup3[1][1])
name, age, gender = ('tom', 2, True)

tup1, *tup2 = (1, 2, 4, 5)

tup = (1,)
print(type(tup))
tup1 = tuple((1, 2, 3))
print('tup1', tup1)

print(tup1.index(2))
print(tup.count(1))

print('--------------')
tup4 = ((1, 3, 4), (2, 3, 5), (12, 32, 54))

for t1 in tup4:
    for t in t1:
        print(t)


def fun():
    name = 'sa'
    age = 21
    return name, age


print(fun())

