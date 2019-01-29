# 双下方法
# __str__
# __repr__
# 内置的类方法和内置的函数之间有着千丝万缕的联系
# 使用str(obj)方法的时候执行的是obj所属数据类型中的内置方法__str__()方法
# 使用repr(obj)方法的时候执行的是obj所属数据类型中的内置方法__repr__()方法
# __repr__方法是__str__方法的备胎
# 如果类中没有__str__方法，就调用__repr__方法
# 但是反过来不行，就是没有__repr__方法，repr方法是不能调用__str__方法的
# 且这两个方法必须都返回字符串类型，否则会报错
# 正常打印一个对象的时候返回的是这个对象的内存地址
# 但是你在子类中重写了这个方法就会执行你自己的这个双下str方法和双下repr方法

# __len__方法不在object类中定义，因为一些数据类型是不能计算长度的，比如int
# 所以我们可以自己定义一个__len__方法，使用内置方法len()方法调用

# __del__方法：析构方法
# 使用内置函数del的时候会调用类中的__del__方法，而且就算你在子类中重写了这个方法，
# 仍然会先滴啊用__del__方法然后把这个对象析构掉
