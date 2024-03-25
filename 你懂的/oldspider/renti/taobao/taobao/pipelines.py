# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
class TaobaoPipeline(object):
    def process_item(self, item, spider):

        novelname=item['mtitle']+'.txt'
        fp=open(novelname,'wb')
        export=JsonItemExporter(fp,ensure_ascii=False,encoding='utf-8')
        print('xoxo'*40)
        export.export_item(item)
        fp.write(b'\n'*3)
        fp.close()
        return it
        
        
        
        em