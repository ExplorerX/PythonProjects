# 模拟10个人抢一张票的情况
# import json
# import time
# from multiprocessing import Process
#
#
# def show(i):
#     with open('ticket') as f:
#         dic = json.load(f)
#     print('余票：{}'.format(dic['ticket']))
#
#
# def buy_ticket(i):
#     with open('ticket') as f:
#         dic = json.load(f)
#         time.sleep(0.1)
#     if dic['ticket'] > 0:
#         dic['ticket'] -= 1
#         print('\033[32m{}买到票了\033[0m'.format(i))
#     else:
#         print('\033[31m{}买到票了\033[0m'.format(i))
#     time.sleep(0.1)
#     with open('ticket', 'w') as f:
#         json.dump(dic, f)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=show, args=(i, ))
#         p.start()
#     for i in range(10):
#         p = Process(target=buy_ticket, args=(i, ))
#         p.start()

# 结果为
# 余票：1
# 余票：1
# 余票：1
# 余票：1
# 余票：1
# 2买到票了
# 1买到票了
# 3买到票了
# 4买到票了
# 0买到票了


# 进程锁，使得写文件的时候锁住
# 模拟一个同步的过程
import json
import time
from multiprocessing import Process
from multiprocessing import Lock


def show(i):
    with open('ticket') as f:
        dic = json.load(f)
    print('余票：{}'.format(dic['ticket']))


def buy_ticket(i, lock):
    lock.acquire()
    with open('ticket') as f:
        dic = json.load(f)
        time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print('\033[32m{}买到票了\033[0m'.format(i))
    else:
        print('\033[31m{}没买到票\033[0m'.format(i))
    time.sleep(0.1)
    with open('ticket', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=show, args=(i, ))
        p.start()
    lock = Lock()
    for i in range(5):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()
