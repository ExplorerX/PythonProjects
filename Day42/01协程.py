# 真正的协程操作就是使用greenlet来完成的
# from greenlet import greenlet
#
#
# def eat():
#     print("Eating start!")
#     g2.switch()
#     print("Playing end!")
#     g2.switch()
#
#
# def play():
#     print("Playing start!")
#     g1.switch()
#     print("Playing end!")
#
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
# g1.switch()

# 使用gevent
# import gevent
# from gevent import monkey;monkey.patch_all()
# import time
#
#
# def eat():
#     print("Eating start!")
#     time.sleep(1)
#     print("Playing end!")
#
#
# def play():
#     print("Playing start!")
#     time.sleep(1)
#     print("Playing end!")
#
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# g1.join()
# g2.join()

# 进程和线程的任务切换由操作系统完成
# 协程任务之间的切换由程序（代码）完成，
# 只有遇到协程模块能识别的IO操作的时候程序才会进行任务切换，实现并发效果

# 同步和异步
# 常用于网络编程socket和爬虫
# from gevent import monkey;monkey.patch_all()
# import time
# import gevent
#
#
# def task():
#     time.sleep(1)
#     print(123445)
#
#
# def sync():
#     for i in range(10):
#         task()
#
#
# def async():
#     g_lst = []
#     for i in range(10):
#         g = gevent.spawn(task)
#         g_lst.append(g)
#     gevent.joinall(g_lst)
#

# sync()
# async()

# 协程：能够在一个线程中实现并发效果的概念
#   能够规避一些任务中的IO操作
#   在任务的执行过程中，检测到IO就切换到其他任务
# 爬虫例子
from gevent import monkey;monkey.patch_all()
from urllib.request import urlopen
import gevent


def get_url(url):
    response = urlopen(url)
    content = response.read().decode()
    return len(content)


g1 = gevent.spawn(get_url, "http://www.baidu.com")
g2 = gevent.spawn(get_url, "http://www.taobao.com")
g3 = gevent.spawn(get_url, "http://www.sogou.com")
g4 = gevent.spawn(get_url, "http://www.hao123.com")
g5 = gevent.spawn(get_url, "http://www.cnblogs.com")
gevent.joinall([g1, g2, g3, g4, g5])
print(g1.value)
print(g2.value)
print(g3.value)
print(g4.value)
print(g5.value)
