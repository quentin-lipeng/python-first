import copy
name_list = ['tom', 'jetty', ['wu', 'ba']]
name_list1 = copy.deepcopy(name_list)

name_list1[2][0] = 'hou'
print(id(name_list))
print(id(name_list1))

name_list1[2].append(5)
print(name_list)
print(name_list1)
