s = '213124'
i = len(s) - 1
while i >= 0:
    print(s[i], end=' ')
    i -= 1

print()
for i in range(-1, -len(s)-1, -1):
    print(s[i], end=' ')

a = 1
b = 2
a, b = b, a
print()
print(a, b)

st = '123_sadASD_'
flag = 0
for s in st:
    i = ord(s)
    if 48 <= i <= 57 \
            or 65 <= i <= 90 \
            or 97 <= i <= 122:
        flag += 1
print(flag)
