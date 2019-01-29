# 进程与进程之间
# 几个进程之间，不通过特殊的手段是不能共享一个数据的
import os
from multiprocessing import Process


def func():
    global n  # 申明一个全局变量
    n = 0  # 对这个全局变量进行赋值
    print('pid: {}'.format(os.getpid()), n)


if __name__ == '__main__':
    n = 100
    p = Process(target=func)
    p.start()
    p.join()
    print(os.getpid(), n)
