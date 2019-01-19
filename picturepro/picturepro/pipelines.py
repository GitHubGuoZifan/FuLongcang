# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class PictureproPipeline(object):
    # def open_spider(self,spider):
    #     self.fp = open('picture.txt','w',encoding='utf8')
    #
    def process_item(self, item, spider):
        # d = dict(item)
        # string = json.dumps(d,ensure_ascii=False)
        self.download(item)
        return item

    def download(self,item):
        dirname = r'E:\urllib_train\picturepro\picturepro\spiders'
        filename = item['name'] + '.' + item['image_src'].split('.')[-1]
        filepath = os.path.join(dirname,filename)
        urllib.request.urlretrieve(item['image_src'],filepath)
