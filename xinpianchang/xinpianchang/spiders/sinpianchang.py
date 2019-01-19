import requests
import scrapy
from xinpianchang.items import XinpianchangItem
import time
from lxml import etree

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
# 以下几步是为了创建链接创建浏览器而存在的
options = Options()
options.add_argument('--headless')  # 无头-不显示浏览器界面
options.add_argument('--disable-gpu')  #禁用gpu ,不加载图片
# options.binary_location=r'D:\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=r'D:\chromedriver.exe')
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context


class SinpianchangSpider(scrapy.Spider):
    name = "xinpianchang"
    allowed_domains = ["www.xinpianchang.com", "cs.xinpianchang.com"]
    start_urls = ['http://www.xinpianchang.com/channel/index/id-31/sort-like']

    page = 1
    urls = 'http://www.xinpianchang.com/channel/index/id-31/page-{}'
    def parse(self, response):
        video_urls = 'http://www.xinpianchang.com/a{}?from=ArticleList'

        # div_list = response.xpath('//ul[@class="video-list"]')
        div_list = response.xpath('//li[@class="enter-filmplay"]')


        for div in div_list:
            item = XinpianchangItem()  # 遍历,提取一些信息

            # 获取电影海报

            item['image_url'] = div.xpath('.//a[@class="video-cover"]//img/@_src').extract_first()
            print(item['image_url'])

            # 获取视频名称
            item['video_name'] = div.xpath('.//p[@class="fs_14 fw_600 c_b_3 line-hide-1"]/text()').extract_first()
            # item['video_name'] = div.xpath('//p[@class="fs_14 fw_600 c_b_3 line-hide-1"]/text()')
            # 获取视频作者
            item['video_author'] = div.xpath('.//div[@class="info"]/p/text()').extract_first()
            # item['video_author'] = div.xpath('//div[@class="info"]/p/text()')
            # 获取发布时间
            item['release_date'] = div.xpath('.//div[@class="video-hover-con"]/p[@class="fs_12"]/text()').extract_first().rstrip(' 发布')
            # item['release_date'] = div.xpath('//div[@class="video-hover-con"]/p[@class="fs_12"]/text()')
            # 获取视频地址
            url = div.xpath('//div[@class="channel-con"]/ul/li[@class="enter-filmplay"]/@data-articleid').extract_first()
            # url = div.xpath('//div[@class="channel-con"]/ul/li[@class="enter-filmplay"]/@data-articleid')
            item['video_url'] = video_urls.format(url)
            driver.get(item['video_url'])
            item['base_url'] = driver.find_element_by_id('xpc_video').get_attribute('src')
            print('********************************************')
            print(item['base_url'])
            print('*'*35)

            yield item

        if self.page < 2:
            self.page += 1
            url = self.urls.format(self.page)

            yield scrapy.Request(url=url,callback=self.parse)
            driver.quit()