st1 = 'hello world'
print(id(st1))
st1 = 'new hello world'
print(id(st1))

li1 = [1, 2, 3]
print(id(li1))

li1.append(4)
print(id(li1))

li1 = [4, 5, 6]
print(id(li1))

li2 = li1.copy()

import copy
names = ['tom', 'jetty', 'cat']
names1 = copy.deepcopy(names)

