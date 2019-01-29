# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# a = A()
# print(isinstance(a, A))
# print(issubclass(B, A))
# print(issubclass(A, B))
# 反射：用字符串类型的名字去操作变量
# 反射就没有安全问题
# 反射对象中的属性和方法 hasattr getattr setattr delattr
import sys
#
#
# class A:
#     def func(self):
#         print('in func')
#
#
# a = A()
# a.name = 'alex'
# 反射对象的属性
# ret = getattr(a, 'name')
# print(ret)

# 反射对象的方法
# ret = getattr(a, 'func')
# print(ret)
# ret()
# year = 2018
#
#
# def func():
#     print('This is a function!')
# 反射自己模块的变量


# print(getattr(sys.modules['__main__'], 'year'))
# print(getattr(sys.modules[__name__], 'year'))

# 反射自己模块的函数
# getattr(sys.modules['__main__'], 'func')()
# getattr(sys.modules[__name__], 'func')()
import time
sign = input('>>>')
print(getattr(time, sign)())

# setattr: 设置修改变量
# delattr：删除一个变量
