# 问题：
# 创建一个字典，同时对字典做迭代或者序列化操作时，也能控制其中元素的顺序，因为普通字典是无序的
# 解决方案：
# 有序字典OrderDict，位于collections中的OrderDict类
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for k in d:
    print(k, d[k])
# 注意：
# OrderDict内部维护了一个双向链表，它会根据元素加入的顺序来排列键的位置
# OrderDict的大小是普通字典的2倍多，这是由于它额外创建的链表导致的。
