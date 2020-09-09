# num = float(input('press five number'))

num = 123.45
# if 100 <= num <= 1000:
#     n1 = int(num % 10)
#     n2 = int(num % 100 // 10)
#     n3 = int(num // 100)
#
#     n4 = num * 100 % 100
#     n5 = int(n4 // 10)
#     n6 = int(n4 % 10)
#
#     print(n6, n5, n1, n2, n3)
#
#
# pass


n = int(num * 100)
n1 = n % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
n5 = n // 10000
print(n1, n2, n3, n4, n5)