import requests
import re
html = requests.get("http://gs.sit.imust.cn/info/2020/2678.htm")
html.encoding = 'utf-8'
re_str = r'<td width=.*?\svalign=.*?\sstyle=.*?><p class=.*?>.*?</p><p class=.*?>' \
         r'<strong>.*?仿宋_gb2312\">(.*?)' \
         r'[<span lang=\"EN-US\">(.*?)</span>(.*?)]{4}' \
         r'<a name=.*?>(.*?)' \
         r'<span lang=\"EN-US\">(.*?)</span></a>' \
         r'[<span lang=\"EN-US\">(.*?)</span>(.*?)]{3}' \
         r'<span lang=\"EN-US\">(.*?)</span>' \
         r'</p>'
m = re.findall(re_str, html.text)
print(m)
# for i in range(0, m.lastindex+1):
#     print(m.group(i))
# print(html.text)

