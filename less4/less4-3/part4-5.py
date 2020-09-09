u_info = {
    'name': 'as',
    'age': 21,
    'height': 16.1
}
print(u_info)

u_info.setdefault('name', 'dsa')

del u_info['name']
u_info1 = {
    'name': 'da',
    'age': 12,
    'height': 43.1
}
u_info.update(u_info1)
print(u_info)

print(u_info.keys())
print(u_info.values())
print(u_info.items())

for key in u_info:
    print(key)

for k, v in u_info1.items():
    print(k, v)

dic1 = dict({'name': 'das'})
dic2 = dict(name='das')
print(dic2)
