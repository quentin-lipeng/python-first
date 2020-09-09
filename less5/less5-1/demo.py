i = [i ** 3 for i in range(10)]
print(i)


def fun(a=10):
    return a
    pass


print(fun(a=9))


def fun1(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    pass


fun1()


def fun2(a, b, c):
    print(a + b + c)
    pass

i.cop


li = [1, 2, 3]
fun2(*li)
