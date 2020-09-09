# 交集 &
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))

# 反交集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 子集
print(set1 < set2)
print(set1.issubset(set2))

# 超集
print(set1 > set2)
print(set1.issuperset(set2))

isinstance()