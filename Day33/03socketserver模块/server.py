# socket tcp使用socket启动一个tcp服务只能与一个客户端建立通信
# 如果用socketserver就可以实时和多个客户端一起通信
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):  # self.request相当于conn
        msg = self.request.recv(1024).decode('utf-8')
        if msg == 'q':
            return
        print(msg)
        info = input('>>>')
        self.request.send(info.encode('utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    # thread 线程
    server.serve_forever()
    # 永远起一个服务

# 第一：多个类之间的继承关系要先整理
# 每一个类中有哪些方法，要大致列出来
# 所有的self对象的调用要清楚的了解是谁的对象
# 所有的方法调用要退回到最子类的类中开始寻找，逐级向上

