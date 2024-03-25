import scrapy
from mpicture.items import MpictureItem
import requests
class SexypicSpider(scrapy.Spider):
    name = 'sexypic'
    # allowed_domains = ['b9102.com']
    start_urls = ['https://www.b9102.com/photo/photo_list.html?photo_type=23&page_index=1']



    def parse(self, response):

        # headers={
        #     ":authority": "imagetupian.nypd520.com",
        #     ":method": "GET",
        #     # ":path": /uploads/laoying/2020/2/2020226/80.jpg?max-age=3600
        #     ":scheme": "https",
        #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     "accept-encoding": "gzip, deflate, br",
        #     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        #     "cache-control": "max-age=0",
        #     "if-modified-since": "Wed, 26 Feb 2020 00:47:31 GMT",
        #     "if-none-match": 'W/"5e55c023-48422"',
        #     "sec-fetch-dest": "document",
        #     "sec-fetch-mode": "navigate",
        #     "sec-fetch-site": "none",
        #     "sec-fetch-user": "?1",
        #     "upgrade-insecure-requests": "1",
        #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
        # }

        current_item_list=response.xpath('//div[@class="box movie_list"]/ul/li/a/@href').getall()
        for url in current_item_list:
            # headers[':path']=url+'?max-age=3600'
            yield scrapy.Request(url=response.urljoin(url),callback=self.dealwith_item)
        
        
        next_page_tmp=response.xpath('//div[@class="pagination"]/a/@href').getall()
        next_page_url=next_page_tmp[-2]
        yield scrapy.Request(url=response.urljoin(next_page_url),callback=self.parse)

    def dealwith_item(self,response):
        catgery=response.xpath('//div[@class="post_title"]/h1/text()').get()
        image_urls=response.xpath('//div[@class="post_content"]/a/img/@src').getall()
        # for i in image_urls:
        #     resp=requests.get(i)
        #     if resp.status_code==200:
        #         with open(image_urls.split('/')[-1],"wb+") as f:
        #             f.write(resp.text)
        item=MpictureItem(catgery=catgery,image_urls=image_urls)
        # item=MpictureItem()
        # item['image_urls']=image_urls
        # item['catgery']=catgery
        print("_"*50)
        print(item)
        yield item 


