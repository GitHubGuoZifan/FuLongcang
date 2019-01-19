# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import urllib.request

# class ImageproPipeline(object):
#     def open_spider(self, spider):
#         self.fp = open('image.txt', 'w', encoding='utf8')
#
#     def process_item(self, item, spider):
#         d = dict(item)
#         string = json.dumps(d, ensure_ascii=False)
#         self.fp.write(string + '\n')
#         # 下载图片函数
#         # self.download(item)
#         return item
#
#     # def download(self, item):
#     #     dirname = r'C:\Users\ZBLi\Desktop\1803\day09\imagepro\imagepro\spiders\images'
#     #     filename = item['name'] + '.' + item['image_src'].split('.')[-1]
#     #     filepath = os.path.join(dirname, filename)
#     #     urllib.request.urlretrieve(item['image_src'], filepath)
#
#     def close_spider(self, spider):
#         self.fp.close()


# import pymysql
# from scrapy.utils.project import get_project_settings
# class MysqlPipeline(object):
#     def open_spider(self, spider):
#         # 从配置文件中获取哪些参数
#         settings = get_project_settings()
#         # 链接数据库
#         self.conn = pymysql.Connect(host=settings['HOST'], port=settings['PORT'], user=settings['USER'], password=settings['PWD'], db=settings['DB'], charset=settings['CHARSET'])
#         # 获取游标
#         self.cursor = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         sql = 'insert into image(name, publish_time, click, collect, download, image_src) values("%s","%s","%s","%s","%s","%s")' % (item['name'], item['publish_time'], item['click'], item['collect'], item['download'], item['image_src'])
#         # 执行sql语句
#         try:
#             self.cursor.execute(sql)
#             self.conn.commit()
#         except Exception as e:
#             print('*' * 50)
#             print(e)
#             print('*' * 50)
#             self.conn.rollback()
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()


import pymongo
class MongodbPipeline(object):
    def open_spider(self, spider):
        # 链接
        self.conn = pymongo.MongoClient('localhost', 27017)
        # 选择数据库
        self.db = self.conn.tupian
        # 选择集合
        self.col = self.db.image

    def process_item(self, item, spider):
        self.col.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.conn.close()
