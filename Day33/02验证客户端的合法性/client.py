import socket
import hmac
secret_key = b'eggaa'
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
msg = sk.recv(1024)
h = hmac.new(secret_key, msg)
digest = h.digest()
sk.send(digest)
sk.close()

