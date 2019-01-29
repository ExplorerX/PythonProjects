import socket
ss = socket.socket()
ss.bind(('127.0.0.1', 8086))
ss.listen()
conn, addr = ss.accept()
print(addr)
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
    info = input('>>>')
    conn.send(bytes(info, encoding='utf-8'))
conn.close()
ss.close()

