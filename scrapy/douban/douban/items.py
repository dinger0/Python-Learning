# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影序列号
    serial_number=scrapy.Field()
    #电影名
    movie_name=scrapy.Field()
    #电影简介
    introduce=scrapy.Field()
    #电影星级
    star=scrapy.Field()
    #电影评价数
    evaluate=scrapy.Field()
    #电影描述
    describe=scrapy.Field()





