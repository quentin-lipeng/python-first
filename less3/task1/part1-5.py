for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (j, i, j*i), end='\t')
    print()

num = int(input('press a num'))
for i in range(2, num):
    if num % i == 0:
        print('its not')
        break
else:
    print('it is ')

in_n = int(input('press a num'))
i = 0
while in_n > 0:
    i = in_n % 10 + i * 10
    in_n //= 10
print(f'{i}')
