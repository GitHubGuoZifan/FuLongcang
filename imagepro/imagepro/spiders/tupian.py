# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imagepro.items import ImageproItem

class TupianSpider(CrawlSpider):
    name = 'tupian'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/nature.html']


    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
        }
    }

    # 写规则，要写两个规则，一个规则是详情页规则，一个是页码连接规则
    detail_link = LinkExtractor(restrict_xpaths='//div[@class="list"]')
    page_link = LinkExtractor(allow=r'/photo-0-11-\d+-0-0-0\.html')
    rules = (
        Rule(page_link, follow=False),
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
