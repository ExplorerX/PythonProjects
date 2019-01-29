# import time
# time.sleep()  # 程序停止，以秒为单位
# time.time()  # 返回以秒为单位的浮点数
# 表示时间的三种方式：
# 1、时间戳：通常来说，时间戳表示的是从1970年1月1日00：00：00开始按秒计算的偏移量。给计算机看的
# 2、格式化的时间字符串：给人看的
# 3、元组：结构化时间 struct_time元组有9个元素(年，月，日，时，分，秒，一年中第几周，第几天，夏令时)
#       计算用的
import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))  # year month day hour minutes seconds
# print(time.strftime("%Y/%m/%d %H:%M:%S"))  # year month day hour minutes seconds
# print(time.strftime("%H:%M:%S"))  # year month day hour minutes seconds
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# struct_time = time.localtime()
# print(struct_time.tm_year)

# 时间戳和结构化时间的转换
# t = time.time()
# struct_time = time.localtime()
# print(struct_time)

# 结构化时间转到时间戳

