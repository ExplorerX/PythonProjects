import os
import sys
import socketserver
sys.path.append(os.path.dirname(os.getcwd()))

from core.server import MyFTPServer
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyFTPServer)
    server.serve_forever()
