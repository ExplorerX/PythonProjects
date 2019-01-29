# 带参数的装饰器
# 装饰器的本质就是闭包
# 闭包的本质就是内层函数使用了外层函数的变量，而这个变量会一直存在于内存中
# import time
# FLAG = True
#
#
# def wrapper(flag):
#     def tim(f):
#         def inner(*args, **kwargs):
#             if not flag:
#                 start = time.time()
#                 ret = f(*args, **kwargs)
#                 end = time.time()
#                 print(end - start)
#                 return ret
#             else:
#                 ret = f(*args, **kwargs)
#                 return ret
#         return inner
#     return tim
#
#
# @wrapper(FLAG)
# def func(*args):
#     time.sleep(0.1)
#     sum1 = 0
#     for i in args:
#         sum1 += i
#     return sum1
#
#
# # li = [1, 2, 3, 4]
# result = func(1, 2, 3, 4)
# print(result)


# 多个装饰器装饰一个函数，就像俄罗斯套娃
def wrapper1(f):
    def inner1(*args, **kwargs):
        print('This is front string in inner1!')
        ret = f(*args, **kwargs)
        print('This is behind string in inner1!')
        return ret
    return inner1


def wrapper2(f):
    def inner2(*args, **kwargs):
        print('This is front string in inner2!')
        ret = f(*args, **kwargs)
        print('This is behind string in inner2!')
        return ret
    return inner2


@wrapper1
@wrapper2
def func(*args):
    sum1 = 0
    print('This is a sum function!')
    for i in args:
        sum1 += i
    return sum1


result = func(1, 2, 3, 4, 5, 6)
print(result)
# 运行结果：
"""
This is front string in inner1!
This is front string in inner2!
This is a sum function!
This is behind string in inner2!
This is behind string in inner1!
21
"""
