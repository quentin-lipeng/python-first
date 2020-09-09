num = float(input('press three number'))
a = num * 1000 % 10
b = num * 1000 // 10 % 10
c = num * 1000 // 100 % 10
gw = int(num) % 10
sw = int(num) // 10
final = a ** 10000 + b * 1000 + c * 100 + gw * 10 + sw
print(final / 100)
