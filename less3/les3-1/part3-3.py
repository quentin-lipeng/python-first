st = 'hello world python'
print(st.count('o'))
# index和find查找一样 不同在于：find找不到返回- index报错
print(st.find('world'))  # 字符串索引从0开始
print(st.rfind('world'))  # 从右边开始查找
print(st.index('world'))
print(st.rindex('world'))
print(st.split('o'))  # ['hell', ' w', 'rld pyth', 'n']
print('max', st.split('o', maxsplit=1))
print(st.partition('w'))  # ('hello ', 'w', 'orld python') 分为三部分
print(st.replace('o', '0'))
print(st.replace('o', '0', 1))

