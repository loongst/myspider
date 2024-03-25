import scrapy
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider
from scrapy import FormRequest
from scrapy.http import FormRequest
import json
import logging
import requests
import datetime
import random
from secinfo.settings import USER_AGENTS_LIST
class OscsSpider(scrapy.Spider):
    name = "oscs"
    allowed_domains = ["oscs1024.com"]
    start_urls = ["https://www.oscs1024.com/cm"]
    headers={

        "accept-encoding":"gzip, deflate, br",
        "accept-language":"zh-CN,zh;q=0.9",
        "content-type":"application/json",
        # "cookie":"tgw_l7_route=e820e94b9fa7c80b604327cb18828928; Hm_lvt_113185c61c5bffebb22e97ff5c955cc5=1678260308; Hm_lpvt_113185c61c5bffebb22e97ff5c955cc5=1678260308",
        "origin":"https://www.oscs1024.com",
        "referer":"https://www.oscs1024.com/cm",
        "sec-ch-ua":'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"Windows",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    # def start_requests(self):
    #     data={"page":"1","per_page":"10"}
    #     # formdata=json.dumps(data)
    #     yield scrapy.FormRequest(url=self.start_urls[0],formdata=data,headers=self.headers,callback=self.parse)
    
    def parse(self, response):
        apiurl="https://www.oscs1024.com/oscs/v1/intelligence/list"
        for i in range (5):
            formdata={"page":i+1,"per_page":10}
            data = json.dumps(formdata)
            headers=self.headers
            # headers['user-agent']=random.choice(USER_AGENTS_LIST)
            res=requests.post(url=apiurl,data=data,headers=headers)
            if res.status_code==200:
                    content=json.loads(res.text)
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
                        yield result


'''
    def parse(self, response):

        # print("^"*300)
        # print(response.request.body.decode())
        url="https://www.oscs1024.com/oscs/v1/intelligence/list"
        headers=self.headers
        headers['referer']=response.url
        for i in range(1,5):
            data={"page":str(i),"per_page":"10"}
            yield scrapy.FormRequest(url=url,formdata=data,headers=headers,callback=self.my_parse)
        # #获取数据并返回
        # if response.status==200:
        #     content=json.loads(response.text)
        #     for i in content['data']['data']:
        #         name = i['title']
        #         url = i['url']
        #         time = i['public_time'].split("T")[0]
        #         severity = i['level']

        #         strftime1 = datetime.datetime.strptime(time, "%Y-%m-%d")
        #         now=str(datetime.datetime.now().date())
        #         nowtime2 = datetime.datetime.strptime(now, "%Y-%m-%d")
        #         label=nowtime2-strftime1
        #         if label.days>7:
        #             raise CloseSpider("停止寻找漏洞时间超过7天的数据！")


        #         yield {
        #             "name":name,
        #             "url":url,
        #             "time":time,
        #             "severity":severity
        #         }
'''

'''
    def my_parse(self,response):
        if response.status==200:
            content=json.loads(response.text)
            for i in content['data']['data']:
                name = i['title']
                url = i['url']
                time = i['public_time'].split("T")[0]
                severity = i['level']

                strftime1 = datetime.datetime.strptime(time, "%Y-%m-%d")
                now=str(datetime.datetime.now().date())
                nowtime2 = datetime.datetime.strptime(now, "%Y-%m-%d")
                label=nowtime2-strftime1
                if label.days>7:
                    raise CloseSpider("停止寻找漏洞时间超过7天的数据！")


                yield {
                    "name":name,
                    "url":url,
                    "time":time,
                    "severity":severity
                }


        yield scrapy.FormRequest(url=self.start_urls[0],formdata={"page":"2","per_page":"1000"},callback=self.parse) 
        next page
        try:
            cookie=''
            try:
                logging.error(response.headers)
                cookie=response.headers['Set-Cookie'].decode().split(";")[0]
                
            except Exception as e:
                logging.error(e)
                logging.error("bnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            if not cookie:
                logging.error(response.request.headers)
                cookie=response.request.headers['cookie'].decode()
                logging.error("333333333333333333333333333333333333333")
            logging.error(cookie)
            try:
                logging.warning(response.request.headers)
                rcookie=response.request.headers['cookie'].decode()
            except Exception as e:
                logging.error(e)
                logging.error('0'*300)
            cookies="Hm_lvt_20ad74f5b33195b920ff4c7a50c4d371=1677826659; Hm_lvt_113185c61c5bffebb22e97ff5c955cc5=1677485681,1677826783;"+cookie
            logging.error(cookies)
            page=int(response.request.body.decode().split("&")[0].split("=")[1])
            page+=1
            data={"page":str(page),"per_page":"10"}
            logging.error(data)
            # formdata=json.loads(data)
            yield scrapy.FormRequest(url=self.start_urls[0],formdata=data,headers={"cookie":cookies},callback=self.parse) 
        except Exception as e:
            logging.error("获取下一页数据失败！")
            logging.error(e)
        

        print("/"*200)
        print(response.text)        
        urls="https://www.oscs1024.com/oscs/v1/intelligence/list"

        if response.status==200:
            for i in range(1,11):
                formdata={"page":i,"per_page":10}
                data = json.dumps(formdata)
                res=requests.post(url=urls,data=data,headers=self.headers)

                if res.text:
                    content=json.loads(res.text)
                    for i in content['data']['data']:
                        name = i['title']
                        url = i['url']
                        time = i['public_time'].split("T")[0]
                        severity = i['level']
                        yield {
                            "name":name,
                            "url":url,
                            "time":time,
                            "severity":severity
                        }

'''