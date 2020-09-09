holiday_name = 'valentin\'s day'
if holiday_name == 'valentin\'s day':
    print('go buy flower')
elif holiday_name == 'Christmas Eve':
    print('go buy some apples')
elif holiday_name == 'birthday':
    print('go buy an cake')
else:
    print('hhh')
pass

has_tik = True
knife_len = 23
if has_tik:
    print('火车票通过')
    if knife_len >= 20:
        print('刀具超过规定长度')
    else:
        print('安检通过')
else:
    print('无车票 不可通过')
pass

x = 1
y = 2
z = 3
if x:
    a = y
else:
    a = z
print(a)
c = y if x else z
print(c)
pass


def gam1():
    player = int(input('请输入要出的拳头 石头(1) 剪刀(2) 布(3) :'))
    computer = 1
    print('玩家出 %s, 电脑出 %s' % (player, computer))

    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('电脑输')
    elif player == computer:
        print('平局')
    else:
        print('电脑赢')
    pass


pass

import random


def gam2():
    player = int(input('请输入要出的拳头 石头(1) 剪刀(2) 布(3) :'))
    computer = random.randint(1, 3)
    print('玩家是%s, 电脑是%s' % (player, computer))
    if player == 1 and computer == 2 \
            or player == 2 and computer == 3 \
            or player == 3 and computer == 1:
        print('电脑输')
    elif player == computer:
        print('平局')
    else:
        print('电脑赢了')
    pass


pass

gam2()
