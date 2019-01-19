# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request
import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.movie
collection = db.movies
class MovieproPipeline(object):
    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        collection.insert(string)
        return item
    def close_spider(self,spider):
        client.close()