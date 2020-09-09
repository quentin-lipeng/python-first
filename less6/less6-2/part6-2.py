import copy

n_l = ['tom', 'dsad', ['hgd', ['qwe']]]
n_l1 = copy.deepcopy(n_l)

n_l[2][0] = 'hpou'
print(n_l)
print(n_l1)

print(id(n_l[2]))
print(id(n_l1[2]))

print(id(n_l[2][1]))
print(id(n_l1[2][1]))

# 深拷贝可变类型对象的元素修改 不会影响新元素
n_l[2][1].append('2')
print(n_l[2][1])
print(n_l1[2][1])
