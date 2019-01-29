# join对于可迭代对象都可以操作
# s = ['alex', 'egon']
# s1 = '_'.join(s)
# print(s1)
# 列表转字符串：join
# 字符串转列表：spilt
# range() 数字按顺序排列的列表，从0开始0可以不用写range(10),可以有步长range(0, 10, 3)
# for i in range(0, 10, 3):
#     print(i)
# for i in range(10, 0, -3):
#     print(i)
# for i in range(0, 10, -1):
#     print(i)
li = [1, 2, 3, 5, 'alex', [2, 3, 4, 5, 'taibai'], 'afds']
for i in li:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)
for i in range(len(li)):
    if type(li[i]) == list:
        for j in li[i]:
            print(j)
    else:
        print(li[i])
