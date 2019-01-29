# property:把方法伪装成一个属性
# 内置装饰器函数，只在面向对象中使用
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property  # 直接用方法名获取返回值
    def area(self):
        return self.radius ** 2 * pi

    @property
    def perimeter(self):
        return self.radius * 2 * pi


c1 = Circle(5)
area = c1.area
perimeter = c1.perimeter
print(area)
print(perimeter)


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


p1 = Person('Alex')
print(p1.name)
p1.name = 'Egon'
print(p1.name)
del p1.name  # 执行到这一句就自动转到34行，执行这个被@name.deleter装饰的函数
print(p1.name)
