import json
import os
import urllib.request
import pymysql
from scrapy.utils.project import get_project_settings
class XinpianchangPipeline(object):
    # 参数spider就是被开启的spider对象
    def open_spider(self, spider):
        # 从配置文件中获取参数
        settings = get_project_settings()   # 这个函数传给你一个字典settings,这个字典里有你在settings李米娜配置的所有选项
        # 连接数据库
        self.conn = pymysql.Connect(host=settings['HOST'],port=settings['PORT'],user=settings['USER'],password=settings['PWD'],db=settings['DB'],charset=settings['CHARSET'])
        # 获取游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into image(image_url, video_name, video_author, release_date, video_url,base_url) values("%s","%s","%s","%s","%s","%s")' % (item['image_url'], item['video_name'], item['video_author'], item['release_date'], item['video_url'],item['base_url'])
        # 执行sql语句
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    #关闭数据库对象
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()