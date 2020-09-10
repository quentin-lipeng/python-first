def area():
    s = 3.14 * 3 ** 2
    print(s)


area()


print(id(area))
area1 = area
print(id(area1))
area1()


def area(r):
    s1 = 3.14 * r ** 2
    print(s1)


area(2)


def area(r):
    s = 3.14 * r ** 2
    return s


def area(r):
    s = 3.14 * r ** 2
    c = 2 * 3.14 * r
    return s, c


ret = area(3)
print(ret)

s, c = area(3)
print(s, c)


def sum_2_num(n1, n2):
    print(n1 + n2)


sum_2_num(2, 3)

sum_2_num(n1=1, n2=23)


def func(*args):
    print(args)


func(1, 2, 3, 4)

tup = (1, 2, 3, 6)

func(*tup)


def func(**kwargs):
    print(kwargs)


func(name='dsa', age=21)


dic = {'name': 'das', 'age': 21}

func(**dic)


def doc():
    """:arg
    this is doc"""
    pass


print(doc.__doc__)


def jiecheng(n):
    if n == 1:
        return 1
    ret = jiecheng(n - 1)

    return n * ret


num = jiecheng(3)
print(num)


def search(n, s, e):
    if n == s:
        return s
    else:
        m = (s + e) // 2
        if m <= n:
            return search(n, m, e)
        else:
            return search(n, s, m)


search(3, 1, 39)
