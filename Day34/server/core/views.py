import os
from core.user import User
from conf import settings
import pickle


def login(msg):
    print(msg)


def register(msg):
    # username, password
    # 创建一个属于这个用户的家目录
    # 把用户名密码写进userinfo文件里，记录用户名
    # 记录用户的初始磁盘配额，并记录下来
    # 记录文件大小
    # 记录用户当前所在的目录
    user_obj = User(msg['username'])  # 记录用户的信息在内存里
    pickle_path = os.path.join(settings.pickle_path, msg['username'])
    with open(pickle_path, 'wb') as f:
        pickle.dump(user_obj, f)
    os.mkdir(user_obj.home)  # 创建一个属于这个用户的对象
    with open(settings.user_info, 'a') as f:
        f.write('%s|%s|%s' % (msg['username'], msg['pwd'], pickle_path))
    return True


def upload(msg):
    print(msg)


def download(msg):
    print(msg)
