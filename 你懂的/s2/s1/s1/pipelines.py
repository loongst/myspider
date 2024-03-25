# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
class S1Pipeline(object):

    def __init__(self):

        dbparams={
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'root',
        'database':'8exf',
        'charset':'utf8',
        }
        self.conn=pymysql.connect(**dbparams)
        self.cursor=self.conn.cursor()
        self._sql=None

    def process_item(self,item,spider):
        self.cursor.execute(self.sql,(item['name'],item['url'],item['tag']))
        self.conn.commit()
        return item
  
    @property
    def sql(self):
        if not self._sql:
            self._sql="""
        insert into rh(id,name,url,tag) values(null,%s,%s,%s)
            """
            return self._sql
        return self._sql


# class YIBUPipline(object):
#     # def process_item(self, item, spider):
#     #     return item
#     def __init__(self):

#         dbparams={
#             'host':'127.0.0.1',
#             'port':3306,
#             'user':'root',
#             'password':'root',
#             'database':'cl',
#             'charset':'utf8',
#             'cursorclass':cursors.DictCursor
#             }
#         self.dbpool=adbapi.ConnectionPool('pymysql',**dbparams)
#         self._sql=None


#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql="""insert into t1(id,name,url,tag) values(null,%s,%s,%s)"""
#             return self._sql
#         return self._sql
    

#     def process_item(self,item,spider):
#         print("-"*100)
#         print(item)
#         print("-"*100)
#         defer=self.dbpool.runInteraction(self.insert_item,item)
#         defer.addErrback(self.handle_error,item,spider)


#     def insert_item(self,cursor,item):
#         cursor.execute(self.sql,(item['name'],item['url'],item['tag']))
      
#     def handle_error(self,error,item,spider):
#         print(error)