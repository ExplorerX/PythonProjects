# login 登录
# log 日志
# logging

# 什么叫日志
# 日志是用来记录用户行为或者代码的执行过程

# logging
# 我能够一键控制，
# 拍错的时候需要打印很多细节来帮助我拍错
# 严重的错误记录下来
# 有一些用户行为 有没有错都要记录下来
# import logging
# logging.debug('debug message')  # 低级别的 # 排错信息
# logging.info('info message')  # 正常信息
# logging.warning('warning message')  # 警告信息
# logging.error('error message')  # 错误信息
# logging.critical('critical message')  # 高级别信息 # 严重错误信息
# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
# try:
#     int(input('>>>'))
# except ValueError:
#     print('ValueError!')

# basicconfig 简单能做的事情相对少
#   中文的乱码问题
#   不能在屏幕和文件中同时输出
# 配置log对象，稍微有点复杂，但是能做的事情相对多
#   程序的充分解耦
#   让程序变得高可定制
import logging
logger = logging.getLogger()
fh = logging.FileHandler('log.log', encoding='utf-8')
sh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')

# 有5中级别的日记录模式：
# 两种配置方式：basicconfig和log对象
