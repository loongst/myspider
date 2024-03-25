import scrapy


class TortestSpider(scrapy.Spider):
    name = 'tortest'
    allowed_domains = ['gunshopzpqbe4kgl.onion']
    start_urls = ['http://gunshopzpqbe4kgl.onion/']

    def parse(self, response):
        pass
