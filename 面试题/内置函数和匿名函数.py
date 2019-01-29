# 1、现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# res = zip(('a', 'b'), ('c', 'd'))
# func = lambda ret: ({i[0], i[1]} for i in ret)
# print(list(func(res)))
# #答案一
# test = lambda t1,t2 :[{i:j} for i,j in zip(t1,t2)]
# print(test(t1,t2))
# #答案二
# print(list(map(lambda t:{t[0]:t[1]},zip(t1,t2))))
# #还可以这样写
# print([{i:j} for i,j in zip(t1,t2)])

# 2、以下代码的输出是什么？请给出答案并解释。
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。


# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# 列表推导式会直接占用一块内存，生成一个列表，所以for循环是一次执行完毕的，然后上述函数返回一个列表
# 类似这样：
# [lambda x:i*x for i in range(4),
# lambda x:i*x for i in range(4),
# lambda x:i*x for i in range(4),
# lambda x:i*x for i in range(4)]
# 因为lanmbda表达式也是一个函数，在调用之前是不执行的，而在整个multyiliers函数中的i保持在for循环之后的
# 3，所以在后来调用的时候使用的i的值就是3
# 而生成器因为其惰性运算的特性，只有你用的时候要一个值，给一个值，所以，改为如下代码：
def multipliers():
    return (lambda x: i*x for i in range(4))
# 返回一个生成器，每次在[m(2) for m in multipliers()]列表推导式里面执行的时候才用一次
# lambda表达式


print([m(2) for m in multipliers()])
