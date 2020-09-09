s = 'hello'
print(s.center(10))  # 已str为中心 其他不足用空格代替
print(s.center(10, '*'))
print(s.ljust(10, '~'))
print(s.rjust(10, '~'))
print(s.zfill(10))
print(s.strip())  # 默认删除两边空格
print(s.strip('~'))
print(s.rsplit('~'))
print(s.lstrip('~'))