print(bool(0))
print(bool(''))
print(bool())
print(bool({}))
print(bool(None))

print(bool(1))
print(bool('a'))
print(bool([1, 2]))
print(bool((1, 2)))

print(4 ** 2)

print(12 % 2)


def reverse():
    a = int(input('press three number : '))
    b = 1 % 10
    c = a // 10 % 10
    d = a // 100 % 10
    f = b * 100 + c * 10 + d
    print(f)
    pass


print(2 ** 3)  # 8


print('------')
num1 = 1
num1 += 2
print(num1)
num1 -= 2
print(num1)
num1 *= 4
print(num1)
num1 /= 2
print(num1)
num1 %= 2
print(num1)
