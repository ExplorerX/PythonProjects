# 列表
# 字典
# 集合 frozenset
# 字符串
# 元组
# 堆栈：先进后出
# 队列：先进先出

# namedtuple('名称', [属性List])
# Circle = namedtuple('Circle', ['x', 'y', 'z'])
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p)
# print(p.x, p.y)

# 队列
# import queue
# q = queue.Queue()
# q.put(10)
# q.put(6)
# q.put(5)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())  # 阻塞

# 双端队列
from collections import deque
dq = deque()
dq.append(1)  # 从后面放数据
dq.appendleft(2)  # 从前面放数据
# deque.pop()  # 从后面取数据
# deque.popleft()  # 从前面取数据
dq.insert(1, 3)
print(dq.pop())
