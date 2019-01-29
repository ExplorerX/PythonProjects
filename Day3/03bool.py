# bool 只有True和False
# int -> str
i = 1
s = str(i)
print(s)
# str -> int
s = '123'
i = int(s)
print(i)
# int -> bool
i = 3
b = bool(i)
print(b)
# bool -> int
i = True
b = int(i)
print(b)
# str -> bool 空字符串转换成bool就是false,非空都是true,可以把字符串作为条件使用
s = 'a'
b = bool(s)
print(b)
