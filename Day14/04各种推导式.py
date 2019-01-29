# [每一个元素或者是和元素相关的操作 for元素 in 可迭代数据类型]
# [满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]
# 30以内所有能被3整除的数
# l1 = [i for i in range(30) if i % 3 == 0]
# print(l1)
# 30以内所有能被3整除的数的平方
# l2 = [i**2 for i in range(30) if i % 3 == 0]
# print(l2)
# 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# list1 = [name for li in names for name in li if name.count('e') == 2]
# 生成器表达式
list1 = (name for li in names for name in li if name.count('e') == 2)
print(list1)
# 列表推导式[]

# 字典推导式{}
# 将一个字典的key和value对调
# m_case = {'a': 10, 'b': 34}
# print(m_case)
# m_case_frequency = {m_case[k]: k for k in mcase}
# print(m_case_frequency)
# 合并大小写对应的value值，将k统一成小写
# my_case = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# my_case_frequency = {k.lower(): my_case.get(k.lower(), 0) + my_case.get(k.upper(), 0) for k in my_case}
# print(my_case_frequency)

# 集合推导式{}
squared = {x**2 for x in [1, -1, 2]}
print(squared)

# 各种推导式：生成器 列表 字典 集合
#   遍历操作
#   筛选操作
