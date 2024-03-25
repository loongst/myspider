# -*- coding: utf-8 -*-
import scrapy
from s1.items import S1Item
from scrapy_redis.spiders import RedisSpider
# from s1 import middlewares
# from selenium import webdriver
class ClSpider(RedisSpider):

    # def __init__(self):
    #     self.options=webdriver.ChromeOptions()
    #     # self.options.add_argument('--headless')
    #     self.options.set_headless()
    #     self.browser=webdriver.Chrome(chrome_options=self.options)
    #     super().__init__()
    name = 'cl'
    # allowed_domains = ['example.com']
    # start_urls = ['https://cu0l.com/html/category/video/video1/page_1.html']
    redis_key='s1:start_urls'

    def parse(self, response):
        #next_page
        next_page=response.xpath('//div[@class="page page_navi"]/a/@href').getall()[-2]
        yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)
            

        #current_page_list
        current_page_list = response.xpath('//li[@class="col-lg-4 col-md-4 col-xs-6"]//a/@href').getall()
        for curl in current_page_list:
            yield scrapy.Request(url=response.urljoin(curl),callback=self.get_item)

    #item_in_list
    
    def get_item(self,response):

        name = response.xpath("//div[@class='j_s']/h3/text()").getall()
        url = response.xpath("//div[@class='j_s']//a/@href").get()
        tag = ','.join(response.xpath("//div[@class='j_s']//li/a/text()").getall()[2:])
        item=S1Item(name=name,url=url,tag=tag)
        yield item

        

        



