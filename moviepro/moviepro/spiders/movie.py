# -*- coding: utf-8 -*-
import scrapy
from moviepro.items import MovieproItem

custom_settings = {
# 去重过滤类使用scrapy-redis去重过滤类

'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",

# 调度器使用scrapy-redis的调度器

'SCHEDULER': "scrapy_redis.scheduler.Scheduler",

# 是否允许暂停

'SCHEDULER_PERSIST': True,

'ITEM_PIPELINES': {

    # 如果想保存到redis中，开启这个管道

    'scrapy_redis.pipelines.RedisPipeline': 400,

},

# 配置redis的ip地址和端口
#//:密码@ip
'REDIS_URL': 'redis://:112638@10.35.165.166:6379/2',

'REDIS_HOST': 'localhost',

'REDIS_PORT': 6379,

'REDIS_PASSWORD': '123456' ,

'DOWNLOAD_DELAY': 1,

}

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.id97.com"]
    start_urls = ['http://www.id97.com/']

    def parse(self, response):
        # 首先找到包含电影的所有div
        div_list = response.xpath('//div[@class="container"]//div[@class="col-xs-1-5 col-sm-4 col-xs-6 movie-item"]')
        # 遍历，提取一些信息
        for div in div_list:
            item = MovieproItem()
            # 获取电影海报
            item['post'] = response.xpath('//div[@class="movie-item-in"]//img/@src').extract_first()
            # 获取电影名字
            item['name'] = response.xpath('//div[@class="meta"]/h1/a/text()').extract_first()
            # 获取电影评分
            item['score'] = response.xpath().extract_first().strip('-分')
            # 获取电影类型
            item['mov_type'] = response.xpath('//div[@class="otherinfo"]/text()').extract_first().rstrip('"类型："')
            # 获取电影详情页链接
            item['detail_url'] = response.xpath('//div[@class="meta"]/h1/a/@href').extract_first()
            # 把item实例化对象传过去
            yield scrapy.Request(url=item['detail_url'],callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        # 获取到传递过来的item
        item = response.meta['item']
        # 提取导演
        item['director'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"导演")]/../../td[2]/a/text()').extract_first()
        # 提取编剧
        item['scriptwriter'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"编剧")]/../../td[2]/a/text()').extract()
        # 提取主演
        item['leader'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"主演")]/../../td[2]/a/text()').extract_first()
        # 提取地区
        item['region'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"地区")]/../../td[2]/a/text()').extract_first()
        # 提取语言
        item['language'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"语言")]/../../td[2]/a/text()').extract_first()
        # 提取上映时间
        item['release_time'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"上映时间")]/../../td[2]/a/text()')
        # 提取片长
        item['mins'] = response.xpath('//table/tbody/tr/td/span[contains(text(),"片长")]/../../td[2]/a/text()')
        yield item
