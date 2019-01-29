# 计算器
# re模块
# 正则表达式 —— 字符串匹配
# 学习正则表达式
# 学习使用re模块来操作正则表达式

# re模块的常用方法：
# findall
# finditer
# search
# match
# import re
# findall：返回所有满足匹配条件的结果，放在列表里
# search：从前往后，找到一个就返回，返回的变量需要调用group()方法才能拿到结果
#   如果没有找到，那么返回None，调用group会报错
# match：match是从头开始匹配的，如果正则规则从头开始可以匹配上，就返回一个对象
# 没有匹配上，就返回None，调用group就会报错
# ret = re.findall('[a-z]+', 'eva egon yuanhao')
# print(ret)
# ret = re.search('[a-z]+', 'eva egon yuanhao')
# print(ret.group())
# ret = re.match('e', 'eva egon yuanhao')
# print(ret.group())
# import re
# ret = re.finditer('\d', 'ds3sy4784a')   # finditer返回一个存放匹配结果的迭代器
# print(ret)  # <callable_iterator object at 0x10195f940>
# print(next(ret).group())  # 查看第一个结果
# print(next(ret).group())  # 查看第二个结果
# print([i.group() for i in ret])  # 查看剩余的左右结果
# 注意事项：
# import re
# ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可
#
# ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
# print(ret)  # ['www.oldboy.com']

# ret=re.split("\d+","eva3egon4yuan")
# print(ret) #结果 ： ['eva', 'egon', 'yuan']
#
# ret=re.split("(\d+)","eva3egon4yuan")
# print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']
#
# 在匹配部分加上（）之后所切出的结果是不同的，
# 没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
# 这个在某些需要保留匹配部分的使用过程是非常重要的。


# 在同一个位置可能出现的各种字符组成了一个字符组，在正则表达式中用[]表示
# [0-9]匹配这个位置是不是数字
# [a-z]匹配这个位置是不是小写字母
# [A-Z]匹配这个位置是不是大写字母
# 可以混着使用[0-9a]匹配这个位置是不是数字或者a
# [0-9a-zA-Z]匹配是不是数字和英文字母

# 元字符
"""
.:匹配除换行符以外的任意字符
\w:匹配字母或者数字或者下划线 word
\s:匹配任意的空白符 space
\d:匹配数字 digit
\W:匹配非字母或数字或下划线
\S:匹配非空白符
\D:匹配非数字
\n:匹配一个换行符
\t:匹配一个制表符
\b:匹配一个单词的结尾
^:匹配字符串的开始
$:匹配字符串的结尾
a|b:匹配字符a或b |表示或者关系
():匹配括号内的表达式，也表示一个组
[...]：匹配字符组中的字符
[^...]:匹配非字符组中字符的所有字符
"""
# 量词
"""
*:重复零次或多次
?:重复零次或一次
+:重复一次或多次
{n}:重复n次
{n,}:重复n次或更多次
{n,m}:重复n次到m次
"""

# 转义符\ 在python中使用r'字符串'来表示对这一个字符串里面的内容进行全部原样
print(r'\d\dsdfa\adasdf\\\\\sadfsadfasd\\\\ssse')

# 贪婪匹配：在满足匹配时，匹配尽可能长的字符串，默认情况下，采用贪婪匹配
# *? 重复任意次，但尽可能少重复
# +? 重复1次或更多次，但尽可能少重复
# ?? 重复0次或1次，但尽可能少重复
# {n,m}? 重复n到m次，但尽可能少重复
# {n,}? 重复n次以上，但尽可能少重复
# .*?x
# 就是取前面任意长度的字符，直到一个x出现
