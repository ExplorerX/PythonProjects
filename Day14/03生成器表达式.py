egg_li = ['鸡蛋%d' % i for i in range(10)]  # 列表推导式
print(egg_li)  # 相当于如下代码：

egg_li = []
for i in range(10):
    egg_li.append('鸡蛋%d' % i)
print(egg_li)

g = ('鸡蛋%d' % i for i in range(10))  # 生成器表达式
for i in g:
    print(i)
