msg = '我叫{name}， 今年{age}岁'
print(msg.format(name='zs', age=18))
print('我叫{:*^5}, 今年{:<4}岁'.format('三', 50))

print('长方形的宽是 {:.2f}cm 高为{:.3f}cm 求面积为 '.format(3/2, 5/3))
print('二进制{:b}'.format(10))
print('八进制{:o}'.format(10))
print('十六进制{:x}'.format(10))

name = '小米'
age = 12
height = 1.7
weight = 80
msg = '姓名: %s, 年龄: %d, 身高: %.2f, 体重:%d' % (name, age, height, weight)
print(msg)