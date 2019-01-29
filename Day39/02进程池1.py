import time
from multiprocessing import Pool, Process


def func(n):
    for item in range(10):
        print(n + 1)


if __name__ == '__main__':
    start = time.time()
    pool = Pool(5)
    # 进程池中常驻5个进程
    pool.map(func, range(100))
    # 开启100个任务map()方法中的第一个参数func为执行的方法名称，第二个参数是一个可迭代对象，用于给func传递参数
    t1 = time.time() - start
    start = time.time()
    p_lst = []
    for item in range(100):
        p = Process(target=func, args=(item, ))
        p_lst.append(p)
        p.start()
    for p in p_lst:
        p.join()
    t2 = time.time() - start
    print(t1, t2)  # 0.9360015392303467 2.9972054958343506
    # 通过时间的对比发现进程池的执行效率是要更高的
