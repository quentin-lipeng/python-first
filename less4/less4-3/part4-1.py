names = ['zhao', 'liu', 'song' 'shen']
print(names)
print(type(names))

li1 = [1, 2, 3]
li2 = [4, 5, 6]
print(li1 + li2)

print(li1 * 3)

print(names[1])

for n in names:
    print(n)

print(names[0::2])

li1, *li2 = [1, 2, 3, 4, 5, 6]
print(li1)
print(li2)

li1, *li2 = 'hello'
print(li1)
print(li2)

names.append('cang')
print(names)

names.insert(0,'huang')
print(names)

names1 = ['sd', 'das', 'rqw']
names.extend(names1)

del names[0]

names1[1] = 'sda'

names.sort()

names.sort(key=str.lower)
names.reverse()

name1 = sorted(names)
name1 = sorted(names, key=str.lower)
name1 = sorted(names, reverse=True)

print(names.index('liu'))
print(names.count('liu'))

li1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(li1[1][2])
