# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy import signals
from twisted.enterprise import adbapi
from pymysql import cursors 
class OdayPipeline(object):

    def __init__(self):
        params={
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'database':'0day',
            'charset':'utf8'
        }
        self.conn=pymysql.connect(**params)
        self.cursor=self.conn.cursor()
        self._sql=None

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into 0dayinfo2(id,Odate_time,Odescription,Otype,Ohits,Orisk_info,Ocve,Oprice) values(null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['Odate_time'],item['Odescription'],item['Otype'],item['Ohits'],item['Orisk_info'],item['Ocve'],item['Oprice']))
        self.conn.commit()
        return item
