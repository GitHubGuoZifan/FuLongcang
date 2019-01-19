# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影海报
    post = scrapy.Field()
    # 电影名字
    name = scrapy.Field()
    # 电影评分
    score = scrapy.Field()
    # 电影类型
    mov_type = scrapy.Field()
    # 电影详情页链接
    detail_url = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 编剧
    scriptwriter = scrapy.Field()
    # 主演
    leader = scrapy.Field()
    # 地区
    region = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 上映时间
    release_time = scrapy.Field()
    # 片长
    mins = scrapy.Field()


