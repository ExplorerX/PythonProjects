from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'books', '-o', 'books.csv'])
cmdline.execute(['scrapy', 'crawl', 'webspider', '-o', 'nations.csv'])
