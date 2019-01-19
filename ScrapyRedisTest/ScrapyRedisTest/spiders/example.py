# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider, RedisMixin

"""
将scrapy 改造成分布式有两个问题需要解决
①request 队列集中管理
② 去重集中管理

"""



class ExampleSpider(RedisSpider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    redis_key = 'jobble:start_urls'

    def parse(self, response):
        """
            1. 提取文章列表页中所有文章详情页链接，并交给 parse_detail 方法进行解析
            2. 提取下一页链接，并交给 Scrapy 进行下载
        Args:
            response: 响应信息
        Yields:
            1. 文章详情页链接，交给 parse_detail 解析
            2. 下一页链接，交给 Scrapy 下载
        """
        post_nodes = response.xpath('//div[@id="archive"]')
        for post_node in post_nodes:
            post_url = post_node.xpath('.//div[@class="post-meta"]//a[@class="archive-title"]/@href').extract_first('')
            front_img_url = post_node.xpath('.//div[@class="post-thumb"]//img/@src').extract_first('')
            yield scrapy.Request(url=url.join(response.url, post_url), callback=self.parse_detail,
                                 meta={'front_img_url': front_img_url})
        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        pass


