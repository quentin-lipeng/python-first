# salary = int(input('your salary :'))
# if salary > 10000:
#     print('买大众')
#
# if 5000 < salary < 10000:
#     print('买qq')
#
# money = int(input('消费金额'))
# if money >= 3000:
#     sex = input('性别')
#     if sex == '男':
#         print('送女盆友')
#     else:
#         print('送蓝盆友')
# else:
#     sex = input('性别')
#     if sex == '男':
#         print('打火机')
#     elif sex == '女':
#         print('发卡')
#     pass

price = float(input('西瓜单价'))
num = float(input('西瓜数量'))
money = price * num
if money > 300:
    print('会员价', money * 0.8)
else:
    print('价格', money)

zs_card = True
ls_card = False
if zs_card or ls_card:
    print('welcome')
else:
    print('you cant')
pass

is_student = True
if not is_student:
    print('you cant')
else:
    print('come in')

holiday = '情人节'
if holiday == '情人节':
    print('flower')
elif holiday == '平安夜':
    print('apple')
elif holiday == '生日':
    print('cake')
else:
    print('关心gf')
pass

has_tic = True
kni_len = 23
if has_tic:
    print('enter')
    if kni_len > 20:
        print('kni 过长 不符合规定')
else:
    print('you cant')
pass

st = ''
res = '爬虫' if st else '@@@'
print(res)

