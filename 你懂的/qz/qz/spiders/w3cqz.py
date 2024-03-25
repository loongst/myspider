# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os,sys

class W3cqzSpider(CrawlSpider):
    name = 'loongqz'
    allowed_domains = ['lskxky.com']
    start_urls = ['http://lskxky.com/index.php?s=/list-read-id-23-p-1']

    rules = (
        Rule(LinkExtractor(allow=r'http://lskxky.com/index.php?s=/list-read-id-23-p-\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        pathname=response.url.split("/")[-1].replace('?',"")
        if not pathname:
            pathname="index.html"
        with open(pathname,'wb+') as f:
            print(response.body)
            f.write(response.body)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
