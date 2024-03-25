# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
from pymysql.converters import escape_string
from vulnhub.settings import *
class VulnhubPipeline:
    def process_item(self, item, spider):
        return item

class VulnhubMiddlewarePipeline(object):
    def __init__(self):
        dbparams = {
            'host':host,
            'port':3306,
            'user':user,
            'password':password,
            'database':database,
            'charset':'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql =None

    @property
    def sql(self):
        if not self._sql:
            self._sql='''
            insert into vuln_info(id,name,date_release,series,file_size,mirror,description,file_format,operating_system)
            values (null,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
            return self._sql
        return self._sql

    def process_item(self,item,spider):
        defer=self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(
            escape_string(item['name']),
            escape_string(item['date_release']),
            escape_string(item['series']),
            escape_string(item['file_size']),
            escape_string(item['mirror']),
            escape_string(item['description']),
            escape_string(item['file_format']),
            escape_string(item['operating_system']),
        ))

    def handle_error(self,error,item,spider):
        print(error)