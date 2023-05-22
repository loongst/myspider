import scrapy


class NoxSpider(scrapy.Spider):
    name = "nox"
    allowed_domains = ["nox.qianxin.com"]
    start_urls = ["http://nox.qianxin.com/"]

    def parse(self, response):
        pass
