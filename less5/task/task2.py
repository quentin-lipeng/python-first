h = 0
for i in range(5):
    num = int(input('press :'))
    if i == 0:
        max_num = min_num = num
    else:
        max_num = num if num > max_num else max_num
        min_num = num if num < min_num else min_num
    h += num
print(max_num, min_num, h)
