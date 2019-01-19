# -*- coding: utf-8 -*-
import scrapy
import time

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["so.gushiwen.org"]
    start_urls = ['https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx']


    def parse(self, response):
        # 提取你需要的信息即可
        image_src = 'https://so.gushiwen.org' + response.css('#imgCode::attr(src)').extract_first()
        # 通过登陆时隐藏域的属性获取值
        self.viewstat = response.css('#__VIEWSTATE::attr(value)').extract_first()
        self.viewg = response.css('#__VIEWSTATEGENERATORZ::attr(value)').extract_first()
        yield scrapy.Request(url=image_src,callback=self.download)

    def download(self,response):
        with open('code.png','wb') as fp:
            fp.write(response.body)

        code = input('请输入验证码：')
        # 发送post请求
        formdata = {
            '__VIEWSTATE': 'p+FNs5jY1KPTlnP0u5pLk4kUDi8QiWLUd/OUrIGN1N7OA45uSMgjAsrhOiP08raBreVkyikPi/y6yi4l201RoIMOZVpGL0ktLtxxpZqk1PLX9wneQH/A+c6WP4g=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',
            'from': 'http://so.gushiwen.org/user/collect.aspx',
            'email': '10960639@qq.com',
            'pwd': '123456',
            'code': code,
            'denglu': '登录',
        }
        post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
        yield scrapy.FormRequest(url=post_url,formdata=formdata,callback=self.parse_post)

    def parse_post(self,response):
        with open('lala.html','wb') as fp:
            fp.write(response.body)
