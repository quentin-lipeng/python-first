class A:
    """this is a document"""
    pass

    def __own(self):
        print('__own')
        return '__own'


a = A()

print(a.__doc__)
# 访问私有方法 对象._类名__私有方法名 非法不建议使用
a._A__own()
