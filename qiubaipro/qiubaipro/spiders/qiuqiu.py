# -*- coding: utf-8 -*-
import scrapy
#导入连接提取器
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider和Rule类
# Rule:规则， 指定哪个回调来处理这批链接响应
from scrapy.spiders import CrawlSpider, Rule


class QiuqiuSpider(CrawlSpider):
    name = 'qiuqiu'
    # 允许的域名
    allowed_domains = ['www.qiushibaike.com']
    # 起始的url
    start_urls = ['http://www.qiushibaike.com/']
    '''
    rules 是一个元组，里面可以写多个规则，一般就一两个
    rules元组里面存放的都是Rule类对象
    Rule类对象创建的时候需要的参数有：
        参数1：链接提取器
        参数2：callback，要处理响应的回调
            前面的callback  self.xxx  现在的callback   'xxx'
        参数3：follow，跟进，提取的链接响应来了之后，通过callback处理完毕之后，要不要接着按照这些规则去提取链接，接着抓取，如果要，就是True，不要就是False
        默认值：如果规则里面有callback，默认为False
                如果规则里面没有callback，默认为True
    [注]crawl spider的parse函数有单独的作用，千万不能重写，它的作用就是按照规则提取链接的。
    '''
    lk = LinkExtractor(allow=r'Items/')
    rules = (
        # parse_item是自定义函数，随便写
        Rule(lk, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
