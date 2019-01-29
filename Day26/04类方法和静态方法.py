# method方法
# staticmethod 静态方法  ***:是为了纯面向对象使用的一个方法，
#   将一个和这个类和对象无关的方法放入对象中使用@staticmethod进行装饰
# classmethod 类方法 ****
# 类里面的方法


class Goods:
    __discount = 0.8

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod
    def change_discount(cls, new_discount):
        Goods.__discount = new_discount


goods1 = Goods('apple', 5)
print(goods1.name, goods1.price)
Goods.change_discount(0.5)
print(goods1.name, goods1.price)
