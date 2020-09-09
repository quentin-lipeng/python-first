name_list = ['tom', 'jerry', 'marry']
name_list.append('mike')
print(name_list)

name_list.insert(0, 'a')
name_list.insert(-2, 'b')

name_list1 = ['wu', 'ba', 'tom']
name_list.extend(name_list1)
print(name_list)

name_list2 = name_list + name_list1
print(name_list2)

del name_list2[0]
print('del', name_list2)

name_list[0] = 'aaa'
print(name_list)
name_list.sort()
print(name_list)

name_list.sort(key=str.lower)
print(name_list)

name_list.sort(reverse=True)
print(name_list)

name_list3 = sorted(name_list)
print(name_list3)
name_list.insert(2, 'AAA')
name_list3 = sorted(name_list, key=str.lower)
print(name_list3)
name_list3 = sorted(name_list,reverse=True)
print(name_list3)
