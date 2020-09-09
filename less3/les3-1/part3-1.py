name = 'My Name is Mike'

char = name[0]
print(char)
char1 = name[-1]
print(char1)

# 起始：结束：步长
char2 = name[0:8:2]  # M ae
print(char2)
char3 = name[0:5]
print(char3)

char4 = name[0:]  # My Name is Mike
print(char4)
char5 = name[:8]  # My Name
print(char5)
char6 = name[:]  # My Name is Mike
print(char6)
char7 = name[::2]  # M aei ie
print(char7)

char8 = name[0:8:-1]  # 取不到
print('8', char8)
char9 = name[8:0:-1]  # i emaN y
print(char9)

char10 = name[-8:5]  # 取不到
print('10', char10)
char11 = name[0:-8]  # My Name
print(char11)
char12 = name[-1:8:-2]  # ei
print(char12)

for s in name:
    print(s)
else:  # 可省略
    print('done')