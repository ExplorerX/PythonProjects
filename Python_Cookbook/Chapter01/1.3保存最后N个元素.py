# 问题：
# 我们希望在迭代或者是其他形式的处理过程中对最后几项记录做一个有限的历史记录统计
# 解决方案：
# 使用collections.deque
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example us on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevline in search(f, 'python', 5):
            for pline in prevline:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# deque是一个双向队列
# deque(maxlen = N)创建了一个固定长度的队列
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)
q.appendleft(5)
print(q)  # deque([5, 2, 3], maxlen=3)
q.pop()
print(q)  # deque([5, 2], maxlen=3)
q.popleft()
print(q)  # deque([2], maxlen=3)
