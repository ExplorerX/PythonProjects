# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleWebscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NationItem(scrapy.Item):
    area = scrapy.Field()
    population = scrapy.Field()
    iso = scrapy.Field()
    country = scrapy.Field()
    capital = scrapy.Field()
    continent = scrapy.Field()
    tld = scrapy.Field()
    currency_code = scrapy.Field()
    currency_name = scrapy.Field()
    phone = scrapy.Field()
    languages = scrapy.Field()
    neighbours = scrapy.Field()
