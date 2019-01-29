# 相对路径
# f = open('模特主妇护士班主任.txt', mode='r', encoding='utf-8')
# content = f.read()
# print(content, type(content))  # bytes ---> str python中str用的是unicode编码，read方法隐藏的的实现了一步编码方式的转换
# f.close()
# f = open('模特主妇护士班主任.txt', mode='rb')
# content = f.read()
# print(content)
# f.close()
# 上面的代码有什么用？
# 非文字类的文件；上传下载

# 对于w：没有此文件就会创建文件
# f = open('log.txt', mode='w', encoding='utf-8')
# f.write("萨达撒把斯巴达三等功撒旦法")
# f.close()
# 有文件把源文件的内容全部清除，在写入
# f = open('log.txt', mode='w', encoding='utf-8')
# f.write("白色的如火如荼会让你更还叫人套近乎")
# f.close()

# f = open('log.txt', mode='wb')
# f.write("萨达撒把斯巴达三等功撒旦法".encode('utf-8'))  # str  --> bytes
# f.close()

# 追加
# f = open('log.txt', mode='a', encoding='utf-8')
# f.write("海贼王")
# f.close()
#
# f = open('log.txt', mode='ab')
# f.write("热血无赖".encode('utf-8'))
# f.close()

# 读写
# f = open('log.txt', mode='r+', encoding='utf-8')
# print(f.read())
# f.write('中华小当家')
# f.close()
# f = open('log.txt', mode='r+b')
# print(f.read().decode(encoding='utf-8'))
# f.write('女神异闻录'.encode('utf-8'))
# f.close()
# 写读
# f = open('log.txt', mode='w+', encoding='utf-8')
# f.write('中华一番')
# print(f.tell())
# f.seek(0)
# print(f.read())
# f = open('log.txt', mode='w+b')
# f.write('中华一番'.encode('utf-8'))
# print(f.tell())
# f.seek(0)
# print(f.read().decode(encoding='utf-8'))
# 追加再读
f = open('log.txt', mode='a+', encoding='utf-8')
print(f.tell())
f.seek(0)
f.write('女神异闻录')
f.seek(0)
content = f.read()
print(content)
f.close()
