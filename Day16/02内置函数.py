# 1、reverse和reversed
# li = [1, 2, 3, 4, 5]
# li.reverse()
# l2 = reversed(li)  # l2是返回的一个迭代器
# print(li)
# print(list(l2))
# 保留原来的列表，返回一个反序的迭代器

# 2、slice切片
# l = [1, 2, 3, 4, 5, 6]
# sli = slice(1, 5, 2)  # 生成一个切片规则，至于切谁并不知道
# print(l[sli])  # 等价于 l[1: 5: 2]
# print(l[1: 5: 2])

# 3、format功能之一：对齐方式
# print(format('test', '<20'))
# print(format('test', '>20'))
# print(format('test', '^20'))

# 4、bytes转换成bytes类型
# 我拿到的是gbk编码的，我想转成utf-8编码的
# print(bytes('你好', encoding='gbk').decode('gbk'))
# print(bytes('你好', encoding='utf-8').decode('utf-8'))
# 网络编程，传输数据只能用二进制
# 文件存储 照片和视频也是用二进制存储的
# html网页爬取到的也是byte编码

# 5、bytearray
# bys = bytearray('你好', encoding='utf-8')
# print(bys[0])

# 6、memoryview 切片——字节类型，不占内存，转换成字节不占，但是转成字符串之后有要占内存


# 7、sorted
l = ['     ', [1, 2], 'hello world']
li = sorted(l, key = len)
print(li)
