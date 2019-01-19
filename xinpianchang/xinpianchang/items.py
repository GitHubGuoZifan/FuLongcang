# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinpianchangItem(scrapy.Item):
    # 图片地址
    image_url = scrapy.Field()
    # 视频名称
    video_name = scrapy.Field()
    # 视频作者
    video_author = scrapy.Field()
    # 发布时间
    release_date = scrapy.Field()
    # 视频地址
    video_url = scrapy.Field()
    # 视频源地址
    base_url = scrapy.Field()