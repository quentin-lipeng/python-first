user_info = {
    'name': 'lee',
    'age': 15,
    'hobby': ['chou', 'xi', 'he']
}

print(user_info)
print(type(user_info))
print(user_info['name'])
user_info.setdefault('name', 'liu')
del user_info['name']
user_info1 = {
    'name': 'wong',
    'age': 27
}
user_info.update(user_info1)
print(user_info.keys())
print(user_info.values())
print(user_info.items())
dic1 = dict()
print(dic1)
print(dict(user_info1))
print(dict([('name', 'lee'), ('age', 19)]))
