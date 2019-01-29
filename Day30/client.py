import socket
ss = socket.socket()
ss.connect(('127.0.0.1', 8086))
while True:
    ret = bytes(input('>>>'), encoding='utf-8')
    ss.send(ret)
    info = ss.recv(1024).decode('utf-8')
    print(info)
    if info == 'bye':
        ss.send(b'bye')
        break
ss.close()
