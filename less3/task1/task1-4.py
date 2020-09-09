for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={j*i}', end='\t')
    print()

num = int(input('press a number'))
init = 2
while num > init:
    if num % init == 0:
        print(f'{num} isn\'t a prime num')
        break
    init += 1
else:
    print(f'{num} is a prime num')

in_num = int(input('press a num'))

i = 0
while in_num > 0:
    i = in_num % 10 + i * 10
    in_num //= 10
print(i)

