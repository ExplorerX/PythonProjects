import os
import time
from multiprocessing import Pool


def func(n):
    print('start func{}'.format(n), os.getpid())
    time.sleep(1)
    print('end func{}'.format(n), os.getpid())


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        p.apply_async(func, args=(i, ))
        # apply_async是进程池中的一个真异步方法，它保证主进程和其他子进程之间没有先后结束关系，主进程在执行完代码之后直接结束
    p.close()
    # 为了在主进程中观察到其他子进程中的结果，使用join方法，但是首先得告诉进程池这个进程池中不会在接到新的任务
    # 使用p.close()来实现这一点，结束进程池接受任务
    p.join()
    # 感知进程池中的进程执行完正在执行的任务
