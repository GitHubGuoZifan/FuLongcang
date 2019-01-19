# -*- coding: utf-8 -*-
import scrapy
from imagepro.items import ImageproItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/tupian/photo-so.html']

    page = 1
    url = 'http://699pic.com/photo-0-0-{}-0-0-0.html'

    def parse(self, response):
        # 得到所有图片的详情页链接
        href_list = response.xpath('//div[@class="list"]/a/@href').extract()
        # 遍历这个列表，依次向每个href发送请求
        for href in href_list:
            print(href)
            yield scrapy.Request(url=href, callback=self.parse_detail)

        # 接着爬取指定页码的内容
        if self.page < 2:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_detail(self, response):
        print(f'-----------------{response.url}-------------')
        # 创建一个item对象
        item = ImageproItem()
        # 提取图片名字
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract()

        print(item['name'])
        # 提取发布时间
        # item['publish_time'] = response.xpath('//div[@class="photo-view"]/div/span[@class="publicityt"]/text()').extract_first().rstrip(' 发布')
        # 提取浏览量
        # item['click'] = response.xpath('//div[@class="photo-view"]/div/span[@class="look"]/read/text()').extract_first()
        # 提取收藏量
        # item['collect'] = response.xpath('//div[@class="photo-view"]/div/span[@class="collect"]/text()').extract_first().rstrip(' 收藏')
        # 提取下载量
        # item['download'] = response.xpath('//div[@class="photo-view"]/div/span[@class="download"]/text()')[1].extract().rstrip(' 下载\t\n')
        # 提取图片的url
        item['image_src'] = response.xpath('//img[@id="photo"]/@src').extract_first()
        print(item['image_src'], '****************************')
        yield item
        # yield scrapy.Request(url=item['image_src'], callback=self.download)

    # def download(self, response):
        # 将图片通过response下载下来即可
        # pass
    #def download(self, item):
#     dirname = r'C:\Users\ZBLi\Desktop\1803\day09\imagepro\imagepro\spiders\images'
#     filename = item['name'] + '.' + item['image_src'].split('.')[-1]
#     filepath = os.path.join(dirname, filename)
#     urllib.request.urlretrieve(item['image_src'], filepath)

