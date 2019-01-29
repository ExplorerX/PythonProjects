def count_down(n):
    while n >= 0:
        new_n = yield n
        if new_n:
            n = new_n
        else:
            n -= 1


cd = count_down(5)
for i in cd:
    print(i)
    if i == 5:
        gg = cd.send(3)
        print("这是gg：", gg)
