# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile']

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        values = response.css('table td.w2p_fw::text').extract()
        yield dict(zip(keys, values))


    # 模拟登陆
    login_url = 'http://example.webscraping.com/places/default/user/login'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        fd = {'email': '384470140@qq.com', 'password': '123456'}
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)

    def parse_login(self, response):
        if 'Goodman' in response.text:
            yield from super().start_requests()
