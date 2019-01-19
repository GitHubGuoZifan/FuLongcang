# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imagepro.items import ImageproItem
from scrapy_redis.spiders import RedisCrawlSpider

class YuebingSpider(RedisCrawlSpider):
    name = 'yuebingspider_redis'
    allowed_domains = ['699pic.com']
    # start_urls = ['http://699pic.com/nature.html']
    redis_key = 'yuebingspider:start_urls'

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
        'REDIS_IP': '10.35.165.22',
        'REDIS_PORT': 6379,
        'DOWNLOAD_DELAY': 1,
    }

    # 写规则，要写两个规则，一个规则是详情页规则，一个是页码连接规则
    detail_link = LinkExtractor(restrict_xpaths='//div[@class="list"]')
    page_link = LinkExtractor(allow=r'/photo-0-11-\d+-0-0-0\.html')
    rules = (
        Rule(page_link, follow=True),
        Rule(detail_link, callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        # 创建一个item对象
        item = ImageproItem()
        # 提取图片名字
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract_first()
        # 提取发布时间
        item['publish_time'] = response.xpath('//div[@class="photo-view"]/div/span[@class="publicityt"]/text()').extract_first().rstrip(' 发布')
        # 提取浏览量
        item['click'] = response.xpath('//div[@class="photo-view"]/div/span[@class="look"]/read/text()').extract_first()
        # 提取收藏量
        item['collect'] = response.xpath('//div[@class="photo-view"]/div/span[@class="collect"]/text()').extract_first().rstrip(' 收藏')
        # 提取下载量
        item['download'] = response.xpath('//div[@class="photo-view"]/div/span[@class="download"]/text()')[1].extract().rstrip(' 下载\t\n')
        # 提取图片的url
        item['image_src'] = response.xpath('//img[@id="photo"]/@src').extract_first()
        yield item
