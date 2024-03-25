# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
class JianshuPipeline(object):

    def __init__(self):
        dbparams={
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'database':'jianshu',
            'charset':'utf8'
        }
        self.conn=pymysql.connect(**dbparams)
        self.cursor=self.conn.cursor()
        self._sql=None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['author'],item['content'],item['read_count'],item['like_count'],item['subjects']))
        self.conn.commit()

        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into article2(id,title,author,content,read_count,like_count,subjects) values(null,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql



# class Mytwistedpipline(object):
#     def __init__(self):

#         dbparams={
#             'host':'127.0.0.1',
#             'port':3306,
#             'user':'root',
#             'password':'root',
#             'database':'jianshu',
#             'charset':'utf8',
#             'cursorclass':cursors.DictCursor
#         }
#         self.dbpool=adbapi.ConnectionPool('pymysql',**dbparams)
#         self._sql=None

#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql="""
#             insert into article2(id,title,author,content,subjects) values(null,%s,%s,%s,%s)
#             """
#             return self._sql
#         return self._sql

#     def process_item(self,item ,spider):
#         defer=self.dbpool.runInteraction(self.insert_item,item)
#         defer.addErrback(self.handle_error,item,spider)

#     def insert_item(self,cursor,item):
#         cursor.execute(self.sql,(item['title'],item['author'],item['content'],item['subjects']))

#     def handle_error(self,error,item,spider):
#         print("="*50+'error'+"="*50)
#         print(error)
#         print("="*50+'error'+"="*50)
