from multiprocessing import Event
# 一个信号可以使所有的进程都进入阻塞状态
# 也可以控制所有的进程解除阻塞
# 一个事件被创建之后，默认是阻塞状态
e = Event()  # 创建一个事件
print(e.is_set())  # 查看一个事件的状态，默认被设置成阻塞
# e.wait()  # 依据e.is_set()的值来决定是否阻塞的
print('Hello, World!')
e.set()
print(e.is_set())
e.wait()
print('Hello, World!')
e.clear()  # 将这个事件的状态改为False
print(e.is_set())
e.wait()
print('Hello, World!')

# set和clear分别用来修改一个事件的状态True和False
# is_set用来查看一个事件的状态
# wait 是依据is_set()来决定自己是否阻塞
# False阻塞，True不阻塞
