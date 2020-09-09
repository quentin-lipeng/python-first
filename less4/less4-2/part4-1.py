names = ['zhao', 'liu', 'song', 'shen']
print(names)
print(type(names))

li1 = [1, 2, 3]
li2 = [4, 5, 6]
print(li1 + li2)

li1 = ['Ni!']
print(li1 * 4)

print(names[1])
print(names[0::2])
for n in names:
    print(n)
li1, *li2 = ['a', 'b', 'c', 'd', 'e']
print(li1, li2)

li1, *li2 = 'hello'
print(li1, li2)

names.append('cang')
print(names)

names.insert(0, 'yan')
print(names)

names1 = ['wu', 'sha', 'zhu']
names1.extend(names)
print(names1)
print(names + names1)

del names1[0]
print(names1)

names.sort()
print(names)

names1.sort(key=str.lower)
print(names1)
names1.sort(reverse=True)
print(names1)
names1.reverse()
print(names1)

user_info = ['zhao', 34, False]
print(user_info[0])
li1 = [[1, 2, 4], [5, 6, 7], [8, 9, 0]]
print(li1[0][1])

st1 = 'hello'
print(id(st1))
st1 = 'new hello world'
print(id(st1))

li1 = [1, 2, 3]
print(id(li1))

li1.append(4)
print(id(li1))
li2 = li1
print(id(li2))
li2 = li1.copy()
print(id(li2))

import copy
# 地址也会改变 重新开辟一块内存空间
li2 = copy.deepcopy(li1)
print(id(li2))
