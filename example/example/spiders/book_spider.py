import scrapy
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = "books"

    # 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中，我们使用
        # css()方法找到所有这样的article元素，并依次迭代
        # for book in response.css("article.product_pod"):
        #     书名信息在article>h3>a元素的tittle属性里
        #     例如<a tittle="A Light in the Attic">A light in the...</a>
        #     name = book.xpath("./h3/a/@title").extract_first()
        #     书价信息在<p class="price_color">的TEXT中
        #     例如：<p class="price_color">￡51.77</p>
        #     price = book.css("p.price_color::text").extract_first()
        #     yield {
        #         "name": name,
        #         "price": price,
        #     }
        # 提取链接
        # next_url = response.css("ul.pager li.next a::attr(href)").extract_first()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)
        for sel in response.css("article.product_pod"):
            book = BookItem()
            book["name"] = sel.xpath("./h3/a/@title").extract_first()
            book["price"] = sel.css("p.price_color::text").extract_first()
            yield book
        next_url = response.css("ul.pager li.next a::attr(href)").extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
