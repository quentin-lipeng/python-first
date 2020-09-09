# 优先级 not > and > or
print(True and False or not True)
# 短路逻辑
i = 0
j = 10
# 如果i为false则后面不执行
print(i and j)
# i为False后面继续执行
print(i or j)

from logging42 import logger

st = ''
# print('a' if st else 'null')
logger.info('hello')

