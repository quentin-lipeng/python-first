# 一个一个求商 求不尽的就是质数 消耗资源
def prime():
    n = int(input('press number'))
    for i in range(2, n):
        if n % i == 0:
            print('%d is not a prime' % n)
            break
    else:
        print('%d is a prime' % n)


prime()
