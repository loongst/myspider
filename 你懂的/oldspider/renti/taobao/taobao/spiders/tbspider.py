# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from taobao.items import TaobaoItem
class TbspiderSpider(CrawlSpider):
    name = 'tbspider'
    allowed_domains = ['wwwdxj1119.com']
    start_urls = ['https://wwwdxj1119.com/arttype/20.html']

    rules={
        Rule(LinkExtractor(allow=r'https://wwwdxj1119.com/arttype/20-\d+.html'),callback=None,follow=True),
        Rule(LinkExtractor(allow=r'https://wwwdxj1119.com/artdetail-\d+.html'),callback="parse_self",follow=False)
        
    }

    def parse_self(self, response):
        mtitle=response.xpath('//h1/text()').get()
        mcontent=response.xpath("//div[@class='fed-arti-content fed-padding']/p/text()").getall()
        mcontent=''.join(mcontent)
        item=TaobaoItem()
        item['mtitle']=mtitle
        item['mcontent']=mcontent

        yield item