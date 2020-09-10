def area():
    s = 3.14 * 3 ** 2
    print(s)


area()

print(id(area))
area1 = area
print(id(area1))
area1()


def xx():
    return i + 1


i = 5
a = xx
b = xx
print(a())
i = 7
print(a())
print(b())


def area(r):
    s1 = 3.14 * r ** 2
    print(s1)


area(2)
area(3)
area(4)


def area(r):
    s1 = 3.14  * r ** 2
    return s1


s = area(2)
print(s)


def area(r):
    s1 = r * 3.14 ** 2
    c = 2 * 3.14 * r
    return s1, c


ret = area(3)
print(ret)

s, c = area(3)
print(s, c)


def sum_2_num(n1, n2):
    total = n1 + n2
    print(total)
    

sum_2_num(20, 32)

sum_2_num(n1=12, n2=23)


def func(*args):
    print(args)
    
    
func(1, 2, 3)

tup = (1, 2, 6, 2)

func(*tup)


def func(**kwargs):
    print(kwargs)


dic = {'name': 'da', 'age': 21}

func(**dic)

func(name='dsa', age=21)


def doc():
    """:arg
    this is a doc"""
    pass


print(doc.__doc__)


def jiecheng(num):
    if num == 1:
        return 1
    ret = jiecheng(num - 1)
    return num * ret


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
        
search(4, 2, 6)