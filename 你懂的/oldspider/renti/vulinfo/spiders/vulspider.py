# -*- coding: utf-8 -*-
import scrapy
from vulinfo.items import VulinfoItem

class VulspiderSpider(scrapy.Spider):
    name = 'vulspider'
    # allowed_domains = ['roak.com/']
    start_urls = ['http://roak.com/img/list/?tid=6']

    def parse(self, response):

        locallist=response.xpath("//ul[@class='clearfix']/li/a/@href").getall()
        for url in locallist:
            yield scrapy.Request(url=response.urljoin(url),callback=self.parse)

        # next_page_list=
        try:
            next_page=response.xpath('//section[@id="vod-page"]/a/@href').getall()[-1]
            yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)
        except:
            pass

        
        item=VulinfoItem()
        image_urls=response.xpath("//img[@class='pic-large']/@src").get()
        image_urls='http://roak.com'+image_urls.strip()
        catgery=response.xpath("//img[@class='pic-large']/@alt").get()
        item['image_urls']=[image_urls]
        item['catgery']=catgery
        print(item)
        yield item
        next_item_page= response.xpath("//div[@class='pic-next-img']/a/@href").get()
        if next_item_page:
            yield scrapy.Request(url=response.urljoin(next_item_page),callback=self.parse)


# import scrapy
# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor
# from vulinfo.items import VulinfoItem

# class VulspiderSpider(CrawlSpider):

#     name = 'cspider'
#     allowed_domains = ['roak.com']
#     start_urls = ['http://roak.com/img/list/?tid=6']
#     rules={
#         Rule(LinkExtractor(allow=r'http://roak.com/img/list?tid=.*'),callback="parse_my",follow=True),
#         Rule(LinkExtractor(allow=r'http://roak.com/img/?id=.*'),callback="parse_my",follow=True)
#     }

#     print("p"*100)

#     def parse_my(self,response):
#         print("xxoo"*50)

#         item=VulinfoItem()
#         image_urls=response.xpath("//img[@class='pic-large']/@src").get()
#         image_urls='http://roak.com'+image_urls.strip()
#         catgery=response.xpath("//img[@class='pic-large']/@alt").get()
#         item['image_urls']=[image_urls]
#         item['catgery']=catgery
#         print(item)
#         yield item