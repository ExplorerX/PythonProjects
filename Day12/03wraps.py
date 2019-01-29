from functools import wraps


def wrapper(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print('这是在函数前面执行的代码！')
        ret = f(*args, **kwargs)
        print('这是在函数后面执行的代码！')
        return ret
    return inner


@wrapper  # func = wrapper(func)
def holiday(day):
    """
    这是一个放假通知
    :param day: 放假天数
    :return: 心情
    """
    print('全体放假%s' % day)
    return '好开心'


ret1 = holiday(3)
print(holiday.__name__)
print(holiday.__doc__)
print(ret1)
