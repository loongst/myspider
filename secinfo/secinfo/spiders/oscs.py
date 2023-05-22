import scrapy
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider
from scrapy import FormRequest
from scrapy.http import FormRequest
from scrapy.http import JsonRequest
import json
import logging
import requests
import datetime
import random
import time as t

class OscsSpider(scrapy.Spider):
    name = "oscs"
    allowed_domains = ["oscs1024.com"]
    start_urls = ["https://www.oscs1024.com/cm"]
    myheaders={
        "cookie":"Hm_lvt_113185c61c5bffebb22e97ff5c955cc5=1678260308; Hm_lpvt_113185c61c5bffebb22e97ff5c955cc5=1678260308",
        "Content-Type": "application/json",
        "origin":"https://www.oscs1024.com",
        "referer":"https://www.oscs1024.com/cm",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    cookies={"Hm_lvt_113185c61c5bffebb22e97ff5c955cc5":"1678260308","Hm_lpvt_113185c61c5bffebb22e97ff5c955cc5":"1678260308"}
   
    def parse(self, response):
        apiurl="https://www.oscs1024.com/oscs/v1/intelligence/list"
        for i in range (5):
            formdata={"page":i+1,"per_page":10}
            data = json.dumps(formdata)
            yield JsonRequest(url=apiurl,data=formdata,headers=self.myheaders,cookies=self.cookies,callback=self.get_item,dont_filter=True)
           

    def get_item(self,response):
            print(response.text)
            content=json.loads(response.text)
            for i in content['data']['data']:

                name = i['title']
                url = i['url']
                time = i['public_time'].split("T")[0]
                severity = i['level']
                result= {
                    "name":name,
                    "url":url,
                    "time":time,
                    "severity":severity
                }

                # strftime1 = datetime.datetime.strptime(time, "%Y-%m-%d")
                # now=str(datetime.datetime.now().date())
                # nowtime2 = datetime.datetime.strptime(now, "%Y-%m-%d")
                # label=nowtime2-strftime1
                # if label.days>7:
                #     raise CloseSpider("停止寻找漏洞时间超过7天的数据！")

                yield result
