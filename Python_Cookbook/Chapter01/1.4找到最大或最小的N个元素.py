# 问题：
# 在某个集合中找到最大或最小的N个元素
# 解决方案：
# heapq模块中有两个数——nlargest()和nsmallest()
import heapq
# num = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, num))
# print(heapq.nsmallest(3, num))
#
# # 这两个函数都还可以接受一个参数key
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])
# print(cheap)
# print(expensive)

# 以下函数首先会在底层将数据转化成列表。切元素会以堆的顺序排列
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)  # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]转化成了小顶堆

# 注意：
# 如果找的元素数量相对较少，nlargest()和nsmallest()才是最合适的
# 如果想很快的找到最大最小元素，max()和min()函数会更加快
# 如果N和集合大小差不多，通常更快的方法是先对集合排序，然后做切片操作
