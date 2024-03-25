# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql
from twisted.enterprise import adbapi
from secinfo.settings import *
class SecinfoPipeline:
    def __init__(self):
        try:
            self.connect=pymysql.connect(
                host=DB_host,
                user=DB_user,
                passwd=DB_pass,
                db=DB_name
            )
            self.cursor=self.connect.cursor()
            print("数据库连接成功！")
        except Exception as e:
            print("数据库连接失败！")
            print(e)

    def process_item(self, item, spider):
        insert_sql='''
        insert into oscs(name,url,time,severity) values(%s,%s,%s,%s)
        '''

        # 当item['quotes']里面含有引号时，使用pymysql.escape_string()方法
        # sql = """INSERT INTO video_info(video_id, title) VALUES("%s","%s")""" % (video_info["id"],pymysql.escape_string(video_info["title"]))
        try:
            self.cursor.execute(insert_sql,(
                item['name'],
                item['url'],
                item['time'],
                item['severity']
            ))
            self.connect.commit()
            print("insert_sql插入成功!")
        except Exception as e:
            print(e)
            print("insert_sql插入失败!")
        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()

# class SecinfoMysqlPipeline:
#     def __init__(self,dbpool):
#         self.dbpool=dbpool


#     def process_item(self, item, spider):
#         return item