# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs
import pymysql
from twisted.enterprise import adbapi
from pymysql.converters import escape_string

class CveSpiderPipeline:

    #保存到json文件中
    def __init__(self):  
        self.file = codecs.open('guizhou.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  
        self.file.write(line)  
        return item  
        
    def spider_closed(self, spider):  
        self.file.close()

class Mysql_CveSpiderPipeline:
    def __init__(self,dbpool) -> None:
        self.dbpool=dbpool
    
    @classmethod
    def from_settings(cls,settings):
        adbparams=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASS'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        dbpool=adbapi.ConnectionPool('pymysql',**adbparams)
        return cls(dbpool)

    def process_item(self,item,spider):
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addCallback(self.handle_error)
        return item

    def do_insert(self,cursor,item):
        insert_sql='''insert into cve(CVE_ID,CWE_ID,Vulnerability_Type,Publish_Date,Update_Date,Score,Gained_Access_Level,Access,Complexity,Authentication,Confidentiality,Integrity,Availability,Description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(insert_sql,(
            item['CVE_ID'],item['CWE_ID'],item['Vulnerability_Type'],item['Publish_Date'],item['Update_Date'],item['Score'],item['Gained_Access_Level'],item['Access'],item['Complexity'],item['Authentication'],item['Confidentiality'],item['Integrity'],item['Availability'],escape_string(item['Description'])
        ))
        ###注意，如果数据是字符串类型的，则values中的占位符不需要加引号如%s，如果不是，则需要加'%s'

        # ,(
        #     item['CVE_ID'],item['CWE_ID'],item['Vulnerability_Type'],item['Publish_Date'],item['Update_Date'],item['Score'],item['Gained_Access_Level'],item['Access'],item['Complexity'],item['Authentication'],item['Confidentiality'],item['Integrity'],item['Availability'],escape_string(item['Description'])
        # )

    def handle_error(self,failure):
        if failure:
            print(failure)