# 问题：
# 我们有一个包含N个元素的元组或者序列(可迭代对象)，现在想将它们分解为N个单独的变量
# 解决方案：
# 简单的复制操作就可以做到
# 使用范围：只要对象是可迭代的就可以使用：字符串，迭代器，生成器等都可以

# 元组
p = (4, 5)
x, y = p
print(x, y)

# 列表
data = ['ACME', 50, 91.1, [2012, 12, 21]]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, mon, day) = data
print(year)

# 如果我只想取特定的：
_, shares, price, _ = data
print(shares)
print(_)
