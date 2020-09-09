def solid():
    for n in range(5):
        print('*' * 5)
    pass


def hollow():
    n = 5
    flag = 0
    while flag < n:
        if flag == 0 or flag == n:
            print('*' * n)
        flag += 1
        for i in range(5):
            if i == 0 or i == 4:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    else:
        print('*' * n)


hollow()
