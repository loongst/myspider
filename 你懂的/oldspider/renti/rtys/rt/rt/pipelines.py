# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.pipelines.images import ImagesPipeline
# import scrapy
# from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline
# import functools
# import hashlib
# import six

# try:
#     from cStringIO import StringIO as BytesIO
# except ImportError:
#     from io import BytesIO

# from PIL import Image

# from scrapy.utils.misc import md5sum
# from scrapy.utils.python import to_bytes
# from scrapy.http import Request
# from scrapy.settings import Settings

# import json
# class RtPipeline(object):

#     # def process_item(self, item, spider):
#     #     return item
#     # def get_media_requests(self, item, info):
#     #     for image_url in item['image_urls']:
#     #         yield scrapy.Request(image_url,meta={'item':item})
#     #     #通过meta属性将item传递到file_path()函数


#     # def file_path(self, request, response=None, info=None):
#     #     image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
#     #     item=request.meta['item']
#     #     image_guid = item['images']+'/'+image_guid+'.jpg'
#     #     print(image_guid)
#     #     return image_guid
#     def __init__(self):
#         self.fp=open("123456.txt","w",encoding="utf-8")

    # def open_spider(self,spider):
    #     print('爬虫开始啦！')

    # def process_item(self,item,spider):
    #     item_json=json.dumps(dict(item),ensure_ascii=False)
    #     self.fp.write(item_json+'\n')
        
    # def close_spider(self,spider):
    #     self.fp.close()
    #     print("爬虫结束了")


# from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter

# class quotes(object):

#     def __init__(self):
#         self.fp=open('quotes.json',"wb")

#     def open_spider(self,spider):
#         print('爬虫开始啦')
#         self.export=JsonItemExporter(self.fp,ensure_ascii=False)
#         self.export.start_exporting()
#     def process_item(self,item,spider):
#         self.export.export_item(item)

#     def close_spider(self,spider):
#         self.export.finish_exporting()
#         print("爬虫结束啦")

from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter

class quotes(object):

    def __init__(self):
        self.fp=open('quotes2.json',"wb")

    def open_spider(self,spider):
        print('爬虫开始啦')
        self.export=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
    def process_item(self,item,spider):
        self.export.export_item(item)

    def close_spider(self,spider):
        print("爬虫结束啦")

