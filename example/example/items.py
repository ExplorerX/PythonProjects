# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(Item):
    name = Field()
    price = Field()


# 如果又添加了一个新的爬虫，用来爬取中文翻译的书籍信息，可以来继承BookItem类
# 实现对于新的字段的追加和实现
class ForeignBookItem(BookItem):
    translator = Field()
