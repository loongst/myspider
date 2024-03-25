# -*- coding: utf-8 -*-
import scrapy
from vulinfo.items import VulinfoItem

class VulspiderSpider(scrapy.Spider):
    name = 'vulspider'
    allowed_domains = ['www.umei.cc']
    start_urls = ['https://www.umei.cc/tags/csnrsdp.htm']

    def parse(self, response):

        #本页地址列表
        localurls=response.xpath('//a[@class="TypeBigPics"]/@href').getall()
        for localurl in localurls:

            yield scrapy.Request(url=localurl, callback=self.parse)

        #各个分类的item和url
        nextpage=response.xpath('//div[@class="NewPages"]/ul/li/a/@href').getall().pop()
        if nextpage =='#':
            pass
        else:
            yield scrapy.Request(url=response.urljoin(nextpage),callback=self.parse)
            item=VulinfoItem()
            item['image_urls']=response.xpath('//p[@align="center"]/a/img/@src').getall()
            item['images']=response.xpath('//p[@align="center"]/a/img/@alt').getall()
            item['image_paths']=response.xpath('//p[@align="center"]/a/img/@alt').getall()
    
            yield item
