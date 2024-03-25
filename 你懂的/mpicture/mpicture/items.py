# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MpictureItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # post_title=scrapy.Field()
    # post_content_img=scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    catgery=scrapy.Field()

