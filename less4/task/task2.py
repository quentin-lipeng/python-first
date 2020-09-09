num = int(input('press five number :'))
length = len(str(num))
i = 0
r = 0
while num > 0:
    r += num % 10
    num //= 10
else:
    print(r / length)
