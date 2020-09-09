import copy

n_l = [{'tom'}, 'dsa', ['gd', 'dqe']]
n_l1 = copy.deepcopy(n_l)

n_l1[2][0] = '水水水'
print(n_l)
print(n_l1)
# 深拷贝第一层为新地址 从第二层开始
print(id(n_l[2][0]))
print(id(n_l1[2][0]))

print('-----deep copy----')
print(id(n_l[0]))  # 1342644181480
print(id(n_l1[0]))  # 1342644375624
print(id(n_l[1]))  # 1342641573424
print(id(n_l1[1]))  # 1342641573424

print('------shallow copy------')
n_l2 = n_l.copy()
print(id(n_l[0]))  # 1342644181480
print(id(n_l2[0]))  # 1342644181480
print(id(n_l[1]))  # 1342641573424
print(id(n_l2[1]))  # 1342641573424
