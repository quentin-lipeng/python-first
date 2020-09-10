li1 = [1, 2, 3, 4, 5, 6, 7, 8]
li1_new = [i * i for i in li1]
print(li1_new)


def squ(num):
    return num * num


new_li1 = [squ(i) for i in li1]
print(new_li1)

li1_new = [i for i in li1 if i % 2 ==1]
print(li1_new)

li1_new = [i ** 2 for i in li1 if i % 2 == 0 if i > 2]
print(li1_new)

li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_li1 = [i for i in li2 for j in li1]
print(new_li1)
for i in li2:
    for j in i:
        print(j, end=',')

for i in range(len(li2)):
    print()
    print(li2[i][0])
li2_new = [li2[i][0] for i in range(len(li2))]
print(li1_new)

lst2 = [li2[i][i] for i in range(len(li2))]
print(lst2)


a=[lambda x:x*i for i in range(7)]

print(a[6](4))
print(id(a[3]))
print(id(a[4]))
# print(a[0](6))