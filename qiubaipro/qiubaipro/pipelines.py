# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
#管道，用来保存数据，
class QiubaiproPipeline(object):
    # 构造方法
    def __init__(self):
        pass
    #开启爬虫的函数
    def open_spider(self,spider):
        #打开文件
        self.fp = open('qiubai.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        '''
        方法名：处理item函数
        item:要处理的数据单元，每一个item过来这个函数都要被掉调用
        spider:当前的爬虫对象
        方法有返回值：return item
        将item保存到文件中

        :param item:
        :param spider:
        :return:
        '''
        # 将item 转化为字典
        d = dict(item)
        # 将字典搞成json
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item
    def close_spider(self,spider):
        #关闭文件
        self.fp.close()
