# 抽象类：python原生支持的
# 接口类：python原生不支持的
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):  # 指定为元类，一般创建类的时候默认是type
    @abstractmethod
    def pay(self, money):
        # raise NotImplemented  # 没有实现这个方法 raise主动抛出一个异常
        pass
# 规范：接口类或抽象类都可以
# 接口类：支持多继承，接口类中的所有的方法都必须不能实现
# 抽象类：不支持多继承，抽象类中的方法可以有一些代码的实现


class Wechat(Payment):
    def pay(self, money):
        print('使用微信支付了{}元。'.format(money))


class Alipay(Payment):
    def pay(self, money):
        print('使用支付宝支付了{}元。'.format(money))


class Applepay(Payment):
    def pay(self, money):
        print('使用苹果支付支付了{}元。'.format(money))


def pay(pay_obj, money):
    pay_obj.pay(money)


wechat = Wechat()
pay(wechat, 12134)
alipay = Alipay()
pay(alipay, 4567457)
applepay = Applepay()
pay(applepay, 4567)
