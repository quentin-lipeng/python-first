name_list = ['tom', 'jetty', 'tom']
name = name_list[0]
print(name)
index = name_list.index('jetty')
print(index)
num = name_list.count('tom')
print(num)

li1 = ['aaa', 23, True]
print(li1)
li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(li2[1][0])

# bool、int、float、str、set、list、tuple、dict
st1 = 'hello world'
print(id(st1))

st1 = 'new hello world'
print(id(st1))

print(id(li1))
li1.append(4)
print(id(li1))

li3 = [1, 2, 3]
print(id(li3))
li3 = [4, 5, 6]
print(id(li3))
