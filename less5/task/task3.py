h = 0
for i in range(5):
    num = int(input('press :'))
    if i == 0:
        max_n = min_n = num
    else:
        max_n = num if max_n < num else max_n
        min_n = num if min_n > num else min_n
    h += num
print(max_n, min_n, h)
