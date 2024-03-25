# -*- coding: utf-8 -*-
import scrapy

import json
class MproxySpider(scrapy.Spider):
    name = 'Mproxy'
    # allowed_domains = ['httpbin.org']
    start_urls = ['http://120.79.152.212:8088/ip']

    def parse(self, response):
        proxystr=json.loads(response.text)['origin']
        print(proxystr)
        yield scrapy.Request(url=response.url,callback=self.parse,dont_filter=True)
