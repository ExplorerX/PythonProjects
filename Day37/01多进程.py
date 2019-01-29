import os
from multiprocessing import Process


def func(arg1, arg2):
    print(arg1, arg2)
    print('子进程：', os.getpid())
    print('子进程的父进程：', os.getppid())


if __name__ == '__main__':
    p = Process(target=func, args=('参数', '参数2'))  # 注册 执行带参数的函数
    # p是一个进程对象，还没有启动进程
    p.start()  # 启动一个子进程：操作系统创建一个进程，执行新进程中的代码
    print('*'*10)
    print('父进程：', os.getpid())
    print('父进程的父进程：', os.getppid())

# 进程的生命周期：
#   主进程
#   子进程
#   开启了子进程的主进程：
#       主进程自己的代码如果长，等待自己的代码执行结束
#       子进程的执行时间长，主进程会在主进程代码执行完毕之后等待子进程执行完毕之后主进程才结束

