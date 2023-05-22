import scrapy
import logging
from urllib.parse import urljoin
from scrapy.exceptions import CloseSpider
import datetime


class VenustechSpider(scrapy.Spider):
    name = "venustech"
    allowed_domains = ["venustech.com"]
    start_urls = ["https://www.venustech.com.cn/new_type/aqtg/"]

    def parse(self, response):
        a=0
        for it in response.xpath("//ul[@class='safetyList']/li"):
            a+=1
            print(a)
            name=it.xpath("./a/text()").get()
            url=urljoin(response.url,it.xpath("./a/@href").get())
            time=it.xpath("./span/text()").get()
            severity=''
            strftime1 = datetime.datetime.strptime(time, "%Y-%m-%d")
            now=str(datetime.datetime.now().date())
            nowtime2 = datetime.datetime.strptime(now, "%Y-%m-%d")
            label=nowtime2-strftime1
            if label.days>31:
                raise CloseSpider("停止寻找漏洞时间超过一个月的数据！")

            yield {
                "name":name,
                "url":url,
                "time":time,
                "severity":severity
            }


        try:
            next_page=response.xpath("//div[@id='kkpager']//a/@href").get()
            if next_page:
                next_page=urljoin(response.url,response.xpath("//div[@id='kkpager']//a/@href").get()) 
                yield scrapy.Request(next_page,callback=self.parse,dont_filter=False)

        except Exception as e:
            logging.error(e)
            logging.error("下一页跳转失败！")

        pass
