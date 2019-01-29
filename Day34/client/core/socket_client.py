import socket
import json


class MySocket:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1', 8080))

    def mysend(self, msg):
        res_json = json.dumps(msg)
        self.sk.send(res_json.encode('utf-8'))

