# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[a-z0-9]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # filename=response.url.split('/')[-1]
        # with open(filename,"w",encoding="utf-8") as f:
        #     f.write(response.text)

        title=response.xpath('//h1[@class="_2zeTMs"]/text()').get()

        content=response.xpath('//article[@class="_2rhmJa"]/p/text()').getall()
        content=''.join(content)
        author=response.xpath('//a[@class="qzhJKO"]/span/text()').get()
        read_count=response.xpath('//div[@class="s-dsoj"]/span[3]/text()').get()
        like_count=response.xpath('//div[@class="_3BUZPB"]/span[@class="_1LOh_5"]/text()').get()
        subjects=response.xpath('//div[@class="_2Nttfz"]/a/span/text()').getall()
        subjects=','.join(subjects)
        item = JianshuItem(title=title,content=content,author=author,read_count=read_count,like_count=like_count,subjects=subjects)
        print("+"*80)
        print(item)
        print("+"*80)
        return item
