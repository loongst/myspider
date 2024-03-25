# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OdayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Odate_time = scrapy.Field()
    Odescription = scrapy.Field()
    Otype = scrapy.Field()
    Ohits = scrapy.Field()
    Orisk_info = scrapy.Field()
    Ocve = scrapy.Field()
    Oprice = scrapy.Field()
