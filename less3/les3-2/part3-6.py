s = ''


# print(dir(s))
# print(help(s.split))

def a():
    print('a')
    return True


def b():
    print('b')
    return True


def c():
    print('c')
    return True


def d():
    print('d')
    return False


print(a() or b() or c())
