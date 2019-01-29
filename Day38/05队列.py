from multiprocessing import Queue, Process


def produce(q):
    q.put('hello')


def consume(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=produce, args=(q,))
    p.start()
    c = Process(target=consume, args=(q,))
    c.start()

# 使用队列实现和两个进程之间的通信，在队列中的每一个元素又可以看成有一个锁
# 会在有一个进程访问的时候防止其他进程访问，有效保护数据
