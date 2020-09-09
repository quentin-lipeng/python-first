num = 1
while num < 6:
    print('*  ' * num)
    num += 1
    pass

while num < 10:
    if num == 8:
        print('break')
        break
    else:
        num += 1
        print(num)
    pass

num1 = 0
while num1 < 10:
    num1 += 1
    if num1 % 2 == 0:
        print("跳出")
        continue
    else:
        print(num1)
    pass

num2 = 1
while num2 < 3:
    print(num2)
    num2 += 1
else:
    print('over')
pass

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print('*  ', end='')
        col += 1
    print()
    row += 1
    pass

