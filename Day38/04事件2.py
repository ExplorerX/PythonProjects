# 红绿灯模型
import time
import random
from multiprocessing import Event, Process


def cars(e, i):
    if not e.is_set():
        print('car{}在等待'.format(i))
        e.wait()  # 阻塞，直到得到一个事件状态变成True的信号
    print('\33[0;31;40m car{}通过了\33[0m'.format(i))


def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\33[31m红灯亮了\33[0m')
        else:
            e.set()
            print('\33[32m绿灯亮了\33[0m')
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e, ))
    traffic.start()
    for i in range(20):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())
