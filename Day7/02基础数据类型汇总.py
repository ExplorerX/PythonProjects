"""
str int
"""
# list
# 第一种
# lis = lis[::2]
# print(lis)

# 第二种
# l1 = []
# for i in lis:
#     if lis.index(i) % 2 == 0:
#         l1.append(i)
# lis = l1
# print(lis)

# lis = [11,22,33,44,55]
# # for i in range(len(lis)-1,-1,-1):
# #     if i % 2 == 1:
# #         print(i)
# #         del lis[i]
# #         print(lis)
# # print(lis)

# dic = dict.fromkeys([1, 2, 3], '春哥')
# print(dic)
# dic = dict.fromkeys([1, 2, 3], [])
# print(dic)  # {1: [], 2: [], 3: []}
# dic[1].append('袁姐')
# print(dic)
# dic[2].extend('二哥')
# print(dic)
# print(id(dic[1]), id(dic[2]), id(dic[3]))
# 转换成bool是false：
# 0 '' [] {} () set()

# 元组 元组里面如果只有一个元素而且不加都好，该是什么类型就是什么类型，只要加了逗号就是元组
tu1 = (1)
tu2 = (1,)
print(tu1, type(tu1))
print(tu2, type(tu2))
tu1 = ([1])
tu2 = ([1],)
print(tu1, type(tu1))
print(tu2, type(tu2))
