import time
import os
from multiprocessing import Process


def func():
    print(os.getpid())
    while True:
        time.sleep(0.5)
        print('我还活着')


def func2():
    print('in func2 start')
    time.sleep(8)
    print('in func2 finished')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  # 设置子进程为守护进程
    p.start()
    p2 = Process(target=func2)
    p2.start()
    p2.terminate()
    print(p2.is_alive())
    time.sleep(2)
    print(p2.is_alive())
    print(p.name)
    # i = 0
    # while i < 5:
    #     print('我是socket server')
    #     time.sleep(1)
    #     i += 1

# 守护进程会随着主进程的代码执行完毕而结束
# 在主进程内结束一个子进程p.terminate()
# 结束一个自己进程不是立刻生效，需要操作系统的调度
# p.name p.pid这个进程的进程名和进程号
# 检验一个进程是否还活着的状态p.is_alive()
