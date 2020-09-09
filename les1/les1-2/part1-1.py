print('hello')
v1 = 'a'
print(type(v1))  # <class 'str'>
print(type(10.2))  # <class 'float'>
print(type(True))  # <class 'bool'>

print(True + 10.2)  # 11.2
print(10 + 10.2, type(10 + 10.2))  # 20.2 <class 'float'>
print(True + False)  # 1

print(bool(2))  # True

print(int(2.12))  # 2

print(0o011101)  # 4673

# 16进制
print(0x0A)  # 10
# 8进制
print(0b1001)  # 9
# hex() oct(0 bin()
print(hex(10))
print(oct(10))
print(bin(10))
# 将16进制的0x0A转化为10进制
print(int('0x0A', base=16))

