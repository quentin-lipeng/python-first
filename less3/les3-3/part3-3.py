st = 'hello world python'
print(st.count('o'))
print(st.find('world'))
print(st.rfind('world'))

print(st.index('hello'))
print(st.rindex('world'))

print(st.partition('hello'))
print(st.splitlines())
print(st.split('l'))

print(st.split('l', maxsplit=1))

print(st.replace('o', '0'))
print(st.replace('o', '0', 1))

s = 'hello'
print(s.center(10))
print(s.center(10, '*'))
print(s.ljust(10, '~'))
print(s.rjust(10, '~'))
print(s.strip('~'))
print(s.rstrip('~'))
print(s.lstrip('~'))

name = '小米'
age = 18
height = 1.78
weight = 70
msg = '姓名 %s, 年龄 %d, 身高 %.2f, 体重 %d' % (name, age, height, weight)
print(msg)