dic = {
    'a': 19,
    'b': 11
}
new_dic = {}
for key, value in dic.items():
    new_dic[value] = key
print(new_dic)

dic = {
    'a': 10,
    'b': 11
}
new_dic = {value: key for key,value in dic.items()}
print(new_dic)
dic = {k: v for k, v in zip(list('ABC'), list('123'))}
print(dic)

l1 = [1, 2, 3, 4, 5, 3, 1, 2, 3]
set1 = {i for i in l1}
print(set1)