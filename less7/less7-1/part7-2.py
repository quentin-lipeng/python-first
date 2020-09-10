def sum_2_num(num1, num2):
    total = num1 + num2
    print(total)


sum_2_num(20, 31)

sum_2_num(num1=10, num2=213)


def func(*args):
    print(args)
    print(args[0], args[1])


func(1, 2, 3, 4)

tup = (1, 2, 3)
func(*tup)


def func(**kwargs):
    print(kwargs)


func(name='as', age=13)


def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, name='1da', age=123)



