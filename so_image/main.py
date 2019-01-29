# main函数用来在Windows端运行scrapy爬虫
from scrapy import cmdline
cmdline.execute("scrapy crawl images".split())
