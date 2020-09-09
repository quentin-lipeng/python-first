import copy

n_l = ['tom', 'dsad', ['dsad']]
n_l1 = copy.deepcopy(n_l)
n_l[2][0] = 'dsadwq'
print(n_l)
print(n_l1)
print(id(n_l[2]))
print(id(n_l1[2]))

n_l2 = [3, 4, n_l]
n_l3 = copy.deepcopy(n_l2)
n_l2.append(12)
print(n_l2)
print(n_l3)
