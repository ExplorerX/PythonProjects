# import time
#
#
# def wrapper(f):  # 装饰器函数
#     def inner():
#         start = time.time()
#         f()  # 被装饰的函数
#         end = time.time()
#         print(end - start)
#     return inner
#
#
# @wrapper  # 相当于func = wrapper(func)
# def func():
#     print('我是被装饰的函数')


# func = wrapper(func)
# func()

# 装饰器的作用：不想修改函数的调用方式，但是还想在原来的函数的前后添加代码
# 开放封闭原则：开放：对拓展开放
#              封闭：对修改封闭

# 装饰器的格式
# def wrapper(f):
#     def inner(*args, **kwargs):
#         # 在前面修改的代码
#         ret = f(*args, **kwargs)
#         # 在后面修改的代码
#         return ret
#     return inner
#
#
# @wrapper  # 语法糖
# def func():
#     return 123
#
#
# print(func())

# 接受就是元组，调用就是打散
