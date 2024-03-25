# -*- coding: utf-8 -*-
import scrapy
from s1.items import S1Item
# from s1 import middlewares
# from selenium import webdriver
from scrapy_redis.spiders import RedisSpider
class ClSpider(RedisSpider):

    # def __init__(self):
    #     self.options=webdriver.ChromeOptions()
    #     # self.options.add_argument('--headless')
    #     self.options.set_headless()
    #     self.browser=webdriver.Chrome(chrome_options=self.options)
    #     super().__init__()
    name = 'cl'
    # allowed_domains = ['example.com']
    # start_urls = ['https://8exf.com/html/category/video/video2/page_1.html']
    redis_key='s1:start_urls'

    def parse(self, response):
        #next_page
        next_page=response.xpath('//div[@class="page_navi"]/a/@href').getall()[-2]
        yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)
            

        #current_page_list
        current_page_list = response.xpath('//div[@class="tc_nr l_b"]/ul/li/div[@class="w_z"]//a/@href').getall()
        for curl in current_page_list:
            if curl is not '/':
                yield scrapy.Request(url=response.urljoin(curl),callback=self.get_item)

    #item_in_list
    
    def get_item(self,response):

        name = response.xpath('//div[@class="yp_bt"]/h1/text()').get()
        url = response.xpath('//div[@class="x_z"]/a/@href').get()
        tag = ','.join(response.xpath('//li[@class="tags_list"]/a/text()').getall())
        item=S1Item(name=name,url=url,tag=tag)
        yield item

        

        



