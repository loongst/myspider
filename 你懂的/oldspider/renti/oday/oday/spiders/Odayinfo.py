# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from oday.items import OdayItem

class OdayinfoSpider(CrawlSpider):
    name = 'Odayinfo'
    allowed_domains = ['cn.0day.today']
    start_urls = ['https://cn.0day.today/remote/1']

    rules = (
        Rule(LinkExtractor(allow=r'https://cn.0day.today/remote/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        divs=response.xpath('//div[@class="ExploitTableContent"]')
        for div in divs:

            Odate_time = div.xpath('./div[1]/a/text()').get()
            Odescription = div.xpath('./div[2]/h3/a/text()').get().strip("\n").strip("\t")
            Otype = div.xpath('./div[3]/a/text()').get()
            Ohits = div.xpath('./div[4]/text()').get()
            Orisk_info = div.xpath('./div[5]/div/div/text()').get()
            Ocve = div.xpath('./div[8]/div/text()').get().strip("\n").strip("\t").strip('\n')
            Oprice = div.xpath('./div[10]/text()').get().strip("\n\t\t\t\t\t")
            
            item=OdayItem(
                Odate_time=Odate_time,
                Odescription=Odescription,
                Otype=Otype,
                Ohits=Ohits,
                Orisk_info=Orisk_info,
                Ocve=Ocve,
                Oprice=Oprice
            )
            print("6"*100)
            print(item)
            print("9"*100)
            yield item