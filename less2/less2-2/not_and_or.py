# not > and > or
print(True and False)
print(True or False)
print(True and False or not False)
print(False or False or not False)

a = 0
b = 1
c = 2
d = 3
b1 = a and b and c and d  # 0
print(b1)
b2 = a or b or c or d
print(b2)
