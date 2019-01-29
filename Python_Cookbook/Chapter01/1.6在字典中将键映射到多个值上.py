# 问题：
# 我们想要一个将键映射到多个值上的字典即所谓的一键多值字典(multidict)
# 解决方案：
# 将键映射到另一个容器数据类型上，collections模块中的defaultdict类
# 它会自动初始化第一个值
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
# 使用集合还是列表取决于：
# 如果想要去重：使用集合
# 如果想要保留元素插入的顺序：使用列表
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(3)
e = defaultdict(set)
e['a'].add(1)
e['b'].add(2)
e['c'].add(3)
# setdefault(key, value)如果原来字典中有了这个元素就不改变原来的值，如果没有就添加这个键值对
