# money = int(input('press money'))
# while money >= 10:
#     money -= 10
#     print('剩余', money)
# pass

i = 0
while i < 10:
    print('凉凉')
    i += 1
print('over')
pass

i = 1
while i < 6:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    i += 1
pass

n = int(input('press number'))
i = 1
while i <= n:
    if i == 1 or i == n:
        print(n * '#')
        i += 1
        continue
    print('#', end='')
    j = 1
    while j <= n-1:
        if j == n-1:
            print('#')
            j += 1
            continue
        print(' ', end='')
        j += 1
    i += 1
pass

while True:
    name = str(input('press name'))
    if name == 'zs':
        print('name is correct')
        while True:
            password = str(input('press password'))
            if password == '123':
                print('welcome')
                break
            else:
                print('password is invalid')
            pass
        break
    else:
        print('name is invalid')


