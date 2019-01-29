# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
#
# f1 = Foo('sb')
# f1['age'] = 18
# print(f1['age'])
# f1['age1'] = 19
# del f1.age1
# del f1['age']
# f1['name'] = 'alex'
# print(f1.__dict__)

# item系列实现的功能是就是类似字典和列表，使用中括号里面的加入值，后者索引来找到元素
# 做一个大胆的猜想，在python解释器里面只要发现你在一个类的后面使用了中括号[]，
# 就会去类中寻找这个item系列的方法。换句话说就是因为这些item系列方法的存在才能使用
# 中括号进行一个字典和列表的实现
# 在使用类似f1['age'] = 18这种操作的时候使用的是内置的双下setitem方法
# 在使用类似f1['age']这种操作的时候使用的是内置的双下getitem方法
# 在使用类似del f1['age']这种操作的时候使用的是内置的双下delitem方法
# 在使用类似del f1.age1这种操作的时候使用的是内置的双下delattr方法

# 构造方法


class A:
    def __init__(self):
        self.x = 1
        print('in init function')

    def __new__(cls, *args, **kwargs):
        print('in new function')
        return object.__new__(A)


a = A()
print(a.x)

# 双下new方法是传统的构造方法，在实例化一个对象的时候在双下init方法前面调用
# 其中的cls参数就是只带的这个类，就好比self方法只带的是这个对象一样


# 单例模式，没什么好说的，我觉的很傻比的模式


class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance


one = Singleton()
two = Singleton()

two.a = 3
print(one.a)
# 3
# one和two完全相同,可以用id(), ==, is检测
print(id(one))
# 29097904
print(id(two))
# 29097904
print(one == two)
# True
print(one is two)
