money = float(input('press money'))

while True:
    gender = input('press your gender')
    if money >= 500:
        if gender == 'female':
            print('化妆品')
            break
        elif gender == 'male':
            print('手表')
            break
        else:
            print('sth getting wrong')
    else:
        if gender == 'female':
            print('发卡')
            break
        elif gender == 'male':
            print('领带')
            break
        else:
            print('sth getting wrong')

        pass

pass
