import json
from core.socket_client import MySocket


class Auth:
    __instance = None

    def __new__(cls, *args, **kwargs):  # 单例模式
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.socket = MySocket()
        self.username = None
    
    def login(self):
        username = input('username:')
        pwd = input('password:')
        if username.strip() and pwd.strip():
            # send
            self.socket.mysend({'username': 'alex', 'pwd': 'alex3714', 'operation': 'login'})
        ret = self.socket.sk.recv(1024)  # 登录结果

    def register(self):
        username = input('username:')
        pwd = input('password:')
        pwe2 = input('password_ensure:')
        if username.strip() and pwd.strip():
            self.socket.mysend({'username': 'alex', 'pwd': 'alex3714', 'operation': 'register'})
        ret = self.socket.sk.recv(1024)  # 注册结果
