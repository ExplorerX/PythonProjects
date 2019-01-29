import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*'*arg1)
    time.sleep(3)
    print('*'*arg2)


if __name__ == '__main__':
    p = Process(target=func, args=(10, 20))
    p.start()
    # p.join()  # 感知一个子进程的结束，将异步的程序变成同步
    print('=======,运行完了')
