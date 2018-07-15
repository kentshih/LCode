# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RecruitItem(scrapy.Item):
    name  = scrapy.Field()
    detailLink = scrapy.Field()
    catalog = scrapy.Field()
    recruitNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()