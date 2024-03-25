# -*- coding: utf-8 -*-
import scrapy
import string,re
from mmspider.items import MmspiderItem

class MzspiderSpider(scrapy.Spider):
    name = 'mzspider'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/tag/youhuo/']

    def parse(self, response):


        netx_page=response.xpath('//a[@class="next page-numbers"]/@href').extract()
        print('下一页地址')
        print(netx_page)
        for url in netx_page:
            print('请求下一页--------------------------')
            yield scrapy.Request(url,callback=self.parse)
        item_selector=response.xpath('//ul[@id="pins"]/li/a/@href').extract()
        print("当前页条目：")
        print(item_selector)
        for url2 in item_selector:
            print('请求页内条目')
            yield scrapy.Request(url2,callback=self.get_image_url)

      

        
        
    def get_image_url(self,response):
        imageurllist=[]
        imageurl=response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()
        num=int(response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2])
        alt=response.xpath('//div[@class="main-image"]/p/a/img/@alt').extract()
        for url3 in imageurl:
            for x in range(1,num+1):
                if x<10:
                    temp=url3.replace('1.jpg',str(x)+'.jpg')
                else:
                    temp=url3.replace('01.jpg',str(x)+'.jpg')
                imageurllist.append(temp)
        item=MmspiderItem()
        item['image_urls']=imageurllist
        item['alt']=alt
        print("条目内图片")
        print(imageurllist)
        print(alt)
        yield item

        