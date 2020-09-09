tup = ('zs', 'ls', 'ww')
print(tup[0])
print(type(tup))

for t in tup:
    print(t)
tup1 = tup[1::-1]
print(tup1)

# 元组为有序序列
tp1 = (1, 2)
tp2 = (3, 4)
print(tp1 + tp2)
tp3 = 'Nil'
print(tp3 * 4)

mut_tup = (('a', 'b'), ('1', '2'), (1, 2, 3))
print(mut_tup[2][0])
name, age, gender = ('tom', 2, False)
print(name, age, gender)

name, age, gender = 'tom', 3, False
print(name, age, gender)
tup1, *tup2 = (1, 2, 3, 4)
print(tup1, tup2)

# tuple不允许修改
tup = ('张', '关', '曹', ['a', 'b'])
# tup[0] = '阿'  # 会报错
tup[3].append('c')
print(tup)

tup1 = (1,)
tup2 = (1)
print(type(tup1))
print(type(tup2))


