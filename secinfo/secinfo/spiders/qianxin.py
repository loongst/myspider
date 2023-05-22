import scrapy


class QianxinSpider(scrapy.Spider):
    name = "qianxin"
    allowed_domains = ["ti.qianxin.com"]
    start_urls = ["http://ti.qianxin.com/"]

    def parse(self, response):
        pass
