def say_hello():
    """
    say hello
    """
    print('hello python')


# print(say_hello.__doc__)


def print_num(num):
    print(num)
    if num == 3:
        return
    num -= 1
    print_num(num)
    print('---->>>')
    

def jiecheng(num):
    if num == 1:
        return 1
    ret = jiecheng(num - 1)
    return num * ret


num = jiecheng(3)
print(num)


def search(num, start, end):
    if num == start:
        return start
    else:
        middle = (start + end) // 2
        if middle <= num:
            return search(num, middle, end)
        else:
            return search(num, start, middle)
        

search(67, 2, 100)
