# -*- coding: utf-8 -*-
import scrapy


class WebspiderSpider(scrapy.Spider):
    name = 'webspider'
    allowed_domains = ['http://example.webscraping.com/']
    start_urls = ['http://http://example.webscraping.com//']

    def parse(self, response):
        pass
