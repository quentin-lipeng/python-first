names = ['zhao', 'liu', 'lee', 'shen']
print(names)
print(type(names))

li1 = [1, 2, 3]
li2 = [4, 5, 6]
li3 = li1 + li2
print(li3)

li4 = li1 * 4
print(li4)

name = names[1]
print(name)

for name in names:
    print(name)
name = names[0::2]
print(name)

li5, li6 = ['a', 'b']
print(li5)
print(li6)

li7, *li8 = [1, 2, 3, 4, 5]
print(li7)
print(li8)

*li9, li10 = [1, 2, 3, 4, 5]
print(li9)
print(li10)