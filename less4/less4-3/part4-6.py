set1 = {1, 2, 3, 4}
print(type(set1))
set1.add('sas')
set1.update({'dsad', 'dasd'})
print(set1)

set1.remove('dsad')
# set1.clear()
for s in set1:
    print(s)

set1 = {1, 2, 3, 4, 5}
set2 = {1, 6, 7, 3, 2, 8}

print(set1 & set2)
print(set1.intersection(set2))

print(set1 | set2)
print(set1.union(set2))

print(set1 - set2)
print(set1.difference(set2))

print(set1 > set2)
print(set1.issubset(set2))

print(set1 < set2)
print(set1.issuperset(set2))