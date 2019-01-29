# def max(a, b):
#     return a if a > b else b
#
#
# print(max(45, 75))
#
#
# def my_max(x, y, z):
#     c = max(x, y)
#     return max(c, z)
#
#
# print(my_max(54, 45262, 34345))
# 函数的嵌套定义
# 内部函数可以使用外部函数的变量
# a = 1
# def outer():
#     a = 11
#     def inner():
#         global a
#         a += 1
#         print(a)
#         print('inner')
#     inner()
# outer()
# print(a)
# nonlocal只能用于局部变量，找上层中离当前函数最近的一层的局部变量
# 声明了nonlocal的内部函数的变量修改会影响到离当前函数最近一层的局部变量，但这个变量不能是全局变量


# 函数名可以作为容器类型的一个元素
# def func():
#     print(124)
# func2 = func
# 函数名就是内存地址
# 函数名可以赋值
# func2()
# l = [func, func2]
# for i in l:
#     i()
# def func():
#     print(123)
#
# def wahaha(f):
#     f()
# wahaha(func)  # 函数名可以作为函数的参数

# def func():
#     print(123)
#
# def wahaha(f):
#     f()
#     return f
# qqxing = wahaha(func)  # 函数名可以作为函数的返回值
# qqxing()
# 第一类对象：
# 1、可在运行期间创建
# 2、可用作函数参数或者返回值
# 3、可存入变量的实体
