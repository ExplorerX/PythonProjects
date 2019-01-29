# 类的定义：
# class 类名:
#     属性名 = 'a'
#
# print(类名.属性名)
# 过程：
# 类名()首先会创造一个对象，创建一个self变量
# 调用init方法，类名括号里的参数会被这里接收
# 执行init方法
# 返回self
# 对象能做的事
# 查看属性，调用方法
# 类名能做的事：
# 实例化，调用方法

# class Person:
#     # 类属性 静态属性
#     country = 'China'  # 创造了一个只要是这个类就一定有
#
#     def __init__(self, *args):
#         self.name = args[0]
#         self.hp = args[1]
#         self.aggr = args[2]
#         self.sex = args[3]
#
#     def walk(self, n):
#         print('%s走走走，走了%d步.' %(self.name, n))
#
#
# alex = Person('alex', 100, 5, 'male')
# alex.walk(10)

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return self.radius * 2 * pi


c = Circle(5)
print(c.area())
print(c.perimeter())
