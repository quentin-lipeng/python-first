import keyword

''' ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 
'''
# print(keyword.kwlist)

# print(eval('10+2'))  # 12

# input('press')

b = 10 | False
# print(b)  #10

num = 8

# print(20 // num)  # 取整数 2

# print(3 < num < 20)  # 比较num是不是在3和20之间


def if_elif():
    if num > 3:
        print('true')
    elif num == 1:
        print("equals 1 ")
    else:
        print('false')
    pass


def while_else():
    num1 = 3
    while num1 < 6:
        print(num1)
        num1 += 1
    else:
        print('over')
    pass


def row():
    i = 1
    while i < 10:
        i += 1
        j = 10
        while i < j:
            j -= 1
            print(i, ' ', end='')
        print('')
    pass


def for_each():
    i = [5, 4, 3, 2, 1]
    for number in i:
        print(number)
    pass


def for_range():
    for number in range(0, 20, 4):
        print(number)
    pass


for_range()


list1 = [1, 2, 3]

# print('we have {} and {}'.format(list1, 2))
