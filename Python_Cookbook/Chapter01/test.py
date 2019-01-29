import re
text = '1.day75-1-01 内容回顾(Av28550381,P1).flv'
arr =re.findall('.*?(Av.*?,P1).flv', text, )
print(arr)
