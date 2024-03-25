# -*- coding: utf-8 -*-
import scrapy
import json

class MymdwSpider(scrapy.Spider):
    name = 'mymdw'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://120.79.152.212:8088/user-agent']

    def parse(self, response):
        ag=json.loads(response.text)['user-agent']
        print(ag)

        yield scrapy.Request(url=response.url,dont_filter=True,callback=self.parse)
