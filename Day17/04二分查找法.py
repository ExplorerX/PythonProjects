# 什么叫算法
# 计算的方法：人脑复杂，计算机简单

# 查找
# 排序
# 遍历问题
# 最短路径问题

# 我们学习的算法都是过去式
# 了解基础的算法，才能创造出更好的算法
# 不是所有的事情都能套用现成的方法解决的
# 有些时候会用到学过的算法知识来解决问题


# 二分查找 必须处理有序列表
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100]


def find(l, aim):
    start = 0
    end = len(li) - 1
    mid = int((start + end) / 2)
    while li[mid] != aim and start <= end:
        if li[mid] > aim:
            end = mid - 1
            mid = int((start + end) / 2)
        else:
            start = mid + 1
            mid = int((start + end) / 2)
    return mid


res = find(li, 7)
print(res)
