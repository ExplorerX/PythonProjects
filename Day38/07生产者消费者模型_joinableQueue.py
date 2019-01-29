import random
import time
from multiprocessing import Process, JoinableQueue


def consumer(q, name):
    while True:
        food = q.get()
        print('\33[31m{}消费了{}\33[0m'.format(name, food))
        time.sleep(random.randint(1, 3))
        q.task_done()


def producer(name, food, q):
    for i in range(4):
        time.sleep(random.randint(1, 2))
        f = '{}生产了{}{}'.format(name, food, i)
        print(f)
        q.put(f)
    q.join()  # 阻塞，直到一个队列中的所有数据全部被处理完毕


if __name__ == '__main__':
    q = JoinableQueue(20)
    p1 = Process(target=producer, args=('Egon', '包子', q))
    p2 = Process(target=producer, args=('WuSir', '泔水', q))
    c1 = Process(target=consumer, args=(q, 'alex'))
    c2 = Process(target=consumer, args=(q, 'jinboss'))
    p1.start()
    p2.start()
    c1.daemon = True  # 设置为守护进程，主进程中的代码执行完毕之后，子进程自动结束
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()  # 检测p1是否停止
    p2.join()  # 检测p2是否停止

# 在消费者这一端
#   每次获取一个数据
#   处理一个数据
#   发送一个信号，表示这一个数据处理成功

# 在生产者这一端
#   每一次生产一个数据
#   且每一次生产的数据都放在队列中
#   当生产者全部生产完毕之后
#   join信号：已经停止生产数据了
#       且要等待之前被刻上记号都被消费掉
#       当数据都被处理完时，join阻塞结束

# consumer中把所有任务消耗完
# producer端的join感知到，停止阻塞
# 主进程中的p.join结束
# 主进程中的代码结束
# 守护进程(消费者的进程)结束
