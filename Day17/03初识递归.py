# 递归函数
#   了解什么是递归：在函数中调用自身
#       最大递归深度是997/998 是python从内存角度出发做的优化和限制
#       可以修改
#       如果递归次数太多就不适合递归来解决问题
#       import sys
#       sys.setrecursionlimit(递归最大深度)
#       优点：会让代码变简单
#       缺点：占内存
#   能看懂递归
#   能知道递归的应用场景
#   初识递归 ——
#   算法——二分查找算法
#   三级菜单
# import sys
# sys.setrecursionlimit(1000)
# n = 0
#
#
# def story():
#     global n
#     n += 1
#     print(n)
#     story()
#
#
# story()

# 计算年龄的递归算法：


def age(n):
    if n == 4:
        return 40
    elif 0 < n < 4:
        return age(n + 1) + 2


print(age(1))
