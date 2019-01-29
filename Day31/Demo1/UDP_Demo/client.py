import socket
ss = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8086)
while True:
    info = input('>>>').encode('utf-8')
    ss.sendto(info, ip_port)
    msg, addr = ss.recvfrom(1024)
    msg = msg.decode('utf-8')
    print(msg)
