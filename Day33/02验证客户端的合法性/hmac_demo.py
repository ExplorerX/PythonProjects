# import hmac
# h = hmac.new()  # secret_key,你想进行加密的bytes
# 密文 = h.digest()
# hmac.compare_digest()  # 对比 密文和另外一个密文
import os
print(os.urandom(32))  # 随机生成32字节
