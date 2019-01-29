import socket
ss = socket.socket(type=socket.SOCK_DGRAM)
ss.bind(('127.0.0.1', 8086))
while True:
    msg, addr = ss.recvfrom(1024)
    print(msg.decode('utf-8'))
    info = input('>>>').encode('utf-8')
    ss.sendto(info, addr)
