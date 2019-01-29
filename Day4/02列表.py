# li = ['alex', [1, 2, 3], 'Wusir', 'egon', '女神', 'taibai']
# l1 = li[0]
# print(l1)
# l2 = li[1]
# print(l2)
# l3 = li[0:3]
# print(l3)

# 列表的常用操作：增删改查
li = list(['alex', [1, 2, 3], 'Wusir', 'egon', '女神', 'taibai'])
# 列表的追加
# li.append('日天')
# li.append(26)
# print(li)
#
# flag = ''
# while flag != 'g':
#     print('Please input append data:')
#     data = input()
#     li.append(data)
#     flag = input('Please input flag:')
# print(li)
# 插入
# li.insert(4, '春哥')
# print(li)
# li.extend([1, 2, 3])
# # li.extend(li)
# # print(li)
# 删
# pop()默认删除最后一个，按照索引进行删除
# print(li.pop(0))
# print(li)
# 按元素删除 remove()没有返回值
# li.remove('taibai')
# print(li)
# 清空列表
# li.clear()
# print(li)
# 删除列表
# del li
# print(li)
# 切片去删除
# del li[0:2]
# print(li)

# 改
# 按索引改
# li[5] = '难受'
# print(li)
# li[2:4] = ['第三个', '第四个']  # 迭代
# print(li)

# 查
# for i in li[0:2]:
#     print(i)

# 公共方法
# l = len(li)
# print(l)
# l = li.count('taibai')
# print(l)
# l = li.index('taibai')
# print(l)

# 排序 正向排序sort(),反向排序sort(reverse=True) 反转函数：reverse()
li = [1, 7, 75, 4, 90, 34]
li.sort(reverse=True)
li.reverse()
print(li)
