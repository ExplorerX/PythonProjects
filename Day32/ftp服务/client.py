import json
import socket
import struct
import os
sk = socket.socket()
sk.connect(('127.0.0.1', 8090))
buffer = 512
head = {'filepath': r'F:\Python第九期\第一部分\day32',
        'filename': r'07 python fullstack s9day32 关于ftp文件传输的报错.mp4',
        'filesize': None}
file_path = os.path.join(head['filepath'], head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
json_head = json.dumps(head)
bytes_head = json_head.encode('utf-8')
head_len = len(bytes_head)
pack_len = struct.pack('i', head_len)
sk.send(pack_len)
sk.send(bytes_head)
with open(file_path, 'rb') as f:
    while filesize:
        if filesize >= buffer:
            content = f.read(buffer)
            sk.send(content)
            filesize -= buffer
        else:
            f.read(filesize)
            sk.send(content)
            break
sk.close()

