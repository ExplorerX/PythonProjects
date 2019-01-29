"""
问题：
    需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N，
    这会导致出现“分解的值过多的错误”(too many values to unpack)的异常
解决方案：
    *表达式
"""


def avg(num):
    length = len(num)
    sum = 0
    if length != 0:
        for i in num:
            sum += i
        return sum / length
    else:
        return


def drop_first_last(grades):
    first, *middle, last = grades  # middle返回的是一个列表，保存着除去第一个和最后一个的剩下的元素
    return avg(middle), middle


numbers = [1, 2, 3, 4, 5, 6, 778, 89]
avg, middle = drop_first_last(numbers)
print(avg)
print(middle)
# 分解之后想要丢弃，使用*_
record = ('ACME', 50, 124.56, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
