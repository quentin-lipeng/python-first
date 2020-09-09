# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j} * {i} = {j * i}', end='\t')
#     print()

i = int(input('press a number :'))
init = 2
while init < i:
    if i % init == 0:
        print('不为质数')
        break
    init += 1
else:
    print('为质数')

num = int(input('press a number'))
num1 = 0
while num > 0:
    num1 = num1 * 10 + num % 10
    num //= 10
print(num1)
