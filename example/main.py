from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'books', '-o', 'books.csv'])
cmdline.execute(['scrapy', 'crawl', 'books', '-t', 'excel', '-o', 'books.xls'])
