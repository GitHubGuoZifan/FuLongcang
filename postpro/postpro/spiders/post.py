# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["https://cn.bing.com/"]
    start_urls = ['http://https://cn.bing.com//']

    def start_requests(self):
        post_url = 'https://cn.bing.com/ttranslationlookup?&IG=173800F312B648A9A3172BEF6BAAFF4F&IID=translator.5036.1'
        # 表单数据
        formdata = {
            'from': 'zh-CHS',
            'to': 'en',
            'text': '天空',
        }
        # 发送post请求
        yield scrapy.FormRequest(url=post_url,callback=self.parse())

    def parse(self, response):
        print('*' * 50)
        print(response.text)
        print('*' * 50)