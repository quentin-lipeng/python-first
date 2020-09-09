name = 'My name is Mike'

print(name[0])
print(name[-1])

s = 'hello world'
print(s[0:8:1])
print(s[0:7:2])

print(s[0:8])
print(s[0:])
print(s[8:])

print(s[:])
print(s[::2])
print(s[:8:2])
print(s[4:8:2])

print(s[0:8:-1])
print(s[8:0:-1])
print(s[::-1])

print(s[-8:5])
print(s[0:-8])
print(s[-1:8:-2])

for i in s:
    print(i)
pass
