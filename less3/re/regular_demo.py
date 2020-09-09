import re

def re1():
    origin = 'asdw3123.+-2_-'
    str_pattern = '[a-zA-Z]'
    num_par = '\d'
    number = []
    string = []
    symbel = []
    for s in origin:
        if re.search(str_pattern, s):
            string.append(s)
        elif re.search(num_par, s):
            number.append(s)
        else:
            symbel.append(s)

    print(string, number, symbel)


def re2():
    sentence = 'I am a student'

    part = re.compile(r't$')
    mats = part.finditer(sentence)
    for m in mats:
        print(m)

re2()
