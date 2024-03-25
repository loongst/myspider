# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycrawl.items import MycrawlItem

class McrawlSpider(CrawlSpider):
    name = 'Mcrawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://quotes.toscrape.com/page/\d'),follow=True),
        Rule(LinkExtractor(allow=r'http://quotes.toscrape.com/author/.+'),callback="parse_item",follow=False),
    )

    def parse_item(self, response):
        item = MycrawlItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['author']=response.xpath("//h3[@class='author-title']/text()").get()
        borninfo= response.xpath("//div[@class='author-details']//span/text()").getall()
        item['born']=''.join(borninfo)
        item['content']=response.xpath("//div[@class='author-description']/text()").get()
        # print(item)
        yield item
