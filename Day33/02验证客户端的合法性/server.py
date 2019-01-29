import socket
import hmac
import os
secret_key = b'egg'
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def check_conn(conn):
    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(secret_key, msg)
    digest = h.digest()
    client_digest = conn.recv(1024)
    return hmac.compare_digest(digest, client_digest)


conn, addr = sk.accept()
res = check_conn(conn)
if res:
    print('合法的客户端')
    conn.close()
else:
    print('不合法的客户端')
    conn.close()
sk.close()
