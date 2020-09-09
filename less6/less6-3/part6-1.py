li1 = [1, 2, 3]
li2 = li1.copy()
print(id(li1))
print(id(li2))
print(id(li1[0]))
print(id(li2[0]))

li1.remove(1)
print(li1)
print(li2)

li1 = [3, 4]
li2 = [1, 2, li1]
li3 = li2.copy()
print(li2)
print(li3)
print(id(li2[2]))
print(id(li3[2]))

li2[2].append(5)
print(li2)
print(li3)