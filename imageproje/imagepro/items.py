# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#item是用来保存爬去数据的容器
#在这里定义字段
import scrapy


class ImageproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片名称
    name = scrapy.Field()
    #发布时间
    publish_time = scrapy.Field()
    # 浏览量
    click = scrapy.Field()
    #收藏量
    collect = scrapy.Field()
    #下载量
    download = scrapy.Field()
    #图片链接
    image_src = scrapy.Field()
