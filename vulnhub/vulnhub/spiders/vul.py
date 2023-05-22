import scrapy
from vulnhub.items import VulnhubItem

class VulSpider(scrapy.Spider):
    name = 'vul'
    allowed_domains = ['vulnhub.com']
    start_urls = ['http://www.vulnhub.com/?page=3']

    def parse(self, response):
        for url in response.xpath("//div[@class='card']/a/@href").extract():
            yield scrapy.Request(url=response.urljoin(url),callback=self.get_info)

        #     nextpage is
        nextpage =response.xpath("//nav[@class='pagination-area']/ul/li[last()]/a/@href").extract_first()
        yield scrapy.Request(url=response.urljoin(nextpage),callback=self.parse)

    def get_info(self,response):
        item=VulnhubItem()
        item['name']=response.xpath("//div[@id='release']/ul/li[1]/text()").extract_first().strip(' :')
        item['date_release']=response.xpath("//div[@id='release']/ul/li[2]/text()").extract_first().strip(' :')
        item['series']=response.xpath("//div[@id='release']/ul/li[4]/a/text()").extract_first().strip(" :")
        item['file_size']=response.xpath("//div[@id='download']/ul/li/small/text()").extract_first()
        item['mirror']=response.xpath("//div[@id='download']/ul/li[2]/a/@href").extract_first()
        item['description']=';'.join(response.xpath("//div[@id='description']/p/text()").extract())
        item['file_format']=response.xpath("//div[@id='vm']/ul/li[1]/text()").extract_first().strip(" :")
        item['operating_system']=response.xpath("//div[@id='vm']/ul/li[2]/text()").extract_first().strip(" :")
        yield item

