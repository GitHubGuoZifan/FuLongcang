# -*- coding: utf-8 -*-
import scrapy
from picturepro.items import PictureproItem
from scrapy.linkextractors import LinkExtractor
class PictureSpider(scrapy.Spider):
    name = "picture"
    allowed_domains = ["www.meizitu.com/"]
    start_urls = ['http://www.meizitu.com/']

    page = 1
    url = 'http://www.mzitu.com/page/{}/'

    def parse(self, response):
        # 得到每一页的链接
        href_list = response.xpath('//ul[@id="pins"]/li/a/@href').extract()
        # 遍历这个列表，依次向每个href发送请求
        print('*' * 50)
        print(href_list)
        print('*' * 50)
        for href in href_list:
            yield scrapy.Request(url=href,callback=self.parse_detail)

        # 接着爬取指定页码的内容
        if self.page < 194:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse_detail(self,response):
        # 创建一个item对象
        item = PictureproItem()
        # 提取图片的名字
        item['name'] = response.xpath('//div[@class="postlist"]/ul/li/a/img/@alt').extract_first()
        # 提取图片的链接
        item['image_src'] = response.xpath('div[@class="postlist"]/ul/li/img/@src').extract_first()
        # yield scrapy.Request(url=item['image_src'],callback=self.next_detail)
        yield item
    # def next_detail(self,response):
    #     le = LinkExtractor(restrict_xpaths='//div[@class="pagenavi"]')
    #     le.extract_links(response)