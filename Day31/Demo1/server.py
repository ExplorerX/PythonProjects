import socket
# tcp协议
ss = socket.socket()
ss.bind(('127.0.0.1', 8086))
ss.listen()
conn, addr = ss.accept()  # 已经完成了三次握手，建立了一个连接
# 阻塞
while True:
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    if msg == 'bye':
        break
    send_info = input('>>>')
    conn.send(send_info.encode('utf-8'))
    if send_info == 'bye':
        break
conn.close()
ss.close()
