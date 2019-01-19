# -*- coding: utf-8 -*-
import scrapy
from qiubaipro.qiubaipro.items import QiubaiproItem

class SpidersSpider(scrapy.Spider):
    name = "spiders"
    allowed_domains = ["www.qiushibaike.com"]
    start_urls = ['http://www.qiushibaike.com/']

    # 在这里定义页码和url
    page = 1
    url = 'https://www.qiushibaike.com/8hr/page/{}/'

    def parse(self, response):
        # 解析，首先找到所有的段子div
        div_list= response.xpath('//div[starts-with(@id,"qiushi_tag")]')
        # 遍历，依次提取每一个段子信息
        for div in div_list:
            #创建item对象
            item = QiubaiproItem()
            # 获取头像链接
            item['face_url'] = div.xpath('')
            # 获取用户名
            item['name'] = div.xpath('')
            # 用户年龄
            item['age'] = div.xpath('')
            # 内容
            item['content'] = div.xpath('')
            # 好笑个数
            item['haha_count'] = div.xpath('')
            # 评论个数
            item['comment_count'] = div.xpath('')

            yield item

        # 接着发送请求，爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)