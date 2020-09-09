sets = {1, 2, 3, 4, 5}
print(sets)
print(type(set))

sets = set([1, 2, 3, 4, 5])
print(sets)

sets = set('hello')
print(sets)
sets = set({'name': 'zs', 'age': 12})
print(sets)

sets.add('hei')
print(sets)
sets.update({'xixi','hh'})
print(sets)

sets.pop()
print(sets)
sets.remove('hh')
print(sets)
sets.clear()
print(sets)
# del sets
# print(sets)
