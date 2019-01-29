def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'


g = generator()
print(dir(g))
print(type(g))
for i in g:
    print(i)
