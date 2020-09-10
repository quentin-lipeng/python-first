def area():
    s = 3.14 * 3 ** 2
    print(s)


# area()

print(id(area()))
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
print(id(a))
print(id(b))


def area(r):
    s1 = 3.14 * r ** 2
    print(s1)


area(2)
area(3)
area(4)


def area(r):
    s1 = 3.14 * r ** 2
    return s1


s = area(2)
print(s)


def area(r):
    s1 = 3.14 * r ** 2
    c = 2 * 3 * r
    return s1, c


s, c = area(3)
print(s, c)
