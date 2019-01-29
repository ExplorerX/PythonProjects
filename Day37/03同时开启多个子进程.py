import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*'*arg1)
    time.sleep(3)
    print('*'*arg2)


if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=func, args=(10 * i, 20 * i))
        p_list.append(p)
        p.start()
    [p.join() for i in p_list]
    print('运行完了')
# 确保子进程之间异步执行，但是到了某一个节点的时候要与主进程保持同步
