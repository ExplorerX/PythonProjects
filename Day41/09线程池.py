import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    # time.sleep(2)
    print(n)
    return n ** 2


t_pool = ThreadPoolExecutor(max_workers=5)
t_lst = []
for i in range(20):
    t = t_pool.submit(func, i)
    t_lst.append(t)
t_pool.shutdown()
print("主线程")
for t in t_lst:
    print("***", t.result())
