import random
import time
from multiprocessing import Process, Queue


def consumer(q, name):
    while True:
        food = q.get()
        if food is None:
            print('{}获得了一个空'.format(name))
            break
        print('\33[31m{}消费了{}\33[0m'.format(name, food))
        time.sleep(random.randint(1, 3))


def producer(name, food, q):
    for i in range(4):
        time.sleep(random.randint(1, 3))
        f = '{}生产了{}{}'.format(name, food, i)
        print(f)
        q.put(f)


if __name__ == '__main__':
    q = Queue(20)
    p1 = Process(target=producer, args=('Egon', '包子', q))
    p2 = Process(target=producer, args=('WuSir', '泔水', q))
    c1 = Process(target=consumer, args=(q, 'alex'))
    c2 = Process(target=consumer, args=(q, 'jinboss'))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()  # 检测p1是否停止
    p2.join()  # 检测p2是否停止
    q.put(None)
    q.put(None)
