"""
集合：可变的数据类型，但是存储的元素必须是不可变的数据类型，集合无序，不重复，可以求交差并集
"""
# set的创建两种：
# set1 = set({1, 2, 3, 4})
# set2 = {1, 2, 3, 4}
# print(set2)
# 方法只有增加和删除
# 增加
set1 = {'alex', 'wusir', 'ritian', 'egon', 'barry', 'barry'}
# set1.add('女神')
# print(set1)
#
# set1.update('abc')  # 相当于list里面的extend
# print(set1)
# 删除
# set1.pop()  # 随机删除
# print(set1.pop())
# 按元素去删除
set1.remove('alex')
print(set1)
# 清空集合
# set1.clear()
# print(set1)
# dic = {}
# print(dic)
# li = []
# print(li)
# 查
for i in set1:
    print(i)
set2 = {1, 2, 3, 4}
set3 = {5, 6, 3, 4}
set8 = {1, 2}
# 交集
set4 = set2 & set3
print(set4)
set4 = set2.intersection(set3)
print(set4)
# 并集
set5 = set2 | set3
print(set5)
set5 = set2.union(set3)
print(set5)
# 反交集
set6 = set2 ^ set3
print(set6)
set6 = set2.symmetric_difference(set3)
print(set6)
# 差集
set7 = set2 - set3
print(set7)
set7 = set2.difference(set3)
print(set7)
# 子集
print(set8 < set2)
print(set8.issubset(set2))
# 超集
print(set2 > set8)
print(set2.issuperset(set8))
# 去重
li = [1, 2, 3, 4, 5, 3, 23, 211]
set9 = set(li)
print(set9)
li = list(set9)
print(li)

# 不可变的集合
s = frozenset('zahng')
print(s)

"""
对于赋值运算来说，l1与l2指向的是同一个内存地址，所以他们是完全一样的。
对于浅copy来说，第一层创建的是新的内存地址，而从第二层开始，指向的都
    是同一个内存地址，所以，对于第二层以及更深的层数来说，保持一致性。
    l1 = [1,2,3,['barry','alex']]
    l2 = l1.copy()
对于深copy来说，两个是完全独立的，改变任意一个的任何元素（无论多少层
    ），另一个绝对不改变。
    l1 = [1,2,3,['barry','alex']]
    l2 = copy.deepcopy(l1)
"""
