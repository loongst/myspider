import scrapy


class A0daySpider(scrapy.Spider):
    name = '0day'
    allowed_domains = ['0day.today.com']
    start_urls = ['http://0day.today']

    def parse(self, response):
        pass
