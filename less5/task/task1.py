i = 0
he = 0
while i < 5:
    num = int(input('press :'))
    # 初始值
    if i == 0:
        max_num = min_num = num
    else:
        max_n = num if num > max_n else max_n
        min_n = num if num < min_n else min_n
    he += num
    i += 1
print(max_n, min_n, he)
