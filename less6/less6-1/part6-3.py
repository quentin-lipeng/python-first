import copy
stuff = [[1, 2], {1, 2}, {1: 'a', 2: 'b'}, (1, 2), 'abc', 123]
stuff_deep = copy.deepcopy(stuff)
stuff_shallow = stuff.copy()

# 深拷贝中 第一层的可变类型地址会改变list set dic
i = 0
while i < len(stuff):
    print(type(stuff[i]), id(stuff[i]), '\t', stuff[i], 'origin')
    print(type(stuff_deep[i]), id(stuff_deep[i]), '\t', stuff_deep[i], 'deep')
    print(type(stuff_shallow[i]), id(stuff_shallow[i]), '\t', stuff_shallow[i], 'swallow')
    print()
    i += 1
