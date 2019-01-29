

def qqxing(l = []):
    l.append(1)
    print(l)


qqxing()
qqxing([])
qqxing()
qqxing()
# 如果默认参数的数据类型是一个可变的数据类型，在你每次不传参数调用的时候相当于共享这个变量的资源
