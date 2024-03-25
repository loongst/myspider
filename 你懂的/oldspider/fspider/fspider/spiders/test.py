# -*- coding: utf-8 -*-
import scrapy

from  fspider.items import FspiderItem
class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.chaojida.net']
    start_urls = ['http://www.chaojida.net/index.php',]

    def parse(self, response):

        nextp=response.xpath('//a[@class="nav-link"]/@href').getall()
        for urlp in nextp:
            yield scrapy.Request(url=response.urljoin(urlp),callback=self.parse)

        divs = response.xpath('//a[@class="box"]')
        for div in divs:
            item=FspiderItem()
            item['images']=[div.xpath(".//h4[@class='caption-title']/text()").getall()[0].strip('\r\n').strip('\t')]
            item['image_urls']=div.xpath(".//img[@class='caption-bg']/@src").getall()

            yield item


