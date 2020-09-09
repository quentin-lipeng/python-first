li1 = [1, 2, 3]
li2 = li1.copy()

print(id(li1))
print(id(li2))
print(id(li1[0]))
print(id(li2[0]))

li1.append(4)
print(li1)
print(li2)

li1.remove(1)
print(li1)
print(li2)

li3 = [4, 5, li1]
print(li3)
print(li2)
print(id(li3[2]))
print(id(li1))

# 浅拷贝中如果 原对象第一层可变对象修改 新对象也随之修改 因为两元素同时指向同一地址
li1 = [3, 4]
li2 = [1, 2, li1]
li3 = li2.copy()
li2[2].append(5)
print(li2)
print(li3)
print((id(li2[2])))
print((id(li3[2])))
