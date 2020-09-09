def ten_l():
    for i in range(10):
        print('凉凉')
    pass


# 5050
def one_to_hun():
    n = 1
    flag = 1
    while flag < 100:
        flag += 1
        n += flag
    print(n)
    pass


def star():
    n = 5
    flag = 0
    while flag < n:
        flag += 1
        j = 0
        while j < flag:
            print('*', end='  ')
            j += 1
        pass
        print('')


star()
