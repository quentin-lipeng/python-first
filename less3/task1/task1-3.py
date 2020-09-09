# i = 0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print(f'{j}*{i}={j*i}', end='\t')
#     print()

num = int(input('press a number!'))
i = 2
while num > i:
    if num % i == 0:
        print(f'{num} is not a prime number')
        break
    i += 1
else:
    print(f'{num} is a prime number')


# in_number = int(input('press a number'))
#
# i = 0
# while in_number > 0:
#     i = in_number % 10 + i * 10
#     in_number //= 10
# print(i)
