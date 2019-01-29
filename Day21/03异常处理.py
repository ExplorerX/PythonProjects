try:
    ret = int(input('number>>>'))
    print(ret * '*')
except Exception:
    print('Input error, please input a number!')
else:
    print('*********')
finally:
    print('=========')
# 使用try和except就能处理异常
#   try是我们需要处理的代码
#   except后面跟一个错误类型，当代码发生错误且错误类型符合的时候就会执行except中的代码
# except可以有多个分支
# 万能异常：Exception
# 有了万能的处理机制，仍然要把能预测到的问题单独处理
# 单独处理的内容要写在万能异常的前面
# 没有被中断就会执行else中的代码
# finally不管代码是否异常都会执行
# finally和return相遇的时候还会执行
