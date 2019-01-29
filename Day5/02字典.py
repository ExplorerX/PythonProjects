# dict
"""
数据类型划分：可变数据类型，不可变数据类型
不可变数据类型：元组，boor（只有两种状态不可更改），int：数字：本身不可更改 str：不可更改，经过各种才做产生的是新字符串
    不可更改有成为可哈希
可变数据类型：列表list 字典dict 集合set（本身是可变数据类型，但是里面的元素是不可变数据类型） 不可哈希
字典的key必须是不可变数据类型，可哈希，元祖，数字，bool，str
字典的value任意数据类型
dict的优点：二分查找去查询
           存储大量的关系型数据
           特点：无序的3.5包括3.5以前，意味着查找要用键来查找

"""
# dic = {
#     'name': ['大孟', '小孟'],
#     'py9': [{'number': 71, 'avg_age': 18}],
#     True: 1,
#     (1, 2, 3): 'wuyiyi',
#     2: '二哥'
# }
# print(dic)
dic = {'age': 18, 'name': 'jin', 'sex': 'male'}
# 增 只有两种
# dic['high'] = 185  # 没有就添加
# dic['age'] = 16  # 有就覆盖
# dic.setdefault('weight', 150)
# dic.setdefault('name', 'zz')  # 有这个键，就不做任何操作，没有就添加，默认添加none
# print(dic)
# print(dic.pop('age'))  # 有返回值，按键去删除
# dic.pop('二哥', '没有此键')  # 不存在就返回没有此键
# dic.pop('二哥')  # 因为没有这个键，所以报错
# print(dic)
# dic.popitem()  # 随机删除（3.5），没什么意义 返回元组，里面是删除的键值
# print(dic)
# dic.claer()  # 清空字典
# del 也可以删除键值对 del dic['name']没有的会报错 也可以删除字典

# 改 update()将（）里的都更新到前面，有就覆盖，没有就更新
# dic = {'name': 'jin', 'age': 18, 'sex': 'male'}
# dic2 = {'name': 'alex', 'weitht': 75}
# dic2.update(dic)
# print(dic2)
# print(dic)

# 查
dic = {'name': 'jin', 'age': 18, 'sex': 'male'}
# print(dic.keys(), type(dic.keys()))  # 类型是dict_keys
# print(dic.values(), type(dic.values()))  # 类型是dict_value
# print(dic.items(), type(dic.items()))  # 元组 类型是dict_item
#
# for i in dic:
#     print(i)  # 什么都不写默认打印的是键
# for i in dic.keys():
#     print(i)  # 和上面的for一样
# for i in dic.values():
#     print(i)
# 分别赋值
# a, b = 1, 2
# a, b = [1, 2]
# a, b = [1, 2], [2, 3]
# a, b = (1, 2)
# a, b = b, a
# print(a, b)
# for k, v in dic.items():
#     print(k, v)
a = dic['name']  # 如果没有这个键，报错
print(a)
b = dic.get('name1', '没有这个键')  # 没有返回none，和pop（）类似，可以返回么有的时候的提示
print(b)
