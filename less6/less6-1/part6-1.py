# 列表内存储的是元素地址
li1 = [1, 2, 3, 4]
print(id(li1))

li1.append(5)
print(id(li1))

li1 = [1, 2, 3, 4]
print(id(li1))

li1[0] = 0
print(id(li1))

li1 = list([1, 2, 3, 4])
print(id(li1))
# 只要不重新赋值(修改不会修改地址) list的地址就不会改变

print('-------')
# 浅拷贝第一层会创建新地址 第二层开始都不会 保持原来
li2 = li1.copy()
print(id(li1))
print(id(li2))
print(id(li1[0]))
print(id(li2[0]))

li1.append(5)
print(li1)
print(li2)

li1.remove(1)
print(li1)
print(li2)

li3 = [1, 2, li1]
li4 = li3.copy()
print(id(li3[2]))
print(id(li4[2]))
print(li3)
print(li4)