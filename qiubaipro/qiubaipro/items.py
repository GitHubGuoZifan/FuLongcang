# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义你的数据结构
    # 头像链接
    face_url = scrapy.Field()
    # 用户名
    name = scrapy.Field()
    #内容
    scrapy.Field()
    # 好笑个数
    haha_count = scrapy.Field()
    # 评论个数
    comment_count = scrapy.Field()
