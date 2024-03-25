# -*- coding: utf-8 -*-
import scrapy
from s1.items import S1Item
# from s1 import middlewares
# from selenium import webdriver
class ClSpider(scrapy.Spider):

    # def __init__(self):
    #     self.options=webdriver.ChromeOptions()
    #     # self.options.add_argument('--headless')
    #     self.options.set_headless()
    #     self.browser=webdriver.Chrome(chrome_options=self.options)
    #     super().__init__()
    name = 'cl'
    # allowed_domains = ['example.com']
    start_urls = ['https://c5y1.com/html/category/video/video2/']

    def parse(self, response):
        #next_page
        next_page=response.xpath('//div[@class="page page_navi"]/a/@href').getall()[-2]
        yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)
            

        #current_page_list
        current_page_list = response.xpath('//div[@class="t_p"]/a/@href').getall()
        for curl in current_page_list:
            if curl is not '#':
                yield scrapy.Request(url=response.urljoin(curl),callback=self.get_item)

    #item_in_list
    
    def get_item(self,response):

        name = response.xpath("//div[@class='j_s']/h3/text()").getall()
        url = response.xpath("//div[@class='rm_bq']/ul/li/a/@href").get()
        tag = ','.join(response.xpath("//div[@class='j_s']//li/a/text()").getall()[2:])
        print('+'*100)
        
        item=S1Item(name=name,url=url,tag=tag)
        print(item)
        yield item

        

        



