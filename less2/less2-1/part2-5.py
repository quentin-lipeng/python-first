count = 0
while count < 5:
    print('凉凉一首')
    count += 1
    pass
print('over')


def one_hun():
    num1 = 0
    flag = 1
    while flag <= 100:
        num1 += flag
        flag += 1
    else:
        print(num1)
    pass


pass


# 2550
def dou_sum():
    num = 0
    end = 100
    start = 0
    flag = 1
    while flag <= end/2:
        flag += 1
        if end or start % 2 == 0:
            num += end + start
            end -= 2
            start += 2
            print(num)
    else:
        num += end
        print(num)
    pass


pass


dou_sum()
