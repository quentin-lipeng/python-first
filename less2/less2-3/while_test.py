num = 0
while num < 10:
    if num == 4:
        print('跳出')
        break
    print('当前的num值为%d' % num)
    num += 1
pass

num = 0
while num < 10:
    if num == 4:
        print('跳出循环')
        num += 1
        continue
    print('当前num值为%d' % num)
    num += 1
pass

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        print('con')
        continue
print(n)
