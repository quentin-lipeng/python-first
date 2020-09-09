dic = {'a': 10, 'b': 11}
new_dic = {}
for k, v in dic.items():
    new_dic[v] = k
print(new_dic)

new_dic = {v: k for k, v in dic.items()}
print(new_dic)

l = [1, 2, 3, 4, 5]
set = {i for i in l}
print(set)