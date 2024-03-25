# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.exceptions import DropItem
from scrapy.http import  Request
from scrapy.pipelines.images import ImagesPipeline
class MmspiderPipeline(ImagesPipeline):
    def file_path(self,request,response=None,info=None):
        file_guid=request.url.split('/')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
       
        return os.path.join(file_guid[-2],file_guid[-1])

        
    def get_media_request(self,item,info):
        headers={
            "Host" : "i.meizitu.net",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language" : "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding" : "gzip, deflate, br",
            "DNT" : "1",
            "Connection" : "keep-alive",
            "Upgrade-Insecure-Requests" : "1",
            "Cache-Control" : "no-cache",
            "TE" : "Trailers",
        }
        for url in item['image_urls']:
            yield Request(url,headers=headers)

    def item_completed(self,results,item,info):
        image_paths=[x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("it contains no image")
        #item['image_paths']=image_paths
        yield item  

