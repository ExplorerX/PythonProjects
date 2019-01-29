# 字符串的索引和切片
s = 'ASDFGHJKL'
# 索引
s1 = s[0]
print(s1)
s2 = s[4]
print(s2)
s4 = s[-1]
print(s4)
s5 = s[-2]
print(s5)
# 切片 顾头不顾尾
s3 = s[0:3]
print(s3)
s6 = s[0:]    # ASDFGHJKL
print(s6)
str
s7 = s[:]  # ASDFGHJKL
print(s7)
s8 = s[0:-1]  # ASDFGHJK
print(s8)
# 步长 [首:尾:步长]
s9 = s[0:5:2]
print(s9)
s10 = s[3:0:-1]  # FDS
print(s10)
s11 = s[3::-1]  # FDSA
print(s11)
s12 = s[::-1]
print(s12)
