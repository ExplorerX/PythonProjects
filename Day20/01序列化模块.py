# 序列化 -- 转向一个字符串数据类型
# 序列 -- 字符串

# 从数据类型到字符串的过程：序列化
# 从字符串到数据类型的过程：反序列化

# json *****
# pickle ****
# shelve python3新增的序列化方式，比较好操作 ***

# json通用的序列化格式
#   只有很少的一部分数据类型能够通过json转化成字符串

# pickle
#   所有的python中的数据类型都可以转换成字符串
#   pickle序列化的内容只有python能理解
#   且部分反序列化依赖代码

# shelve
#   序列化句柄
#   使用句柄直接操作，非常方便

# dumps:序列化方法
# loads：反序列化方法
# import json
# dic = {'k1': 'v1'}
# str_d = json.dumps(dic)  # 序列化
# print(dic, type(dic))
# print(str_d, type(str_d))
# dic_d = json.loads(str_d)
# print(dic_d, type(dic_d))
# 数字，字符串，列表，字典，元组(转换成列表进行序列化)

# dump和load：和文件相关的操作
# import json
# dic = {'k1': 'v1'}
# f = open('fff', 'w', encoding='utf-8')
# json.dump(dic, f)
# f.close()
# f = open('fff')
# res = json.load(f)
# f.close()
# print(type(res), res)

# dic = {'k1': 'v1', 'k2': '中国'}
# f = open('fff', 'w', encoding='utf-8')
# json.dump(dic, f, ensure_ascii=False)
# f.close()
# f = open('fff', encoding='utf-8')
# res = json.load(f)
# f.close()
# print(type(res), res)

# json只能实现一次写入和一次读出，如果要分多次写入和读出来
# import json
# li = [{'k1': '111'}, {'k2': '222'}, {'k3': '333'}]
# f = open('file', 'w', encoding='utf-8')
# for dic in li:
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')
# f.close()
# f = open('file')
# for i in f:
#     dic = i.strip()
#     print(json.loads(dic))

# pickle也有四种方法
# 序列化之后使用的是bytes类型，但是不影响反序列化之后的效果
# load和dump需要使用bytes类型的文件打开方式
# 对于pickle任何数据类型都可以序列化
# 而且可以分布的dump和load但是json不可以
# 但是pickle只在python中可以使用

# shelve
# import shelve
# # f = shelve.open('shelve_file')
# # f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
# # f.close()
# #
# # f1 = shelve.open('shelve_file')
# # existing = f1['key']  # 取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# # f1.close()
# # print(existing)


# 由于shelve在默认情况下是不会记录待持久化对象的任何修改的，所以我们在shelve.open()时候需要修改默认参数，否则对象的修改不会保存。
# import shelve
# f1 = shelve.open('shelve_file')
# print(f1['key'])
# f1['key']['new_value'] = 'this was not here before'
# f1.close()
#
# f2 = shelve.open('shelve_file', writeback=True)
# print(f2['key'])
# f2['key']['new_value'] = 'this was not here before'
# f2.close()
