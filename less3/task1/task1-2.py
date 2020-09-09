for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i*j}', end='\t')
    print()

num = int(input('press a number :'))

i = 0
while num > i:
    i += 1
    if num % i == 0:
        print('not prime number!')
        break
else:
    print('it is prime number')


in_num = int(input('press a number'))

i = 0
while in_num > 0:
    i = in_num % 10 + i * 10
    in_num //= 10
print(i)
