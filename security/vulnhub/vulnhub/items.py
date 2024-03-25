# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VulnhubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    date_release=scrapy.Field()
    series=scrapy.Field()
    mirror=scrapy.Field()
    description=scrapy.Field()
    file_size=scrapy.Field()
    file_format=scrapy.Field()
    operating_system=scrapy.Field()

