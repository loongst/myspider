# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CveSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    # url = scrapy.Field()
    # time=scrapy.Field()
    # severity=scrapy.Field()

    CVE_ID=scrapy.Field()
    CWE_ID=scrapy.Field()
    Vulnerability_Type=scrapy.Field()
    Publish_Date=scrapy.Field()
    Update_Date=scrapy.Field()
    Score=scrapy.Field()
    Gained_Access_Level=scrapy.Field()
    Access=scrapy.Field()
    Complexity=scrapy.Field()
    Authentication=scrapy.Field()
    Confidentiality=scrapy.Field()
    Integrity=scrapy.Field()
    Availability=scrapy.Field()
    Description=scrapy.Field()
    pass
