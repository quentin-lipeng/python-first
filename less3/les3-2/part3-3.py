s = 'hello world this is python'
print(s.split('l', maxsplit=1))

print(s.replace('o', '0'))
print(s.replace('o', '0', 1))
print(s.center(10))
print(s.center(10, '*'))
print(s.ljust(10, '~'))
print(s.rjust(10, '~'))
print(s.zfill(10))
print(s.strip('~'))
print(s.rstrip('~'))
print(s.lstrip('~'))

