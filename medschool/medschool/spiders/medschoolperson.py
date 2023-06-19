import scrapy


class MedschoolpersonSpider(scrapy.Spider):
    name = "medschoolperson"
    allowed_domains = ["www.medschool.umaryland.edu"]
    start_urls = ["https://www.medschool.umaryland.edu/faculty/Faculty-Profiles/"]

    def parse(self, response):
        url_list=response.xpath("//div[@class='content']/ul/li[3]/a/@href").getall()
        for i in url_list:
            yield scrapy.Request(url=i,callback=self.get_item)

    def get_item(self,response):
        item={}
        person_list=response.xpath("/html/body/div[2]/div[2]/div[2]/ul/li")
        for it in person_list:
            item['username']=it.xpath("./strong//text()").get().replace('\r\n','').replace(' ','')
            item['tel']=it.xpath("./div[2]/text()").get()
            item['email']=it.xpath("./div[3]//text()").get()
            try:
                keywords=it.xpath("./div[4]//text()").get()
                item['keywords']=keywords
            except Exception as e:
                item['keywords']=''
                print(e)
            yield item