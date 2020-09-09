i = 2
num = int(input('press a number'))
if num < i:
    print('not prime')
while i < num:
    if num % i == 0:
        print(num, 'not prime')
        break
    i += 1
else:
    print('%d is prime' % num)
pass
