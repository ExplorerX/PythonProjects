import socket
ss = socket.socket()
ss.connect(('127.0.0.1',8086))
while True:
    send_info = input('>>>')
    ss.send(send_info.encode('utf-8'))
    if send_info == 'bye':
        break
    msg = ss.recv(1024).decode('utf-8')
    print(msg)
    if msg == 'bye':
        break
ss.close()
