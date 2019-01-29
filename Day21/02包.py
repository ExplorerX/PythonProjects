# 把解决一类问题的模块放在一个文件夹里面，这个文件夹就是包
# 在python2.7中包里面必须包含一个__init__.py的文件才行，而在python3中没有也不影响
# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py', 'w'))
# l.append(open('glance/api/__init__.py', 'w'))
# l.append(open('glance/api/policy.py', 'w'))
# l.append(open('glance/api/versions.py', 'w'))
# l.append(open('glance/cmd/__init__.py', 'w'))
# l.append(open('glance/cmd/manage.py', 'w'))
# l.append(open('glance/db/models.py', 'w'))
# map(lambda f: f.close(), l)

# import glance
# glance.db.models.register_models('mysql')

# 使用绝对路径的特点：不能挪动，但是直观
# 使用相对路径的特点：可以随意移动包，只要能够找到包的位置，就可以使用包里面的模块
# 包里的模块如果也是使用了相对路径就不能直接执行了，使用了相对路径就不能在包内直接执行这个文件了


