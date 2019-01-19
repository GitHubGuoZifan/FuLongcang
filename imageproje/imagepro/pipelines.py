# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#这一节是项目管道
import json
import os
import urllib.request
import pymysql

class ImageproPipeline(object):
    #参数spider就是被开启的spider对象
    def open_spider(self,spider):
        self.fp = open('image.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')
        # 下载图片函数
        self.download(item)
        return item
    #关闭数据库对象
    def close_spider(self,spider):
        self.fp.close()