# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import hashlib
from scrapy.utils.python import to_bytes
class MpicturePipeline(ImagesPipeline):
    
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self,item,info):
        # print('开始1'*10)
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item':item})

    def file_path(self,request,response=None,info=None):
        # print('开始2'*10)
        image_guid=hashlib.sha1(to_bytes(request.url)).hexdigest()
        item=request.meta['item']
        image_guid=item['catgery']+'/'+image_guid+'.jpg'
        return image_guid

    # def item_completed(self, results, item, info):
    #     print('开始3'*10)
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     adapter = ItemAdapter(item)
    #     adapter['image_paths'] = image_paths
    #     return item
