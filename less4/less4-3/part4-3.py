a = [123, 345, 567, 67]
i = 0
while i < len(a):
    b = 0
    while a[i] > 0:
        # 每次取个位 之后每一次最前一位的数进一位
        b = b * 10 + a[i] % 10
        # 每次原始数字退一位
        a[i] = a[i] // 10
    a[i] = b
    i += 1
print(a)


