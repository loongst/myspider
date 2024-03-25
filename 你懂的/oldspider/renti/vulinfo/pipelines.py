# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from vulinfo.settings import IMAGES_STORE
import functools
import hashlib
import six

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from PIL import Image

from scrapy.utils.misc import md5sum
from scrapy.utils.python import to_bytes
from scrapy.http import Request
from scrapy.settings import Settings

#TODO: from scrapy.pipelines.media import MediaPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FileException, FilesPipeline
import json
import os
# class VulinfoPipeline(object):

#     def __init__(self):
#         self.fp=open('xxoo.json',"w",encoding='utf-8')

#     def open_spider(self,spider):
#         print("爬虫开始了！")

#     def process_item(self,item,spider):
#         item_json=json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')

#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫结束了！")


class rbrtPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item':item})
    #通过meta属性将item传递到file_path()函数


    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        item=request.meta['item']
        image_guid = item['catgery']+'/'+image_guid+'.jpg'
        print("`"*50)
        print(image_guid)
        return image_guid

    ''' 

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    '''

    # class mypiplines(ImagesPipeline):
    #     def get_media_requests(self,item,info):
    #         Mrequests=super(mypiplines,self).get_media_requests(item,info)
    #         for Mrequest in Mrequests:
    #             Mrequest.item=item
    #         return Mrequests

    #     def file_path(self,request,response=None,info=None):
    #         path=super(mypiplines,self).file_path(request,response,info)
    #         catgery=request.item.get['catgery']
    #         filename=path.replace("full/","")  
    #         #path等于原方法中的full/xxx.jpg,在此将full/去掉，换上我们自己的catgery
    #         image_path=catgery+filename
    #         return image_path