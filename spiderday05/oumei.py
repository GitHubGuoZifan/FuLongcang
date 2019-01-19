import urllib.request
from lxml import etree
import time,os

#object继承的一个基类，写不写都行
class OuMeiSpider(object):
    def __init__(self,start_page,end_page):
        self.start_page=start_page
        self.end_page=end_page
        self.first_url='http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'
        self.url='http://sc.chinaz.com/tag_tupian/OuMeiMeiNv_{}.html'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
    def get_request(self,page):
        #判断page是不是第一页
        if page==1:
            url=self.first_url
        else:
            url=self.url.format(page)
        request=urllib.request.Request(url=url,headers=self.headers)
        return request

    def parse_content(self,content):
        #生成tree对象
        tree=etree.HTML(content)
        #写xpath得到这个网页中你要的图片的src
        image_src_list=tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
        image_name_list=tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
        for image_src in image_src_list:
            #取出名字
            filename=image_name_list[image_src_list.index(image_src) + '.' + image_src.split('.')[-1]]
            dirname='oumei'
            filepath=os.path.join(dirname,filename)
            print("正在下载%s..."% filename)
            urllib.request.urlretrieve(image_src,filepath)
            print('结束下载 %s'% filename)
            time.sleep(2)
    def run(self):
        for page in range(self.start_page,self.end_page+1):
            print('正在下载第--%s...' % page)
            #拼接url并且生成请求对象
            request=self.get_request(page)
            #发送请求，得到响应
            content = urllib.request.urlopen(request).read().decode('utf8')
            #解析内容
            self.parse_content(content)
            print('结束下载---%s' % page)
            time.sleep(2)


def main():
    start_page=int(input("请输入起始页码："))
    end_page=int(input("请输入结束页码："))

    obj=OuMeiSpider(start_page,end_page)
    obj.run()



if __name__ == '__main__':
    main()