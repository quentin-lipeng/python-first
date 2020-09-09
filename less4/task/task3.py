li1 = []
for i in range(5):
    li1.append(int(input('press five number :')))

for i in range(len(li1)):
    for j in range(len(li1)-1):
        if li1[j] > li1[j+1]:
            b = li1[j]
            li1[j] = li1[j+1]
            li1[j+1] = b
else:
    print('bigger : ', li1[len(li1)-1])
    print('smaller : ', li1[0])
    print('sum : ', eval(f'{li1[0]} + {li1[len(li1)-1]}'))
