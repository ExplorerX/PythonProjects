# def demo():
#     for i in range(4):
#         yield i
#
#
# g = demo()
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g1), type(g1))
# print(list(g2), type(g2))


def add(n, i):
    return n+i


def test():
    for i in range(4):
        yield i


g = test()
for n in [1, 10, 5]:
    g = (add(n, i) for i in g)

print(list(g))
