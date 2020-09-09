print('string')
print("string")


def n_p():
    name = input('username: ')
    password = input('password: ')
    print(name, password)
    pass


def people():
    name = str('lee')
    age = int(input("age: "))
    gender = str(input('gender'))
    height = float(input('height'))
    print(name, type(name))
    print(age, type(age))
    print(gender, type(gender))
    print(height, type(height))
    pass


# 改变引用
v2 = 'a'
print(v2, id(v2))
v2 = 3
print(v2, id(v2))

# 共享引用
num = 1
num1 = num
print(num, id(num))
print(num1, id(num1))
