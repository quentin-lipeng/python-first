user_info = {
    'name': '于谦',
    'age': 50,
    'hobby': ['抽', '喝', '烫']
}
print(user_info)
print(type(user_info))
# 字典的key 不能是可修改数据类型

user_info['height'] = 1.8
print(user_info)
user_info.setdefault('weight', 50)
print(user_info)

del user_info['name']
print(user_info)
# del user_info
# print(user_info)

user_info1 = {
    'name': '🐟哥',
    'age': 18
}
user_info.update(user_info1)
print(user_info)

print(user_info.keys())
print(user_info.values())
print(user_info.items())
print(len(user_info))

for key in user_info:
    print(key)
for key in user_info.keys():
    print(key)
for value in user_info.values():
    print(value)
for key, value in user_info.items():
    print(key, value)
