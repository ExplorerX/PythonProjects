import socketserver
import json
from core import views
from conf import settings


class MyFTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        # 消息的转发 把任务转给views文件中的对应的方法
        op_str = msg['operation']
        if hasattr(views, op_str):
            func = getattr(views, op_str)
            ret = func(msg)
            self.my_send(ret)

    def my_recv(self):
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        msg = json.loads(msg)
        return msg

    def my_send(self, msg):
        json.dumps(msg).encode(settings.code)
        self.request.send(msg)

