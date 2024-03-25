import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tortest2Spider(CrawlSpider):
    name = 'tortest2'
    allowed_domains = ['gunshopzpqbe4kgl.onion']
    start_urls = ['http://gunshopzpqbe4kgl.onion/']

    rules = (
        Rule(LinkExtractor(allow=r'http://gunshopzpqbe4kgl.onion/.*'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r))
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        try:

            page_name=response.url.split("/")[-1]
            file_path='./page/'+page_name
            if response.status_code=='200':
                with open(file_path,"w+") as f:
                    f.write(response.text)

        except:
            print("page save failed!")
        return item
