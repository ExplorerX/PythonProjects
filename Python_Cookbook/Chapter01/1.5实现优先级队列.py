# 问题：
# 我们想要实现一个优先级队列，它能够以给定的优先级来对元素排序，
# 且每次pop操作都会返回优先级最高的那个元素
# 解决方案：
# heapq模块
import heapq  # 导入heap queue模块


class PriorityQueue:  # 定义优先级队列类
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def push(self, item, priority):
        """
        优先级队列入队方法
        :param item: 入队的项
        :param priority: 优先级
        :return: None
        """
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        # 上述的代码实现压入一个元素进入堆中，压入的格式为一个元组(-priority, self.__index, item)
        # 压入这个元组之后，堆排序会从元组的第一个元素开始比较进行堆排序，当元组中的第一个元素相同时
        # 比较第二个元素，以此类推
        self.__index += 1
        # 为了保证在优先级相同的情况下，先输入的元素排在前面使用pop，使用index约束

    def pop(self):
        """
        优先级队列弹出优先级最高的元素方法
        :return: 优先级最高的元素
        """
        return heapq.heappop(self.__queue)[-1]
        # 元组结构为(-priority, self.__index, item)，需要的只是item，所以从后面返回一个，
        # 最后一个元素的索引为-1


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # 重写__repr__方法，输出的时候直接输出Item，原本是输出这个对象的内存地址
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
