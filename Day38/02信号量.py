import time
import random
from multiprocessing import Process
from multiprocessing import Semaphore


def ktv(i, sem):
    sem.acquire()  # 取一把钥匙
    print('进程{}进入ktv'.format(i))
    time.sleep(random.randint(3, 6))
    print('进程{}走出ktv了啦'.format(i))
    sem.release()  # 还钥匙


if __name__ == '__main__':
    sem = Semaphore(4)  # 设置有4把钥匙的一个锁
    for i in range(10):
        p = Process(target=ktv, args=(i, sem))
        p.start()
