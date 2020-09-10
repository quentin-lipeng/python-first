h = 0
for i in range(5):
    num = int(input('press :'))
    if i == 0:
        ma_n = mi_n = num
    else:
        ma_n = num if ma_n < num else ma_n
        mi_n = num if mi_n > num else mi_n
    h += num
print(ma_n, mi_n, h)