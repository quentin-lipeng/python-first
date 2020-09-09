num = int(input('press here :'))

if num < 2:
    raise Exception

for i in range(2, num):

    if num % i == 0:
        print('its not')
        break
else:
    print('it is')

i = 2
while num > i:
    if num % i == 0:
        print('It\'s not')
        break
    i += 1
else:
    print('It is')
