set1 = {1, 2, 3, 4, 5}
print(set1)
print(set([1, 2, 3, 4, 5]))

print(set({
    'name': 'lee', 'age': 14
}))
set1.add('heihei')
set1.update({'name': 'qun'})
set1.pop()
set1.remove('name')
set1.clear()

del set1

set1 = {1, 2,3, 4}
set2 = {6, 7, 8, 9}
print(set1 & set2)
print(set1.intersection(set2))

print(set1 | set2)
print(set1.union(set2))

print(set1 - set2)
print(set1.difference(set2))

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

print(set1 < set2)
print(set1.issubset(set2))

print(set1 > set2)
print(set1.issuperset(set2))
