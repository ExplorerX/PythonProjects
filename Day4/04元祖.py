# 只读列表……元祖 可循环，可切片 儿子不能改，孙子可能能改
tu = (1, 2, 3, 'alex', [2, 3, 4, 'taibai'], 'egon')
tu[4][3] = tu[4][3].upper()
tu[4].append('sb')
for i in tu:
    print(i)
