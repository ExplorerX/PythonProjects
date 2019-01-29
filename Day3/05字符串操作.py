# # 字符串操作
# # 首字母大写
# s = 'zhang zheng546.'
# s1 = s.capitalize()
# print(s1)
# # 转成大写 对数字没有影响
# s2 = s.upper()
# print(s2)
# # 转成小写 对数字没有影响
# s2 = 'aSdFgHjKl1223.'
# s3 = s2.lower()
# print(s3)
# # 大小写反转
# s1 = 'aSdFgHjKl1223.'
# s4 = s1.swapcase()
# print(s4)
# # 隔开的首字母大写,特殊符号包括数字
# s = 'i@!love#china'  # 特殊字符隔开也可以
# s5 = s.title()
# print(s5)
# # 居中
# s = 'asdfghjkl'
# s5 = s.center(20, '#')  # #####asdfghjkl######
# print(s5)
# # 将tab用一个字节补齐
# s = 'as\tdfgh\tjkl'
# s6 = s.expandtabs()
# print(s6)
# # 公共方法 len()
# s = 'asdfghjkl你好'
# l = len(s)
# print(l)
# s = 'alexWuSir'
# s7 = s.startswith('al')  # startswith(self, prefix, start=None, end=None)后面的为切片
# find方法 找不到返回-1
# s = 'alexWuWSiWr'
# s8 = s.index('z')
# print(s8)
# index方法  找不到报错
# s.startswith('')
# s.endswith()
# 去前后空格，默认为空格 strip(), lstrip(), rstrip()
# s = '  i love you '
# s9 = s.strip()
# print(s9)
# s = '!i love you$ '
# s10 = s.strip('$! ')
# print(s10)
# s = 'alexUsidssidskjljls'
# s11 = s.count('s')
# print(s11)
# s = 'l#love!you'
# s12 = s.split('#')
# print(s12)
# format的三种用法，格式化输出
res = '{} {} {}'.format('egon', 18, 'male')
print(res)
res = '{1} {0} {1}'.format('egon', 18, 'male')
print(res)
res = '{name} {age} {sex}'.format(sex='male', name='egon', age=18)
print(res)
# replace
# s = '阿斯蒂芬规划局快乐阿三大地飞歌阿斯蒂芬'
# s13 = s.replace('阿', 'a', 2)
# print(s13)
# is系列
# s = 'zhang6882051'
# s14 = s.isalpha()
# s15 = s.isdigit()
# s16 = s.isalnum()
# s17 = s.isdecimal()
# print(s14)
# print(s15)
# print(s16)
# print(s17)

# for循环
s = 'asadflasdhjfl'
for i in s:
    print(i)
#
# # in关键字
if 'sad' in s:
    print('存在sad')
