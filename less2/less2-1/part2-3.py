# age = 19
# if age >= 18:
#     print('you are an adult')
#     pass
# print('arrive')

# age = int(input('your age: '))


def age1(_age):
    if _age >= 18:
        print('you are an adult')
    else:
        print('you are not an adult')
    pass


def age2(_age):
    if 1 < _age < 120:
        print('legal')
    else:
        print('illegal')
    pass


man_id_card = True
woman_id_card = False

if man_id_card or woman_id_card:
    print('welcome')
else:
    print('sorry')
pass


is_student = True
if is_student:
    print('come in ')
else:
    print('you can\'t')