# def generator():
#     print(123)
#     content = yield 1
#     print('======', content)
#     print(456)
#     yield 2
#
#
# g = generator()
# ret = g.__next__()
# print('***', ret)
# # ret = g.send(None)  # send的效果和next一样
# ret = g.send('Hello')
# print('***', ret)

# send 的获取下一个值的效果和next基本一致
# 只实在获取下一个值的时候，给上一个yiele的位置传递一个数据
# 使用send的注意事项：
#   第一次使用生成器的时候，是用next获取下一个值
#   最后一个yield不能接受外部的值

# 获取移动平均值：
# 计算平均值：avg = sum / count


# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
#
# avg_g = average()
# avg_g.__next__()
# while True:
#     number = int(input('Please input a number:'))
#     print(avg_g.send(number))

# 预激生成器的装饰器：为了在拿到生成器的时候就可以使用send方法，在装饰器中进行生成器的激活
# def init(func):  # 装饰器
#     def inner(*args, **kwargs):
#         g = func(*args, **kwargs)
#         g.__next__()
#         return g
#     return inner
#
#
# @init
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
#
# avg_g = average()
# while True:
#     number = int(input('Please input a number:'))
#     print(avg_g.send(number))

# 面试题：携程函数的例子：
# import os
#
#
# def init(func):
#     def wrapper(*args, **kwargs):
#         g = func(*args, **kwargs)
#         next(g)
#         return g
#     return wrapper
#
#
# @init
# def list_files(target):
#     while 1:
#         dir_to_search = yield
#         for top_dir, dir, files in os.walk(dir_to_search):
#             for file in files:
#                 target.send(os.path.join(top_dir, file))
#
#
# @init
# def opener(target):
#     while 1:
#         file = yield
#         fn = open(file)
#         target.send((file, fn))
#
#
# @init
# def cat(target):
#     while 1:
#         file, fn = yield
#         for line in fn:
#             target.send((file, line))
#
#
# @init
# def grep(pattern, target):
#     while 1:
#         file, line = yield
#         if pattern in line:
#             target.send(file)
#
#
# @init
# def printer():
#     while 1:
#         file = yield
#         if file:
#             print(file)
#
#
# g = list_files(opener(cat(grep('python', printer()))))
# g.send('/test1')

# 协程应用：grep -rl /dir
#
# tail&grep

# 将字符串中的字符一个一个返回
def generator():
    a = '12345'
    b = 'abcde'
    yield from a
    yield from b


g = generator()
for i in g:
    print(i)
