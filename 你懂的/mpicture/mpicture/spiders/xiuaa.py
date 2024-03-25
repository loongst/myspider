import scrapy
from mpicture.items import MpictureItem

class XiuaaSpider(scrapy.Spider):
    name = 'xiuaa'
    # allowed_domains = ['xiuaa.com']
    start_urls = ['https://www.xiuaa.com/xgmn_0.html']

    def parse(self, response):
        current_list=response.xpath('//div[@class="post"]/a/@href').getall()
        for url in current_list:
            yield scrapy.Request(url=response.urljoin(url),callback=self.deal_item)

        try:
            next_page=response.xpath('//div[@id="pager"]/ul/li/a/@href').getall()[-2]
            print('=============')
            yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)
            print('=============')
        except:
            print('找不到下一页')
            pass

    def deal_item(self,response):

        
        catgery=response.xpath('//div[@id="bigpic"]/a/img/@alt').get().split('(')[0]
        image_url=response.xpath('//div[@id="bigpic"]/a/img/@src').get()
        image_urls=[response.urljoin( image_url)]
        item=MpictureItem(catgery=catgery,image_urls=image_urls)
        yield item


        next_page2=response.xpath('//div[@id="pager"]/ul/li/a/@href').getall()[-2]
        yield scrapy.Request(url=response.urljoin(next_page2),callback=self.deal_item)





