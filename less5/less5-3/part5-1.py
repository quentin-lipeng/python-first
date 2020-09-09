li1 = [1, 2, 3, 4, 5, 6, 7, 8]
li1_new = [i * i for i in li1]
print(li1_new)


def squ(num):
    return num * num


li1_new = [squ(i) for i in li1]

print(li1_new)

li1_new = [i for i in li1 if 2 % i == 0]
print(li1_new)

li1_new = [i ** 2 for i in li1 if i % 2 == 0 if i > 2]
print(li1_new)

li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li2_new = [i for li in li2 for i in li1]
print(li2_new)

li2_new = [li2[i][0] for i in range(len(li2))]
print(li2_new)
li2_new = [li2[i][i] for i in range(len(li2))]
print(li2_new)