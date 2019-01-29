"""
小知识点总结：

=赋值  ==  比较值是否相等  is  比较的是内存地址  id()获取变量的内存地址

数字，字符串 都是用的是小数据池，意思就是在一定范围内的数字和字符串使用相同的地址。目的是在一定程度上节省内存
数字的范围：-5——256
字符串的规律：1、不能有特殊字符，如果没有特殊字符使用的就是同一块内存
             2、s*20还是同一块内存，s*21及以后就是两块内存了 s为一个字符
剩下的list dict  tuple set都没有小数据池的概念

ASCII使用8位表示
Unicode使用32位
utf-8使用24位
gbk使用16个字节
1、各个编码之间的二进制，是不能相互识别的，会产生乱码
2、文件的存储，传输，不能是Unicode，只能是utf-8，gbk,ascii,utf-16 gb2312

在python3中
    str在内存中使用Unicode编码
    bytes类型：不是以unico编码
    传输过程中只能以字节的形式传送,所以要把str转换成字节进行传输
str：
内存中式用Unicode编码
bytes类型
对于英文：
str：表现形式：s = 'zhangzheng'
     编码方式：00101001010101 unicode
     bytes：表现形式： s = b'zhangzheng'
            编码方式：01010101010 utf-8 gbk
对于中文：
str:表现形式：s = '中国'
    编码方式：unicode
bytes：表现形式：b'\xe4\xb8\xad\xe5\x9b\xbd'
       编码方式：utf-8 gbk
"""
# 编码：
# 将英文转化成字节
s = '中国'
s1 = s.encode('utf-8')
print(s1)
