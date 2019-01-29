# 给定一下列表li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# 将所有大于66的值保存至字典的第一个key中，将小于66的值保存
# 值字典的第二个key中 即：{'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# dic = {}
# list_less = []
# list_more = []
# for i in li:
#     if i > 66:
#         list_more.append(i)
#     elif i < 66:
#         list_less.append(i)
# dic.setdefault('k1', list_more)
# dic.setdefault('k2', list_less)
# print(dic)
"""
输出商品列表，用户输入序号，显示用户选中的商品
商品：li = ['手机', '电脑', '鼠标垫', '游艇']
要求：1：页面显示 序号+商品名称，如：
    1 手机
    2 电脑
    。。。
      2：用户输入选择的商品序号，然后打印商品名称
      3：如果用户输入的商品序号有误，则提示出入有误，并重新输入
      4：用户输入Q或者q，退出程序
"""
li = ['手机', '电脑', '鼠标垫', '游艇']
sign = 1
dic = {}
flag = False
for i in li:
    print(sign, i)
    dic.setdefault(sign, i)
    sign += 1
while 1:
    sign = input('请输入商品序号：')
    if sign.upper() == 'Q':
        break
    elif sign.isdigit():
        for i in dic.keys():
            if int(sign) == i:
                print(dic[i])
                flag = True
                break
    else:
        flag = False
    if flag:
        pass
    else:
        print('Input error, please input again!')
        flag = False
