# -*- coding: utf-8 -*-
import scrapy
from rt.items import RtItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    #allowed_domains = ['rtys6.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        #nextpage
        nextpage=response.xpath('//li[@class="next"]/a/@href').get()
        if nextpage:
            yield response.follow(nextpage)

        #item

        divs=response.xpath("//div[@class='col-md-8']/div")

        for div in divs:
            item=RtItem()
            mtext=div.xpath("./span[@class='text']/text()").get()
            mauthor=div.xpath(".//small/text()").get()
            mtags=div.xpath('.//a[@class="tag"]/text()').getall()
            item['mtext']=mtext
            item['mauthor']=mauthor
            item['mtags']=mtags
            yield item


