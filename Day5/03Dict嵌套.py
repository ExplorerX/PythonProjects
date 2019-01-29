dic = {
    'name': ['alex', 'wusir', 'taibai'],
    'py9': {
        'time': '1213',
        'learn_money': 19800,
        'address': 'CBD',
    },
    'age': 21,
}
# dic['age'] = 56
# print(dic)
# dic['name'].append('日天')
# print(dic)
# dic['name'][1] = dic['name'][1].upper()
# print(dic['name'])
# dic['py9']['famale'] = 6
# dic['py9'].setdefault('female', 6)
# print(dic)
info = input('>>>')
for i in info:
    if i.isalpha():
        info = info.replace(i, ' ')
l = info.split()
print(len(l))
