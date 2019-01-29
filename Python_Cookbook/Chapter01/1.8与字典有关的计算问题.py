# 问题：
# 我们想在字典上对数据执行各式各样的计算，比如：求最大值、最小值、排序等
# 解决方案：
# 使用zip()方法通过对字典的键值对反转为值键对序列来解决这个问题
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
# 注意：zip()拉链方法，创建了一个迭代器，它的内容只能被消费一次
# 如以下代码就不行：
prices_and_nums = zip(prices.values(), prices.keys())
print(min(prices_and_nums))
print(max(prices_and_nums))
# 在上述的min()和max()方法中对容器数据类型进行比较的时候，先比较容器内的第一个元素，相同继续往后比较
# 如1.5中的heapq的排列比较一样
