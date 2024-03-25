# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SecinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    time=scrapy.Field()
    severity=scrapy.Field()
    pass

class NoxSecinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    vuln_name=scrapy.Field()
    vuln_name_en=scrapy.Field()
    qvd_code=scrapy.Field()
    cve_code=scrapy.Field()
    cnvd_id=scrapy.Field()
    cnnvd_id=scrapy.Field()
    threat_category=scrapy.Field()
    technical_category=scrapy.Field()
    residence_id=scrapy.Field()
    rating_id=scrapy.Field()
    not_show=scrapy.Field()
    publish_time=scrapy.Field()
    description=scrapy.Field()
    description_en=scrapy.Field()
    change_impact=scrapy.Field()
    operator_hid=scrapy.Field()
    create_hid=scrapy.Field()
    temp=scrapy.Field()
    other_rating=scrapy.Field()
    create_time=scrapy.Field()
    update_time=scrapy.Field()
    latest_update_time=scrapy.Field()
    rating_level=scrapy.Field()
    vuln_type=scrapy.Field()
    poc_flag=scrapy.Field()
    patch_flag=scrapy.Field()
    detail_flag=scrapy.Field()
    tag=scrapy.Field()
    tag_len=scrapy.Field()
    is_rating_level=scrapy.Field()