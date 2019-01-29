# 格式化输出
name = input('请输入姓名:')
age = input('请输入年龄:')
height = input('请输入身高:')
msg = '我叫%s,我今年%s岁,我身高%scm,学习进度3%%' % (name, age, height)
# %为占位符 s为str d为数字digital 
# 格式化输出的时候如果要输出百分号%这个符号，使用%%，在前面先使用一个%对后面的%进行转义
print(msg)
