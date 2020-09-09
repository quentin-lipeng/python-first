class Person:
    def __init__(self, __name):
        self._name = __name
        self.age = 1
        pass

    @property  # 加了此修饰可以使用对象.方法名访问(相当于一个属性使用) 不加需要对象.方法名()使用
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print('delete name')
        self._name = None
        pass


pass

p = Person('')
p.name = 'lee'
del p.name
print(p.name)
