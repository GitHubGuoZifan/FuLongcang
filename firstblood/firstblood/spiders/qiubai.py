# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    #爬虫的名字，可以修改，启动爬虫的时候用
    name = "qiubai"
    #允许的域名列表，域名限制，可以允许多个
    allowed_domains = ["www.qiushibaike.com"]
    #起始url，列表，一般只有一个
    start_urls = ['http://www.qiushibaike.com/']
    #重写父类的函数，自动被调用，回调函数
    #起始url的响应，来了之后就会调用这个函数
    #response:响应对象
    def parse(self, response):
        #首先得到所有的div
        div_list = response.xpath('//div[@id="content-left"]/div')
        items=[]
        for odiv in div_list:
            #用户头像
            user_face = odiv.xpath('./div//img/@src').extract()[0]
            #用户名字
            username = odiv.xpath('./div//h2/text()')[0].extract().strip('\n\t\r')

            item = {
                '用户头像': user_face,
                '用户名': username
            }
            items.append(item)
        return items
