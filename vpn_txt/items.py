# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VpnTxtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title   = scrapy.Field()
    keyword = scrapy.Field()
    content = scrapy.Field()
    url     = scrapy.Field()
    status  = scrapy.Field()
    creat_time = scrapy.Field()

class GetKeywordItem(scrapy.Item):
    keyword_start =scrapy.Field()
    keyword_result=scrapy.Field()
    keyword_sum   =scrapy.Field()
    status        =scrapy.Field()
    creat_time    =scrapy.Field()

