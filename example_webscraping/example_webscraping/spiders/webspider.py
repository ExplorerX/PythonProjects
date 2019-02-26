# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import NationItem


class WebspiderSpider(scrapy.Spider):
    name = 'webspider'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div#results a[href]')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.detail_parse)
        # 获取next的链接
        le = LinkExtractor(restrict_css='div#pagination a[href]:last-child')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        nation = NationItem()
        nation['area'] = response.css('tr#places_area__row td.w2p_fw::text').extract_first().strip()
        nation['population'] = response.css('tr#places_population__row td.w2p_fw::text').extract_first().strip()
        nation['iso'] = response.css('tr#places_iso__row td.w2p_fw::text').extract_first().strip()
        nation['country'] = response.css('tr#places_country__row td.w2p_fw::text').extract_first().strip()
        nation['capital'] = response.css('tr#places_capital__row td.w2p_fw::text').extract_first().strip()
        nation['continent'] = response.css('tr#places_continent__row td.w2p_fw a::text').extract_first().strip()
        nation['tld'] = response.css('tr#places_tld__row td.w2p_fw::text').extract_first().strip()
        nation['currency_code'] = response.css('tr#places_currency_code__row td.w2p_fw::text').extract_first().strip()
        nation['currency_name'] = response.css('tr#places_currency_name__row td.w2p_fw::text').extract_first().strip()
        nation['phone'] = response.css('tr#places_phone__row td.w2p_fw::text').extract_first().strip()
        nation['languages'] = response.css('tr#places_languages__row td.w2p_fw::text').extract_first().strip()
        nation['neighbours'] = " ".join(response.css('tr#places_neighbours__row td.w2p_fw a::text').extract()).strip()
        yield nation


